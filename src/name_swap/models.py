from pydantic import (
    BaseModel,
    ValidationInfo,
    field_validator, Field
)


class Giver(BaseModel):
    name: str
    drawn: bool = False
    exclusions: list[str] = Field(default_factory=list)
    gives_to: str | None = None

    @field_validator("gives_to")
    @classmethod
    def check_gives_to_others(cls, v: str, info: ValidationInfo):
        if v in info.data.get("exclusions", []):
            raise ValueError("gives_to must not be in exclusions")
        return v

    @field_validator("gives_to")
    @classmethod
    def check_gives_to_self(cls, v: str, info: ValidationInfo):
        if v == info.data.get("name", ""):
            raise ValueError("gives_to must not be the same as the giver")
        return v
