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

Windows:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
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

### Fake Provider

Recommended for development:

```env
AI_PROVIDER=fake
DEBUG_MODE=false
```

This mode requires no API key.

---

### Gemini Provider

```env
AI_PROVIDER=gemini
GEMINI_API_KEY=YOUR_API_KEY
DEBUG_MODE=false
```

---

## Run Application

```bash
python -m streamlit run src/interfaces/streamlit/app.py
```

The application should open automatically in the browser.

If it does not open automatically:

```text
http://localhost:8501
```

---

## Run Tests

Execute:

```bash
python -m pytest
```

Expected result:

```text
All tests passed
```

---

## Common Issues

### ModuleNotFoundError: No module named 'src'

Run the application from the project root:

```bash
python -m streamlit run src/interfaces/streamlit/app.py
```

Do not run:

```bash
streamlit run src/interfaces/streamlit/app.py
```

unless your environment is configured correctly.

---

### Gemini Quota Errors

Examples:

```text
429 RESOURCE_EXHAUSTED
503 UNAVAILABLE
```

Solutions:

* Switch to fake provider
* Wait for quota reset
* Use a different AI provider

---

### PDF Generation Issues

Make sure:

```bash
pip install fpdf2
```

is installed correctly.

---

## Development Workflow

Recommended workflow:

```text
Develop UI using FakeStoryAdapter
        ↓
Run Tests
        ↓
Switch to Gemini
        ↓
Validate AI Output
        ↓
Commit Changes
```
