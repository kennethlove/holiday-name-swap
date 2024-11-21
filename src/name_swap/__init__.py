import json
import random

from src.name_swap.models import Player


def get_players(json_blob: str) -> list[Player]:
    """Convert a JSON blob into a list of players."""
    players = json.loads(json_blob)
    return [Player(**player_data) for player_data in players]


def find_matches(players: list[Player]) -> list[Player]:
    """Find matches for a list of players."""
    available_players = [player for player in players if not player.drawn]
    matches = []
    while available_players:
        random.shuffle(available_players)
        lucky_player = available_players.pop(0)
        matches.append(find_match(lucky_player, available_players))
    return matches


def find_match(player: Player, players: list[Player]) -> Player:
    """Given a player and a list of players, find a match for the player."""
    while players:
        other_player = random.choice(players)
        players.remove(other_player)
        try:
            matched_player = Player(**player.model_dump() | {"gives_to": other_player.name, "drawn": True})
        except ValueError:
            continue
        else:
            return matched_player
    raise ValueError("No match found")