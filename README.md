# EchoGate

EchoGate is a multimodal AI storytelling app that turns an uploaded image into an interactive five-chapter adventure.

## Features

- Upload an image as story inspiration
- Choose genre, tone, and protagonist role
- Generate interactive story chapters
- Select choices to continue the story
- Generate character profile, world description, and ending
- Export the completed story as a PDF
- Optionally include the uploaded image on the PDF cover

## Architecture

EchoGate follows Clean Architecture:

- `domain/` — core story entities and business rules
- `application/` — use cases, ports, DTOs, and mappers
- `infrastructure/` — AI adapters, persistence, PDF export
- `interfaces/` — Streamlit UI
- `config/` — environment settings

## Run Locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m streamlit run src/interfaces/streamlit/app.py