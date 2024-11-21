from src.name_swap.models import Player


def test_basic_player(alice_data):
    assert Player(**alice_data)


def test_player_matched_with_exclusion(alice_data):
    player_data = alice_data | {"gives_to": "Bob"}
    try:
        Player(**player_data)
    except ValueError as e:
        assert "gives_to must not be in exclusions" in str(e)


def test_player_matched_with_self(alice_data):
    player_data = alice_data | {"gives_to": "Alice"}
    try:
        Player(**player_data)
    except ValueError as e:
        assert "gives_to must not be the same as the player" in str(e)
