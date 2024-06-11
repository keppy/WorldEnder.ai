import pytest
from worldender.models.outcome import Outcome

def test_outcome():
    previous_outcome = Outcome(description="The world ended", consequence="Everyone died", choices=["A", "B", "C"], outcomes=[])
    outcome = Outcome(description="The world ended", consequence="Everyone died", choices=["A", "B", "C"], outcomes=[previous_outcome])
    assert outcome.description == "The world ended"
    assert outcome.consequence == "Everyone died"
    assert outcome.choices == ["A", "B", "C"]
    assert outcome.outcomes == [previous_outcome]
    assert outcome == outcome
    assert outcome != previous_outcome
