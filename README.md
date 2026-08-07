# Miran

### AI Engineer · Secure AI Systems · Backend · RAG

I build production-oriented AI systems where models operate inside reliable backend, retrieval, authorization, and security boundaries.

[![Profile Automation](https://github.com/miransec/miransec/actions/workflows/update-profile.yml/badge.svg)](https://github.com/miransec/miransec/actions/workflows/update-profile.yml)

## `~/currently`

- shipped **[VaaniDesk](https://github.com/miransec/vaanidesk)** — multilingual AI customer-support platform with controlled actions and hybrid RAG
- shipped the latest **[AtlasCore](https://github.com/miransec/atlascore)** UI v2 experience — secure enterprise AI infrastructure for knowledge, retrieval, and grounded AI workflows
- exploring the intersection of AI engineering and cybersecurity

## Featured systems

### AtlasCore
**Secure enterprise AI infrastructure for knowledge, retrieval, and grounded AI workflows.**

A multi-tenant AI platform built around database-enforced isolation, workspace-scoped knowledge, hybrid retrieval, evidence-gated answering, and auditable access control.

`FastAPI` · `PostgreSQL RLS` · `pgvector` · `Redis` · `Next.js` · `RBAC` · `grounded AI` · `evaluation`

**Latest verified UI v2:**
- **717 backend tests passed**
- **46/46 deterministic evaluations passed**
- Ruff clean
- mypy `--strict` clean across 90 source files
- frontend lint, type-check, Vitest, and production build passed
- FORCE RLS and restricted runtime DB-role invariants preserved

> Repository: [miransec/atlascore](https://github.com/miransec/atlascore)

### VaaniDesk
**Multilingual AI Customer Support Platform**

A production-oriented support system for multilingual conversations, controlled business actions, access-controlled knowledge retrieval, and secure customer workflows.

`multilingual AI` · `controlled tool calling` · `human approval` · `hybrid RAG` · `pgvector` · `authorization` · `idempotency` · `prompt-injection defenses`

> Repository: [miransec/vaanidesk](https://github.com/miransec/vaanidesk)

## `~/stack`

**AI / ML**  
`Python` `RAG` `Embeddings` `LLM APIs` `Evaluation`

**Backend**  
`FastAPI` `PostgreSQL` `SQLAlchemy` `Redis` `REST APIs`

**AI infrastructure**  
`pgvector` `Docker` `OpenTelemetry`

**Frontend**  
`Next.js` `TypeScript` `Tailwind CSS`

**Engineering**  
`Git` `GitHub Actions` `pytest` `Ruff` `mypy`

## `~/principles`

- models are untrusted components
- authorization belongs outside prompts
- retrieval should be measurable and evidence-backed
- sensitive actions require explicit approval
- state-changing tools should be idempotent
- production claims require tests and evidence

## `~/identity`

```python
class Miran:
    focus = [
        "AI systems",
        "backend engineering",
        "secure retrieval",
        "agent security",
        "production infrastructure",
    ]

    shipped = ["VaaniDesk", "AtlasCore UI v2"]

    def philosophy(self) -> str:
        return "Build it. Test it. Measure it. Secure it."
```

## Connect

- Portfolio: [muhammadmiran.com](https://muhammadmiran.com)
- GitHub: [@miransec](https://github.com/miransec)
- Email: [contact@muhammadmiran.com](mailto:contact@muhammadmiran.com)
