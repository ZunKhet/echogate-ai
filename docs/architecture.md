# Architecture

## Overview

EchoGate follows Clean Architecture principles to separate business rules from frameworks, external services, and user interfaces.

The goal is to make the system maintainable, testable, and easy to extend.

## High-Level Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
Application Layer
 │
 ▼
Domain Layer
 │
 ▼
Infrastructure Layer
```

## Layers

### Domain Layer

Location:

```text
src/domain/
```

Responsibilities:

* Core business entities
* Business rules
* Domain constants

Examples:

```text
Story
Chapter
Choice
ImageAnalysis
```

The Domain layer contains no Streamlit code, no AI provider code, and no external dependencies.

This layer is the heart of the application.

---

### Application Layer

Location:

```text
src/application/
```

Responsibilities:

* Use cases
* DTOs
* Ports
* Mappers

Examples:

```text
StoryService
ExportStoryUseCase
AIStoryPort
StoryRepositoryPort
```

The Application layer coordinates workflows but does not know how AI generation or PDF export is implemented.

---

### Infrastructure Layer

Location:

```text
src/infrastructure/
```

Responsibilities:

* AI provider implementations
* PDF generation
* Data persistence

Examples:

```text
GeminiStoryAdapter
FakeStoryAdapter
PDFExportAdapter
InMemoryStoryRepository
```

The Infrastructure layer implements the contracts defined by the Application layer.

---

### Interface Layer

Location:

```text
src/interfaces/
```

Responsibilities:

* User interface
* User interactions

Current implementation:

```text
Streamlit
```

The Interface layer communicates only with Application use cases.

---

## Dependency Rule

Dependencies always point inward.

```text
Interface
    ↓
Application
    ↓
Domain
```

Infrastructure depends on Application contracts.

```text
Infrastructure
    ↓
Application
```

The Domain layer never depends on Streamlit, Gemini, or PDF libraries.

---

## Story Generation Flow

```text
Upload Image
      │
      ▼
Analyze Image
      │
      ▼
Generate Story Title
      │
      ▼
Generate Chapter 1
      │
      ▼
User Selects Choice
      │
      ▼
Generate Next Chapter
      │
      ▼
Finalize Story
      │
      ▼
Export PDF
```

---

## AI Provider Abstraction

EchoGate uses a Port-and-Adapter pattern.

Application defines:

```text
AIStoryPort
```

Infrastructure provides implementations:

```text
FakeStoryAdapter
GeminiStoryAdapter
```

This allows AI providers to be swapped without changing business logic.

---

## PDF Export Flow

```text
Story
   │
   ▼
ExportStoryUseCase
   │
   ▼
PDFExportAdapter
   │
   ▼
Generated PDF
```

The PDF implementation can be replaced without affecting the Domain layer.

---

## Testing Strategy

The project includes:

* Unit tests for domain entities
* Mapper tests
* Story service tests

The FakeStoryAdapter allows testing the entire application without external AI dependencies.

---

## Design Decisions

### Why Clean Architecture?

Benefits:

* Easier testing
* Easier maintenance
* Replaceable AI providers
* Replaceable UI framework
* Better separation of concerns

### Why Streamlit?

Benefits:

* Rapid prototyping
* Minimal frontend code
* Fast iteration

### Why AI Provider Abstraction?

Benefits:

* Gemini can be replaced later
* Fake provider enables offline testing
* Multiple providers can be supported in the future
