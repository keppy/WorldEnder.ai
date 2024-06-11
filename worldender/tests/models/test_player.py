import pytest
from worldender.models.player import DEFAULT_CONFIG, Player

def test_player():
    player = Player()

    assert player.name == DEFAULT_CONFIG['name']
    assert player.city == DEFAULT_CONFIG['city']
    assert player.sanity == DEFAULT_CONFIG['sanity']
    assert player.item == DEFAULT_CONFIG['item']
    assert player.ailment == DEFAULT_CONFIG['ailment']
    assert player.hp == DEFAULT_CONFIG['hp']
    assert player.sanity == DEFAULT_CONFIG['sanity']
    assert isinstance(player, Player)
    table = player.status_table()
    assert isinstance(table, str)
