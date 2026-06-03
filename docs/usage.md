# Usage Guide

## Overview

EchoGate transforms an uploaded image into an interactive AI-generated adventure story.

The story is generated chapter by chapter based on user choices and can be exported as a PDF book.

---

## Step 1: Upload an Image

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

## Step 2: Configure Story Settings

Optional settings:

### Story Title

Leave empty:

```text
AI generates a title
```

Or enter your own title.

---

### Genre

Available genres:

* Fantasy
* Mystery
* Sci-fi
* Adventure
* Dark Fairytale
* Cozy Magical

---

### Tone

Available tones:

* Mysterious
* Epic
* Dreamy
* Dark
* Hopeful
* Emotional

---

### Protagonist Role

Available roles:

* Explorer
* Wanderer
* Mage
* Guardian
* Dreamer
* Lost Traveler

---

## Step 3: Open the Gate

Click:

```text
✨ Open the Gate
```

EchoGate will:

1. Analyze the image
2. Generate story inspiration
3. Generate a title
4. Generate Chapter 1

---

## Step 4: Explore The Gate's Vision

The Gate's Vision displays:

### Setting

Where the story takes place.

### Mood

Atmosphere of the story.

### Key Elements

Important objects detected from the image.

### First Echo

Initial story premise.

### Hidden Tension

Main conflict that drives the adventure.

---

## Step 5: Continue the Story

Read the chapter.

Select one of the available choices.

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

The selected choice influences the next chapter.

---

## Step 6: Reach the Ending

After the final chapter, EchoGate generates:

### Character Profile

Summary of the protagonist.

### World Description

Description of the story world.

### Final Ending

Story conclusion.

---

## Step 7: Export PDF

Enable:

```text
Include uploaded image on cover page
```

(Optional)

Click:

```text
Prepare PDF
```

Then:

```text
Download Story PDF
```

The generated PDF contains:

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

## Development Mode

When using:

```env
AI_PROVIDER=fake
```

EchoGate uses the FakeStoryAdapter.

Benefits:

* No API cost
* No quota limits
* Faster testing

This mode is recommended for UI development and testing.

---

## Gemini Mode

When using:

```env
AI_PROVIDER=gemini
```

EchoGate generates real AI content.

Requirements:

* Gemini API key
* Internet connection

Note:

Free-tier Gemini usage may be subject to quotas and rate limits.
