from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "profile.json"
README_PATH = ROOT / "README.md"

START = "<!-- AUTO:RECENT-START -->"
END = "<!-- AUTO:RECENT-END -->"


def load_config() -> dict[str, Any]:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def github_request(url: str) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "Mod-With-Miran-profile-automation",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_repositories(username: str) -> list[dict[str, Any]]:
    url = (
        f"https://api.github.com/users/{username}/repos"
        "?sort=pushed&direction=desc&per_page=100&type=owner"
    )
    data = github_request(url)
    if not isinstance(data, list):
        raise RuntimeError("Unexpected GitHub API response.")
    return data


def normalize_language(repo: dict[str, Any]) -> str:
    return repo.get("language") or "Mixed"


def render_recent(repos: list[dict[str, Any]], config: dict[str, Any]) -> str:
    excluded = set(config.get("exclude_repos", []))
    include_forks = bool(config.get("include_forks", False))
    include_archived = bool(config.get("include_archived", False))
    limit = int(config.get("max_recent_repos", 4))

    filtered = []
    for repo in repos:
        if repo.get("name") in excluded:
            continue
        if repo.get("fork") and not include_forks:
            continue
        if repo.get("archived") and not include_archived:
            continue
        filtered.append(repo)

    filtered = filtered[:limit]
    if not filtered:
        return "_No public project repositories to show yet. This section updates automatically._"

    lines = [
        "| Repository | What it is | Stack | Updated |",
        "|---|---|---|---|",
    ]
    for repo in filtered:
        name = repo.get("name", "repository")
        url = repo.get("html_url", "#")
        description = (repo.get("description") or "Public project").replace("|", "\\|")
        language = normalize_language(repo)
        pushed_at = repo.get("pushed_at") or ""
        try:
            updated = datetime.fromisoformat(pushed_at.replace("Z", "+00:00")).strftime("%Y-%m-%d")
        except ValueError:
            updated = "—"
        lines.append(
            f"| [`{name}`]({url}) | {description} | `{language}` | {updated} |"
        )
    return "\n".join(lines)


def replace_section(readme: str, content: str) -> str:
    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END),
        flags=re.DOTALL,
    )
    replacement = f"{START}\n{content}\n{END}"
    if not pattern.search(readme):
        raise RuntimeError("README automation markers are missing.")
    return pattern.sub(replacement, readme)


def main() -> int:
    config = load_config()
    username = config["username"]

    try:
        repos = fetch_repositories(username)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        print(f"GitHub API request failed: {exc}", file=sys.stderr)
        return 2

    current = README_PATH.read_text(encoding="utf-8")
    rendered = render_recent(repos, config)
    updated = replace_section(current, rendered)

    if updated == current:
        print("README already up to date.")
        return 0

    README_PATH.write_text(updated, encoding="utf-8")
    print("README updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
