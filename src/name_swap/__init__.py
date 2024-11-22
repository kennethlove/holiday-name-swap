import random

from src.name_swap.models import Giver


def pair_givers(givers: list[Giver]) -> list[Giver]:
    """Find matches for a list of givers."""
    matches = []
    for giver in givers:
        potential_matches = [givee for givee in givers
                             if givee.name not in giver.exclusions and
                             givee != giver and
                             not givee.drawn]
        if potential_matches:
            givee = random.choice(potential_matches)
            matches.append(Giver(**giver.model_dump() | {"gives_to": givee.name}))
    if not matches:
        raise ValueError("No matches found")
    return matches
