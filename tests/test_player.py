import pytest
from euphony.player import Player


class TestPlayer:

    def test_standard_case(self):
        artist = Player()
        with artist:
            for i in range(10000000):
                pass

    def test_artist_options_mozart(self):
        artist = Player(artist='mozart')
        with artist:
            for i in range(10000000):
                pass

    def test_artist_options_bach(self):
        artist = Player(artist='bach')
        with artist:
            for i in range(10000000):
                pass

    def test_artist_options_beethoven(self):
        artist = Player(artist='beethoven')
        with artist:
            for i in range(10000000):
                pass

    def test_incorrect_artist(self):
        artist = Player(artist='abc')
        with pytest.raises(KeyError):
            with artist:
                for i in range(10000000):
                    pass
