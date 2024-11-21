import pytest


@pytest.fixture()
def alice_data():
    return {
        "name": "Alice",
        "drawn": False,
        "exclusions": ["Bob"],
        "gives_to": None
    }


@pytest.fixture()
def bob_data():
    return {
        "name": "Bob",
        "drawn": False,
        "exclusions": [],
        "gives_to": None
    }


@pytest.fixture()
def charlie_data():
    return {
        "name": "Charlie",
        "drawn": False,
        "exclusions": [],
        "gives_to": None
    }

