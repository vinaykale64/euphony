import pytest
from euphony.player import Player

class TestPlayer:

    def test_standard_case(self):
        artist = Player()
        with artist:
            for i in range(10000000):
                pass

    def test_incorrect_artist(self):
        artist = Player(artist='abc')
        with pytest.raises(KeyError):
            with artist:
                for i in range(10000000):
                    pass

