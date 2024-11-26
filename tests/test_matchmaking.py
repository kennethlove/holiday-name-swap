from src.name_swap import pair_givers
from src.name_swap.models import Giver


def test_find_match(alice_data, bob_data, charlie_data):
    alice = Giver(**alice_data)
    bob = Giver(**bob_data)
    charlie = Giver(**charlie_data)
    alice, bob, charlie = pair_givers([alice, bob, charlie])
    assert alice.gives_to == charlie.name
    assert bob.gives_to == alice.name
    assert charlie.gives_to == bob.name


def test_find_match_same(alice_data):
    matches = [Giver(**alice_data), Giver(**alice_data)]
    output = pair_givers(matches)
    assert [giver.gives_to is None for giver in output]

