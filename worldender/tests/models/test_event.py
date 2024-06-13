import pytest
from worldender.models.event import Event
from worldender.models.choice import Choice

def test_event():
    choice = Choice(
        choice="run",
        consequence="You run away from the event"
    )
    event = Event(description='An event has occurred.', country='USA', city='New York', possible_choices=[choice])
    assert event.description == 'An event has occurred.'
    assert event.country == 'USA'
    assert event.city == 'New York'
    assert event.possible_choices == [choice]
