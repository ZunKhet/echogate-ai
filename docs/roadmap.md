# Roadmap

This document outlines the development journey of EchoGate and planned future improvements.

---

# Version 0.1 — Foundation

Status: Completed ✅

## Architecture

* Clean Architecture implementation
* Domain layer
* Application layer
* Infrastructure layer
* Interface layer

## Story Engine

* Story entity
* Chapter entity
* Choice entity
* ImageAnalysis entity

## Story Flow

* Upload image
* Generate title
* Generate story
* Branching choices
* Three-chapter structure

## Export

* PDF export
* Optional cover image

## Testing

* Domain tests
* Service tests
* Mapper tests

---

# Version 0.2 — AI Integration

Status: Completed ✅

## AI Features

* Gemini integration
* Image analysis
* Story title generation
* Chapter generation
* Story finalization

## Reliability

* JSON validation
* DTO validation using Pydantic
* FakeStoryAdapter fallback

## Development Support

* Debug mode
* Environment-based provider switching

---

# Version 0.3 — Portfolio Release

Status: Current 🚀

Goals:

* Complete documentation
* Architecture diagrams
* Screenshots
* Improved README
* Public GitHub repository

Deliverables:

* Recruiter-friendly repository
* Local setup instructions
* Technical documentation

---

# Future Version 0.4 — Persistence

Status: Planned

Potential features:

* SQLite support
* Story history
* Story library
* Continue previous stories

Possible repositories:

```text
SQLiteStoryRepository
PostgresStoryRepository
```

---

# Future Version 0.5 — Multi-Provider AI

Status: Planned

Potential providers:

* Gemini
* OpenAI
* Groq
* OpenRouter
* Ollama

Benefits:

* Lower vendor lock-in
* Better cost control
* Improved reliability

---

# Future Version 0.6 — User Experience

Status: Planned

Potential features:

* Story length selection
* Multiple endings
* More genres
* More protagonist roles
* Story illustrations
* Theme customization

---

# Future Version 0.7 — User Accounts

Status: Planned

Potential features:

* Authentication
* Personal story library
* Story sharing
* Cloud storage

---

# Future Version 1.0

Vision:

A complete AI storytelling platform that transforms images into interactive adventures and allows users to create, save, share, and export personalized stories.

Potential capabilities:

* Multi-language stories
* AI-generated illustrations
* Audio narration
* Story collections
* Mobile application
* Community story sharing

---

# Lessons Learned

Key engineering lessons from EchoGate:

* Clean Architecture improves maintainability.
* AI output should always be validated.
* Provider abstraction reduces vendor lock-in.
* Testing becomes easier with fake adapters.
* Documentation is part of software engineering.
* Prototype applications should optimize for simplicity before scale.
