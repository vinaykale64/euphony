import os
import pkg_resources

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from pygame import mixer

class player:
    def __init__(self):
        pass

    def __enter__(self):
        mixer.init()
        path = 'music_templates/sample.mp3'
        filepath = pkg_resources.resource_filename(__name__, path)
        mixer.music.load(filepath)
        mixer.music.play()

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
            # return False # uncomment to pass exception through

        mixer.music.stop()
        return True
