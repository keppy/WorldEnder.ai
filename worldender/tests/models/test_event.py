import pytest
from worldender.models.event import Event
from worldender.models.outcome import Outcome

def test_event():
    old_outcome = Outcome(description='The world ends.', consequence='The world ends.', choices=['The world ends.', 'The world ends.', 'The world ends.'], outcomes=[])
    outcome = Outcome(description='The world ends.', consequence='The world ends.', choices=['The world ends.', 'The world ends.', 'The world ends.'], outcomes=[old_outcome])
    event = Event(description='An event has occurred.', country='USA', city='New York', possible_outcomes=[outcome])
    assert event.description == 'An event has occurred.'
    assert event.country == 'USA'
    assert event.city == 'New York'
    assert event.possible_outcomes == [outcome]
