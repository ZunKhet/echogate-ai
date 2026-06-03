# Project Decisions

This document explains the key architectural and engineering decisions made during the development of EchoGate.

The goal is to document not only what was built, but also why certain approaches were chosen.

---

# Why Clean Architecture?

EchoGate follows Clean Architecture principles.

Benefits:

* Separation of concerns
* Easier testing
* Easier maintenance
* Replaceable AI providers
* Replaceable user interfaces
* Clear project organization

The architecture allows the application logic to remain independent from Streamlit, Gemini, and PDF generation libraries.

---

# Why Domain-Driven Structure?

The project is organized around business concepts rather than technologies.

Core concepts include:

```text
Story
Chapter
Choice
ImageAnalysis
```

This makes the code easier to understand and extend.

---

# Why Streamlit?

The project is intended as a portfolio application and prototype.

Streamlit provides:

* Fast development
* Minimal frontend complexity
* Rapid experimentation
* Easy demonstration of AI workflows

The architecture intentionally isolates Streamlit inside the Interface layer so it can be replaced later.

Potential future replacements:

```text
React
Next.js
Flutter
Desktop UI
```

without changing business logic.

---

# Why AI Provider Abstraction?

AI providers are external dependencies.

Instead of calling Gemini directly from the UI, EchoGate defines:

```text
AIStoryPort
```

and implements:

```text
FakeStoryAdapter
GeminiStoryAdapter
```

Benefits:

* Easier testing
* Easier provider replacement
* Reduced vendor lock-in

Future providers could include:

```text
OpenAI
Groq
OpenRouter
Ollama
```

without changing the application layer.

---

# Why FakeStoryAdapter?

AI APIs introduce:

* Cost
* Quotas
* Rate limits
* Network failures

The FakeStoryAdapter enables:

* Offline development
* UI testing
* PDF testing
* Automated testing

without consuming API quota.

---

# Why PDF Export?

Generated stories should be portable.

PDF export allows users to:

* Save stories
* Share stories
* Archive stories

The exported PDF includes:

* Cover page
* Story chapters
* Character profile
* World description
* Final ending

---

# Why Three Chapters?

The original design used five chapters.

The project was later simplified to three chapters.

Reasons:

* Lower API cost
* Faster generation
* Better user experience
* Reduced Gemini quota usage
* Easier story completion

The structure still supports:

```text
Beginning
Conflict
Resolution
```

which is sufficient for a portfolio demonstration.

---

# Why Structured JSON Responses?

AI output is required to follow predefined schemas.

Examples:

```text
ImageAnalysisResponse
ChapterResponse
StoryFinalizationResponse
```

Benefits:

* Predictable parsing
* Strong validation
* Better reliability
* Easier testing

Pydantic is used to validate AI-generated content before it enters the application.

---

# Why Session-Based Storage?

The current implementation uses:

```text
InMemoryStoryRepository
```

Reasons:

* Simplicity
* No database setup
* Faster development

This approach is sufficient for a prototype.

Future versions could use:

```text
SQLite
PostgreSQL
MongoDB
Cloud Storage
```

without changing application logic.

---

# Future Improvements

Potential future enhancements include:

* Persistent story storage
* Multiple AI providers
* Multi-language support
* Story history
* User accounts
* Public deployment
* Story illustrations
* Audio narration
* Story sharing
* Mobile application

The current architecture was designed to support these extensions with minimal changes.
