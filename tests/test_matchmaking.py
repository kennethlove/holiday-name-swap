import pytest

from src.name_swap import pair_givers
from src.name_swap.models import Giver


def test_find_match(alice_data, charlie_data):
    alice, charlie = pair_givers([Giver(**alice_data), Giver(**charlie_data)])
    assert alice.gives_to == charlie.name
    assert charlie.gives_to == alice.name


def test_find_match_same(alice_data):
    matches = [Giver(**alice_data), Giver(**alice_data)]
    with pytest.raises(ValueError):
        print(pair_givers(matches))


def test_find_matches(alice_data, charlie_data):
    matches = list(
        pair_givers(
            [Giver(**alice_data), Giver(**charlie_data)]
        )
    )
    assert len([m for m in matches if bool(m)]) == 2


