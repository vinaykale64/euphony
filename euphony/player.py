import os
import random
import pkg_resources
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from pygame import mixer


class player:
    """
    The player class creates an instance which can be used to play classical
    music while code runs in background. It's instance will be used as an
    argument to the `with` statement.

    Parameters
    ----------

    artist: str, Optional
        Choose among 'bach', 'beethoven' and 'mozart' to play specific music. If
        not specified, the code plays a random music file.

    Returns
    -------
    object : type player
        To be used as an argument for `with` statement to wrap code around

    Example
    -------

    .. code-block:: python

        from euphony import player
        random = player.player() # random music selector
        bach = player.player(artist='bach') # for bach music
        beethoven = player.player(artist='beethoven') # for beethoven music
        mozart = player.player(artist='mozart') # for mozart music

        # Works for any of the above 4
        with mozart:
            for i in range(1000000000):
                pass
        # Music plays till code completes and then stops.
        ...

    """
    def __init__(self, artist=None):
        self.artist = artist

    def __enter__(self):
        mixer.init()
        templates = os.listdir(
            pkg_resources.resource_filename(__name__, "music_templates")
        )
        if ".DS_Store" in templates:
            templates.remove(".DS_Store")

        if self.artist == "beethoven":
            templates = [template for template in templates if "beethoven" in template]
        elif self.artist == "bach":
            templates = [template for template in templates if "bach" in template]
        elif self.artist == "mozart":
            templates = [template for template in templates if "mozart" in template]
        else:
            pass

        song = random.choice(templates)
        path = "music_templates/" + song
        filepath = pkg_resources.resource_filename(__name__, path)
        mixer.music.load(filepath)
        mixer.music.play(loops=-1)

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
            # return False # uncomment to pass exception through

        mixer.music.stop()
        return True
