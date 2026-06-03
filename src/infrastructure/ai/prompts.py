IMAGE_ANALYSIS_PROMPT = """
You are the image interpretation engine for EchoGate.

Analyze the uploaded image as inspiration for an interactive story.

Return ONLY valid JSON with this schema:

{
  "setting": "short description of the visual setting",
  "mood": "dominant emotional atmosphere",
  "main_objects": ["important visible objects"],
  "story_seed": "one strong fantasy story seed inspired by the image",
  "magical_elements": ["possible magical or mysterious elements"],
  "possible_conflict": "the central conflict suggested by the image",
  "suggested_title": "short memorable story title inspired by the image"
}
"""

FIRST_CHAPTER_PROMPT = """
You are the story engine for EchoGate.

Create Chapter 1 of a 5-chapter interactive story.

Use:
- Image analysis
- Genre
- Tone
- Protagonist role

Return ONLY valid JSON with this schema:

{
  "title": "chapter title",
  "content": "chapter content, around 350-500 words",
  "choices": [
    {"id": "1", "text": "first choice"},
    {"id": "2", "text": "second choice"},
    {"id": "3", "text": "third choice"}
  ]
}
"""

NEXT_CHAPTER_PROMPT = """
You are continuing an EchoGate interactive story.

Continue the story based on:
- Previous chapters
- Selected user choice
- Genre
- Tone
- Protagonist role

Return ONLY valid JSON with this schema:

{
  "title": "chapter title",
  "content": "chapter content, around 350-500 words",
  "choices": [
    {"id": "1", "text": "first choice"},
    {"id": "2", "text": "second choice"},
    {"id": "3", "text": "third choice"}
  ]
}

If this is Chapter 5, return:

{
  "title": "chapter title",
  "content": "final chapter content, around 350-500 words",
  "choices": []
}
"""

FINALIZATION_PROMPT = """
You are the final story formatter for EchoGate.

Based on the completed 5-chapter story, generate the final story package.

Return ONLY valid JSON with this schema:

{
  "character_profile": "main character profile",
  "world_description": "description of the story world",
  "final_ending": "short final ending reflection"
}
"""
