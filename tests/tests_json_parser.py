import pytest

from src.application.dto.image_analysis_response import ImageAnalysisResponse
from src.infrastructure.ai.json_parser import parse_ai_json


def test_parse_ai_json() -> None:
    raw_text = """
    Here is the result:

    {
      "setting": "Ancient forest",
      "mood": "Mysterious",
      "main_objects": ["gate"],
      "story_seed": "A gate awakens.",
      "magical_elements": ["portal"],
      "possible_conflict": "A memory must be sacrificed.",
      "suggested_title": "The Whispering Gate"
    }
    """

    result = parse_ai_json(raw_text, ImageAnalysisResponse)

    assert result.setting == "Ancient forest"
    assert result.mood == "Mysterious"


def test_parse_ai_json_raises_error_when_no_json() -> None:
    with pytest.raises(ValueError, match="No JSON object found"):
        parse_ai_json("No structured response here.", ImageAnalysisResponse)
