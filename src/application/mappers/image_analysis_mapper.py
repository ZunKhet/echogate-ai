from src.application.dto.image_analysis_response import (
    ImageAnalysisResponse,
)
from src.domain.entities.image_analysis import ImageAnalysis


class ImageAnalysisMapper:
    @staticmethod
    def to_domain(
        dto: ImageAnalysisResponse,
    ) -> ImageAnalysis:
        return ImageAnalysis(
            setting=dto.setting,
            mood=dto.mood,
            main_objects=dto.main_objects,
            story_seed=dto.story_seed,
            magical_elements=dto.magical_elements,
            possible_conflict=dto.possible_conflict,
        )
