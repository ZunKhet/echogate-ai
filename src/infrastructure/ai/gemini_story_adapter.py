from src.application.ports.ai_story_port import AIStoryPort
from src.domain.entities.chapter import Chapter
from src.domain.entities.image_analysis import ImageAnalysis
from src.domain.entities.story import Story


class GeminiStoryAdapter(AIStoryPort):
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def analyze_image(self, image_bytes: bytes) -> ImageAnalysis:
        raise NotImplementedError(
            "Gemini image analysis is not implemented yet.")

    def generate_first_chapter(self, story: Story) -> Chapter:
        raise NotImplementedError(
            "Gemini first chapter generation is not implemented yet.")

    def generate_next_chapter(self, story: Story, selected_choice_id: str) -> Chapter:
        raise NotImplementedError(
            "Gemini next chapter generation is not implemented yet.")

    def finalize_story(self, story: Story) -> Story:
        raise NotImplementedError(
            "Gemini finalization is not implemented yet.")
