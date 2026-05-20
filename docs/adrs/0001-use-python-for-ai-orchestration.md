# 0001: Use Python for AI Orchestration

## Status

Accepted

## Context

Neural Notes requires an orchestration language capable of supporting:

- AI workflows
- Retrieval pipelines
- Embedding generation
- Structured outputs
- Evaluation tooling
- Observability integrations
- Rapid experimentation

The language should also have strong ecosystem support for modern LLM tooling and data workflows.

## Decision

Use Python as the primary language for AI orchestration and backend workflows.

## Consequences

### Positive

- Strong ecosystem for AI/ML tooling
- Excellent support for OpenAI and embedding libraries
- Mature observability ecosystem
- Rapid prototyping and iteration
- Strong community support
- Excellent compatibility with vector databases and AI frameworks

### Negative

- Lower runtime performance compared to Go or Rust
- Dynamic typing can introduce runtime issues if not carefully managed
- Packaging and environment management can be inconsistent without tooling discipline

## Alternatives Considered

### Java

Pros:
- Strong typing
- Mature enterprise ecosystem

Cons:
- Slower iteration for AI experimentation
- Smaller modern LLM tooling ecosystem

### TypeScript

Pros:
- Excellent developer experience
- Strong web ecosystem

Cons:
- Weaker AI ecosystem compared to Python
- Fewer mature embedding/retrieval libraries