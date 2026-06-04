# Usage Guide

## Overview

EchoGate transforms an uploaded image into an interactive AI-generated adventure story.

The story evolves through user choices and can be exported as a PDF storybook.

---

## Step 1: Choose a Story Engine

Open the sidebar and select one of the available modes.

### Demo Mode

* No API key required
* Uses the built-in FakeStoryAdapter
* Ideal for testing and exploration

### Gemini AI Mode

* Uses your own Gemini API key
* Generates richer AI-powered stories

To use Gemini AI Mode:

1. Select **Gemini AI Mode**
2. Enter your Gemini API key
3. Upload an image
4. Open the Gate

Get a Gemini API key:

https://ai.google.dev/gemini-api/docs/api-key

---

## Step 2: Upload an Image

Click:

```text
Upload an image to begin your story
```

Supported formats:

* JPG
* JPEG
* PNG

The uploaded image becomes the inspiration for the story.

---

## Step 3: Configure Story Settings

### Story Title

Leave empty to allow EchoGate to generate a title automatically.

Or provide your own title.

### Genre

Choose the genre of your adventure.

### Tone

Choose the overall storytelling tone.

### Protagonist Role

Choose the role of the main character.

---

## Step 4: Open the Gate

Click:

```text
✨ Open the Gate
```

EchoGate will:

1. Analyze the image
2. Generate story inspiration
3. Generate a story title
4. Generate Chapter 1

---

## Step 5: Explore The Gate's Vision

The Gate's Vision displays:

### Setting

Where the story takes place.

### Mood

The atmosphere of the story.

### Key Elements

Important objects identified from the image.

### First Echo

The initial story premise.

### Hidden Tension

The main conflict driving the adventure.

---

## Step 6: Continue the Story

Read the current chapter.

Choose one of the available paths.

Example:

```text
Trust the hidden voice
Search for the lost map
Enter the silver tower
```

Click:

```text
Continue the Story
```

Your choice influences the next chapter.

---

## Step 7: Reach the Ending

After the final chapter, EchoGate generates:

### Character Profile

Summary of the protagonist.

### World Description

Description of the story world.

### Final Ending

The conclusion of the adventure.

---

## Step 8: Export PDF

Optionally enable:

```text
Include uploaded image on cover page
```

Click:

```text
Prepare PDF
```

Then:

```text
Download Story PDF
```

The exported PDF includes:

* Cover page
* Story chapters
* Character profile
* World description
* Final ending

---

## Start a New Story

Click:

```text
🆕 Start New Story
```

This clears:

* Current story
* Uploaded image
* Generated PDF

and starts a new adventure.

---

## Story Engine Locking

Once a story starts, EchoGate locks the selected Story Engine for the entire adventure.

For example:

```text
Start with Gemini AI Mode
        ↓
Generate Chapter 1
        ↓
Continue Story
        ↓
Gemini remains active
```

This ensures a consistent storytelling experience throughout the story.

---

## Error Handling

### Invalid Gemini API Key

EchoGate displays a friendly error message if the provided Gemini API key is invalid.

### Gemini Quota Limits

If Gemini quota limits are reached, EchoGate will notify the user and suggest trying again later or switching to Demo Mode.
