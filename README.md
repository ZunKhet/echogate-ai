# EchoGate 🌌

EchoGate is an AI-powered interactive storytelling application that transforms an uploaded image into a branching fantasy adventure.

The application analyzes an image, extracts storytelling elements such as mood, setting, and visual objects, and generates an interactive story that evolves through user choices. The final story can be exported as a PDF book with an optional cover image.

## Features

* Upload an image as story inspiration
* AI-generated story title
* AI image analysis ("The Gate's Vision")
* Interactive branching story choices
* Three-chapter adventure structure
* Character profile generation
* World description generation
* Final ending generation
* PDF export
* Optional uploaded image on PDF cover page
* Clean Architecture implementation

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### AI

* Gemini API (optional)
* Fake Story Provider (development mode)

### Testing

* Pytest

### Document Generation

* FPDF2

## Architecture

EchoGate follows Clean Architecture principles.

```text
Streamlit UI
    ↓
Application Layer
    ↓
Domain Layer
    ↓
Infrastructure Layer
```

Project structure:

```text
src/
├── domain/
├── application/
├── infrastructure/
├── interfaces/
└── config/
```

## Running Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/echogate-ai.git
cd echogate-ai
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python -m streamlit run src/interfaces/streamlit/app.py
```

## Configuration

Create a `.env` file:

```env
AI_PROVIDER=fake
DEBUG_MODE=false
```

To use Gemini:

```env
AI_PROVIDER=gemini
GEMINI_API_KEY=YOUR_API_KEY
DEBUG_MODE=false
```

## Running Tests

```bash
python -m pytest
```

## Development Notes

The project supports two AI providers:

* FakeStoryAdapter
* GeminiStoryAdapter

The fake provider allows the entire application workflow to be tested without consuming API quota.

## Future Improvements

* Additional AI providers
* Story length customization
* Multiple story genres
* Story history persistence
* Public deployment
* Multi-language support
