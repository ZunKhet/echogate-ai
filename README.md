# EchoGate 🌌

EchoGate is an AI-powered interactive storytelling application that transforms an uploaded image into a branching adventure.

Upload an image, choose your story style, and let EchoGate generate an interactive narrative inspired by the visual elements, mood, and atmosphere of the image. The story evolves through user choices and can be exported as a PDF storybook.

---

## Features

### Image-to-Story Generation

* Upload an image as story inspiration
* AI-powered image analysis
* Automatic story title generation
* Story seed generation based on image content

### Interactive Storytelling

* Branching story choices
* Multi-chapter adventure structure
* Character profile generation
* World description generation
* Final ending generation

### Story Engines

#### Demo Mode

* No API key required
* Uses the built-in `FakeStoryAdapter`
* Ideal for quickly exploring the application

#### Gemini AI Mode

* Uses the user's own Gemini API key
* Generates richer AI-powered stories
* API keys are used only during the current session and are never stored

Get a Gemini API key:

https://ai.google.dev/gemini-api/docs/api-key

### Export

* PDF story export
* Optional uploaded image on PDF cover page

### Architecture

* Clean Architecture
* Dependency inversion through ports and adapters
* Domain-driven design principles
* Testable application layer

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### AI

* Gemini API
* Fake Story Provider

### Testing

* Pytest

### Document Generation

* FPDF2

---

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
├── application/
├── config/
├── domain/
├── infrastructure/
└── interfaces/
```

### Story Generation Flow

```text
Image Upload
      ↓
Image Analysis
      ↓
Story Generation
      ↓
User Choice
      ↓
Next Chapter
      ↓
Story Completion
      ↓
PDF Export
```

### AI Adapter Architecture

```text
AIStoryPort
     │
     ├── FakeStoryAdapter
     │
     └── GeminiStoryAdapter
```

---

## Running Locally

Clone the repository:

```bash
git clone https://github.com/ZunKhet/echogate-ai.git
cd echogate-ai
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run src/interfaces/streamlit/app.py
```

---

## Configuration

Create a `.env` file:

```env
DEBUG_MODE=false
```

### Using Gemini

No Gemini API key is required in `.env`.

Simply:

1. Launch the application
2. Select **Gemini AI Mode**
3. Enter your Gemini API key in the sidebar
4. Start generating stories

---

## Running Tests

```bash
python -m pytest
```

---

## Development Notes

EchoGate supports multiple story-generation providers through the `AIStoryPort` abstraction.

Current implementations:

* `FakeStoryAdapter`
* `GeminiStoryAdapter`

This architecture makes it easy to add additional AI providers in the future without modifying the application layer.

---

## Future Improvements

* Additional AI providers
* Story length customization
* More genres and storytelling styles
* Story persistence and user library
* Multi-language support
* Save and resume stories
* Audio narration
* Custom cover page themes

---

## License

This project is licensed under the MIT License.
