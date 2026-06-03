import json
import re
from typing import TypeVar

from pydantic import BaseModel


T = TypeVar("T", bound=BaseModel)


def extract_json(text: str) -> str:
    if not text or not text.strip():
        raise ValueError("AI response was empty.")

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        preview = text[:500]
        raise ValueError(
            f"No JSON object found in AI response. Preview: {preview}")

    return match.group(0)


def parse_ai_json(text: str, model_class: type[T]) -> T:
    json_text = extract_json(text)
    data = json.loads(json_text)
    return model_class.model_validate(data)
