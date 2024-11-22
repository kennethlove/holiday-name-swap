import json
import random
from typing import List

from src.name_swap.models import Giver


def get_givers(json_blob: str) -> list[Giver]:
    """Convert a JSON blob into a list of players."""
    givers = json.loads(json_blob)
    return [Giver(**giver_data) for giver_data in givers]


def pair_givers(givers: list[Giver]) -> list[Giver]:
    """Find matches for a list of givers."""
    matches = []
    for giver in givers:
        giver = find_match(giver, givers)
        matches.append(giver)
    return matches


def find_match(giver: Giver, receivers: list[Giver]) -> Giver:
    """Given a giver and a list of receivers, find a match for the giver."""
    while available_receivers := [r for r in receivers if not r.drawn]:
        receiver = random.choice(available_receivers)
        try:
            receiver.drawn = True
            matched_giver = Giver(**giver.model_dump() | {"gives_to": receiver.name})
        except ValueError:
            receivers.remove(receiver)
            continue
        else:
            return matched_giver
    raise ValueError("No match found")