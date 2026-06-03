from pydantic import BaseModel


class ChoiceResponse(BaseModel):
    id: str
    text: str


class ChapterResponse(BaseModel):
    title: str
    summary: str
    content: str
    choices: list[ChoiceResponse]
