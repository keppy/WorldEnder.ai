import pytest
from worldender.models.world import World

def test_world_tick():
    world = World()
    world.tick()
    assert world.day == 1
    assert world.population != 8019876189
    assert world.epoch == "Apocalyptic"

def test_world_travel():
    world = World()
    world.travel("San Francisco")
    assert world.current_location == "San Francisco"