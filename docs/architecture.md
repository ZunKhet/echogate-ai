# EchoGate Architecture

EchoGate follows Clean Architecture.

## Layers

- Domain: story entities
- Application: use cases and ports
- Infrastructure: AI, persistence, document export
- Interfaces: Streamlit UI

## Current implementation

- Streamlit frontend
- Fake AI adapter
- In-memory story repository

## Future implementation

- Gemini adapter
- PDF exporter
- SQLite/PostgreSQL repository
- React or FastAPI interface