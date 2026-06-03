from src.application.ports.ai_story_port import AIStoryPort
from src.domain.entities.chapter import Chapter
from src.domain.entities.choice import Choice
from src.domain.entities.image_analysis import ImageAnalysis
from src.domain.entities.story import Story


class FakeStoryAdapter(AIStoryPort):
    def analyze_image(self, image_bytes: bytes) -> ImageAnalysis:
        return ImageAnalysis(
            setting="an ancient gate hidden in a misty forest",
            mood="mysterious",
            main_objects=["gate", "mist", "forest"],
            story_seed="A forgotten gate awakens when touched by moonlight.",
        )

    def generate_first_chapter(self, story: Story) -> Chapter:
        return Chapter(
            number=1,
            title="The First Echo",
            content=(
                "The forest had been silent for one hundred years, "
                "until the gate began to whisper again..."
            ),
            choices=[
                Choice(id="1", text="Step through the glowing gate"),
                Choice(id="2", text="Follow the whispering path"),
                Choice(id="3", text="Touch the ancient symbol"),
            ],
        )

    def generate_next_chapter(self, story: Story, selected_choice_id: str) -> Chapter:
        chapter_number = len(story.chapters) + 1

        return Chapter(
            number=chapter_number,
            title=f"Echo {chapter_number}",
            content=(
                f"The choice marked as {selected_choice_id} changed the path. "
                "The world beyond the gate shifted, revealing a deeper mystery..."
            ),
            choices=[
                Choice(id="1", text="Trust the hidden voice"),
                Choice(id="2", text="Search for the lost map"),
                Choice(id="3", text="Enter the silver tower"),
            ]
            if chapter_number < 5
            else [],
        )

    def finalize_story(self, story: Story) -> Story:
        story.character_profile = "A brave traveler drawn toward forgotten worlds."
        story.world_description = "A realm of gates, echoes, mist, and ancient magic."
        story.final_ending = "The gate closed softly, but one final echo remained."
        story.is_complete = True
        return story
