IMAGE_ANALYSIS_PROMPT = """
Analyze the uploaded image as inspiration for an interactive story.

Return structured JSON with:
- setting
- mood
- main_objects
- story_seed
"""

FIRST_CHAPTER_PROMPT = """
Create Chapter 1 of a 5-chapter interactive story.

Use:
- image analysis
- genre
- tone
- protagonist role

Return structured JSON with:
- title
- content
- 3 choices
"""

NEXT_CHAPTER_PROMPT = """
Continue the story based on the selected choice.

Return structured JSON with:
- title
- content
- 3 choices if chapter number is less than 5
- no choices if chapter number is 5
"""

FINALIZATION_PROMPT = """
Generate the final story package.

Return structured JSON with:
- character_profile
- world_description
- final_ending
"""
