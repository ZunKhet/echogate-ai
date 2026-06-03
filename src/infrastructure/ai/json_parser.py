import json
import re
from typing import TypeVar

from pydantic import BaseModel


T = TypeVar("T", bound=BaseModel)


def extract_json(text: str) -> str:
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON object found in AI response.")

    return match.group(0)


def parse_ai_json(text: str, model_class: type[T]) -> T:
    json_text = extract_json(text)
    data = json.loads(json_text)
    return model_class.model_validate(data)
