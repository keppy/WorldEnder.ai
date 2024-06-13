import pytest
from worldender.models.choice import Choice

def test_choice():
    choice = Choice(
        choice="run",
        consequence="You run away from the event"
    )
    assert choice.choice == "run"
    assert choice.consequence == "You run away from the event"