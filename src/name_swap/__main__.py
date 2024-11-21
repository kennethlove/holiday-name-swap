from pydantic import (
    BaseModel,
    ValidationInfo,
    field_validator
)


class Player(BaseModel):
    name: str
    drawn: bool = False
    exclusions: list[str] = []
    gives_to: str | None = None

    @field_validator("gives_to")
    @classmethod
    def check_gives_to(cls, v: str, info: ValidationInfo):
        if v in info.data["exclusions"]:
            raise ValueError("gives_to must not be in exclusions")
        return v


alice_data = {
    "name": "Alice",
    "drawn": False,
    "exclusions": ["Bob"],
    "gives_to": None
}
bob_data = {
    "name": "Bob",
    "drawn": False,
    "exclusions": [],
    "gives_to": None
}
charlie_data = {
    "name": "Charlie",
    "drawn": False,
    "exclusions": [],
    "gives_to": None
}

alice = Player(**alice_data)
bob = Player(**bob_data)
charlie = Player(**charlie_data)

print(alice, bob, charlie)

alice_data2 = alice_data | {"gives_to": "Bob"}
Player(**alice_data2)