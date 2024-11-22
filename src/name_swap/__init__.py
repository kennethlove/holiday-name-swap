import json
from src.name_swap.models import Giver


def get_givers(json_blob: str) -> list[Giver]:
    """Convert a JSON blob into a list of players."""
    givers = json.loads(json_blob)
    return [Giver(**giver_data) for giver_data in givers]


def pair_givers(givers: list[Giver]) -> list[Giver]:
    """Find matches for a list of givers."""
    matches = []
    for giver in givers:
        givee = find_match(giver, givers)
        print(f"Matched {giver.name} with {givee.name}")

        giver.gives_to = givee.name
        givee.exclusions.append(giver.name)
        givee.drawn = True

        matches.append(giver)

    return matches


def find_match(giver: Giver, receivers: list[Giver]) -> Giver:
    """Given a giver and a list of receivers, find a match for the giver."""
    for receiver in receivers:
        print(f"Checking {giver.name} against {receiver.name}")
        try:
            giver = Giver(**giver.model_dump() | {"gives_to": receiver.name})
        except ValueError as e:
            print(e)
        else:
            givee = Giver(**receiver.model_dump() | {"drawn": True, "exclusions": receiver.exclusions + [giver.name]})
            receivers[receivers.index(receiver)] = givee
            return receiver