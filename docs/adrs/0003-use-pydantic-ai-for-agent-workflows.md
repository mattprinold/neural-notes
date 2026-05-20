# 0003: Use Pydantic AI for Agent Workflows

## Status

Accepted

## Context

Neural Notes requires AI orchestration tooling capable of supporting:

- structured outputs
- typed agent workflows
- prompt modularity
- maintainable AI pipelines
- evaluation-driven development
- observability integration

The project prioritizes engineering clarity and reliability over rapid prototype-style abstraction layers.

## Decision

Use Pydantic AI for AI agent orchestration and structured workflow execution.

## Consequences

### Positive

- Strong typed workflow support
- Excellent integration with Pydantic models
- Structured outputs improve reliability
- Encourages maintainable prompt engineering
- Lightweight and understandable abstractions
- Fits production-oriented engineering practices

### Negative

- Smaller ecosystem compared to LangChain
- Fewer prebuilt integrations
- Requires more deliberate workflow design

## Alternatives Considered

### LangChain

Pros:
- Large ecosystem
- Extensive integrations

Cons:
- High abstraction complexity
- Difficult debugging in larger workflows
- Encourages framework-heavy architecture

### CrewAI

Pros:
- Easy multi-agent setup

Cons:
- Less suitable for strongly typed workflows
- More focused on autonomous agents than controlled orchestration

### AutoGen

Pros:
- Strong multi-agent experimentation support

Cons:
- Less aligned with deterministic production workflows
- Higher orchestration complexity