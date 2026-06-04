# Setup Guide

## Prerequisites

Install:

* Python 3.11+
* Git

Verify:

```bash
python --version
git --version
```

---

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/echogate-ai.git
cd echogate-ai
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a file named:

```text
.env
```

Example:

```env
DEBUG_MODE=false
```

### Note

EchoGate no longer requires Gemini API keys in environment variables.

Users can provide their own Gemini API key directly from the application sidebar when using Gemini AI Mode.

---

## Run Application

```bash
python -m streamlit run src/interfaces/streamlit/app.py
```

The application should open automatically in your browser.

If it does not:

```text
http://localhost:8501
```

---

## Run Tests

```bash
python -m pytest
```

---

## Common Issues

### ModuleNotFoundError: No module named 'src'

Run the application from the project root:

```bash
python -m streamlit run src/interfaces/streamlit/app.py
```

---

### Invalid Gemini API Key

If you see:

```text
The Gemini API key is not valid.
```

Verify that:

* The key was copied correctly
* The key is active in Google AI Studio
* The key has not been deleted or restricted

Get a Gemini API key:

https://ai.google.dev/gemini-api/docs/api-key

---

### Gemini Quota Errors

Examples:

```text
429 RESOURCE_EXHAUSTED
503 UNAVAILABLE
```

Solutions:

* Wait for quota reset
* Use a different Gemini API key
* Switch to Demo Mode

---

### PDF Generation Issues

Verify:

```bash
pip install fpdf2
```

---

## Development Workflow

Recommended workflow:

```text
Develop UI using Demo Mode
        ↓
Run Tests
        ↓
Validate with Gemini AI Mode
        ↓
Commit Changes
```
