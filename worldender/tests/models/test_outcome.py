import pytest
from worldender.models.outcome import Outcome

def test_outcome():
    outcome = Outcome(description="The world ended")
    assert outcome.description == "The world ended"

