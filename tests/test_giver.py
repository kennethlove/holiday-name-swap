from src.name_swap.models import Giver


def test_basic_giver(alice_data):
    assert Giver(**alice_data)


def test_giver_matched_with_exclusion(alice_data):
    giver_data = alice_data | {"gives_to": "Bob"}
    try:
        Giver(**giver_data)
    except ValueError as e:
        assert "gives_to must not be in exclusions" in str(e)


def test_giver_matched_with_self(alice_data):
    giver_data = alice_data | {"gives_to": "Alice"}
    try:
        Giver(**giver_data)
    except ValueError as e:
        assert "gives_to must not be the same as the player" in str(e)
