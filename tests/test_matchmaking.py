import json

import pytest

from src.name_swap import get_players, find_matches, find_match
from src.name_swap.models import Player


def test_convert_to_players(alice_data, bob_data, charlie_data):
    players = get_players(json.dumps([alice_data, bob_data, charlie_data]))
    assert len(players) == 3
    assert all(isinstance(player, Player) for player in players)
    assert players[0].name == "Alice"


def test_convert_to_players_bad_data(alice_data, bob_data):
    alice_data["gives_to"] = "Bob"

    with pytest.raises(ValueError):
        get_players(json.dumps([alice_data, bob_data]))


def test_find_match(alice_data, charlie_data):
    alice = Player(**alice_data)
    charlie = Player(**charlie_data)

    alice = find_match(alice, [charlie])
    assert alice.gives_to == charlie.name


def test_find_match_same(alice_data):
    matches = [Player(**alice_data), Player(**alice_data)]
    with pytest.raises(ValueError):
        find_match(matches[0], matches[1:])


def test_find_matches(alice_data, charlie_data):
    matches = list(
        find_matches(
            [Player(**alice_data), Player(**charlie_data)]
        )
    )
    assert len([m for m in matches if bool(m)]) == 2


