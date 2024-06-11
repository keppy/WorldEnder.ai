import pytest
from worldender.models.world_ender import WorldEnder

def test_world_ender():
    world_ender = WorldEnder(kind='enderman', description='A tall, dark figure with glowing purple eyes.', death_toll="10000", survival_rate="0.1")
    assert world_ender.kind == 'enderman'
    assert world_ender.description == 'A tall, dark figure with glowing purple eyes.'
    assert world_ender.death_toll == '10000'
    assert world_ender.survival_rate == 0.1
