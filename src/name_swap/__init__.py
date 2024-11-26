import random
from copy import deepcopy

from src.name_swap.models import Giver


def pair_givers(givers: list[Giver]) -> list[Giver]:
    """Find matches for a list of givers."""
    all_givers = {giver.name: giver for giver in givers}

    for key, giver in all_givers.items():
        possible_receivers = deepcopy(givers)
        possible_receivers.remove(giver)
        random.shuffle(possible_receivers)

        for receiver in possible_receivers:
            if any([
                receiver.name in giver.exclusions,
                giver.name == receiver.name,
                receiver.gives_to == giver.name,
                receiver.drawn == True,
            ]):
                continue
            else:
                all_givers[key].gives_to = receiver.name
                all_givers[receiver.name].exclusions.append(key)
                all_givers[receiver.name].drawn = True
                break

    return list(all_givers.values())
