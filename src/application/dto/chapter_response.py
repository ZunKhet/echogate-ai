from pydantic import BaseModel, Field


class ChoiceResponse(BaseModel):
    id: str
    text: str


class ChapterResponse(BaseModel):
    title: str
    summary: str
    content: str
    choices: list[ChoiceResponse] = Field(default_factory=list)
