# 0002: Use Qdrant for Vector Storage

## Status

Accepted

## Context

Neural Notes requires a vector database capable of supporting:

- semantic search
- embedding storage
- retrieval-augmented generation (RAG)
- metadata filtering
- local development workflows
- future production scalability

The system should support fast experimentation while remaining production-oriented.

## Decision

Use Qdrant as the primary vector database for semantic retrieval workflows.

## Consequences

### Positive

- Strong developer experience
- Simple local development with Docker
- Excellent metadata filtering support
- Good performance for semantic retrieval workloads
- Open-source and self-hostable
- Strong Python ecosystem support
- Suitable for both MVP and future scaling

### Negative

- Additional infrastructure component to manage
- Smaller ecosystem than some older databases
- Requires operational knowledge for production deployment

## Alternatives Considered

### Pinecone

Pros:
- Fully managed
- Production-ready infrastructure

Cons:
- Vendor lock-in
- Ongoing operational cost
- Less suitable for local-first development

### Weaviate

Pros:
- Rich feature set
- Strong hybrid search capabilities

Cons:
- More operational complexity
- Larger infrastructure footprint

### pgvector

Pros:
- Keeps vectors within PostgreSQL
- Simple operational model

Cons:
- Less specialized for vector workloads
- Reduced flexibility for future retrieval experimentation