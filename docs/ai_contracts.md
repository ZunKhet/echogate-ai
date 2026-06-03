# EchoGate AI Contracts

EchoGate expects every AI provider to return structured JSON.

These contracts must be followed by:

- FakeStoryAdapter
- GeminiStoryAdapter
- Future OpenAIStoryAdapter
- Future ClaudeStoryAdapter

The application should not depend on raw AI text.

---

## 1. Image Analysis Contract

Used after the user uploads an image.

### Expected JSON

```json
{
  "setting": "ancient forest gate surrounded by mist",
  "mood": "mysterious",
  "main_objects": ["gate", "forest", "mist", "moonlight"],
  "story_seed": "A forgotten gate awakens when the moonlight touches its runes.",
  "magical_elements": ["ancient runes", "hidden portal", "whispering mist"],
  "possible_conflict": "The gate opens only for someone who is willing to lose a memory.","suggested_title": "The Whispering Gate"
}
```

### Rules

- `setting` should describe the visual environment.
- `mood` should describe the emotional atmosphere.
- `main_objects` should include important visible objects.
- `story_seed` should be one strong story idea.
- `magical_elements` should contain fantasy or mysterious elements inspired by the image.
- `possible_conflict` should suggest the main tension of the story.
- `suggested_title` should be a short, memorable book title (3–8 words preferred).

### Title Priority

1. User-entered title (highest priority)
2. AI `suggested_title`
3. Fallback title ("Untitled Echo")

The application uses the first available title.

---

## 2. Chapter Generation Contract

Used for Chapter 1 and Chapters 2–5.

### Expected JSON for Chapters 1–4

```json
{
  "title": "The First Echo",
  "summary": "The protagonist discovers a forgotten gate that begins whispering their name.",
  "content": "The forest had been silent for one hundred years...",
  "choices": [
    {
      "id": "1",
      "text": "Step through the glowing gate"
    },
    {
      "id": "2",
      "text": "Follow the whispering path"
    },
    {
      "id": "3",
      "text": "Touch the ancient symbol"
    }
  ]
}
```

### Expected JSON for Chapter 5

```json
{
  "title": "The Last Echo",
  "summary": "The protagonist faces the final truth behind the gate.",
  "content": "At the heart of the forgotten realm, the final echo waited...",
  "choices": []
}
```

### Rules

- `title` should be short and memorable.
- `summary` should be one sentence.
- `content` should be around 350–500 words.
- Chapters 1–4 must contain exactly 3 choices.
- Chapter 5 must contain an empty `choices` list.
- Choice IDs must be strings: `"1"`, `"2"`, `"3"`.
- Choices should create meaningful story branches, not simple yes/no actions.
- The story must stay consistent with previous chapters.

---

## 3. Story Finalization Contract

Used after Chapter 5 is complete.

### Expected JSON

```json
{
  "character_profile": "The protagonist is a curious explorer who is brave enough to face forgotten truths but gentle enough to protect what remains.",
  "world_description": "The story takes place in a hidden realm connected by ancient gates, where memories become echoes and choices reshape the paths between worlds.",
  "final_ending": "The gate closed, but the final echo remained within the protagonist, reminding them that every world leaves something behind."
}
```

### Rules

- `character_profile` should describe the main character.
- `world_description` should summarize the setting, magic, rules, and atmosphere.
- `final_ending` should give emotional closure.
- Do not introduce a completely new plot in the finalization.
- Finalization should summarize and deepen the completed story.

---

## Provider Rule

All AI providers must return JSON matching these contracts.

The application converts AI responses into domain entities using DTO models.

Flow:

```text
AI JSON response
↓
Pydantic DTO
↓
Domain Entity
↓
StoryService
↓
Streamlit UI / PDF Export
```