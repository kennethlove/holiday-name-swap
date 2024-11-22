from typing import Union

from pydantic import (
    BaseModel,
    ValidationInfo,
    field_validator
)


class Giver(BaseModel):
    name: str
    drawn: bool = False
    exclusions: list[str] = []
    gives_to: str | None = None

    @field_validator("gives_to")
    @classmethod
    def check_gives_to_others(cls, v: str, info: ValidationInfo):
        if v in info.data["exclusions"]:
            raise ValueError("gives_to must not be in exclusions")
        return v

    @field_validator("gives_to")
    @classmethod
    def check_gives_to_self(cls, v: str, info: ValidationInfo):
        if v == info.data["name"]:
            raise ValueError("gives_to must not be the same as the giver")
        return v

    # @field_validator("gives_to")
    # @classmethod
    # def check_gives_to_drawn(cls, v: str, info: ValidationInfo):
    #     if info.data["drawn"]:
    #         raise ValueError("gives_to must not be an already drawn giver")
    #     return v
