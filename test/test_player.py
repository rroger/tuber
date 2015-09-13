import os
import sys
import shutil
import unittest
sys.path.append('..')
import tuber.player as player

_test_folder = os.path.dirname(os.path.abspath(__file__))

class TestPlayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global _test_folder
        cls._music_folder = os.path.join(_test_folder, 'music')
        if sys.platform.startswith('darwin'): # On Macosx
            cls._player = player.MacPlayer()
        else: # On Rasparian
            cls._player = player.RaspPlayer()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_play(self):
        # How is it possible to check if external player is called?
        pass
#s        self.player.play(os.path.join(_test_folder, 'fixtures/wycjnCCgUes.mp3')


if __name__ == "__main__":
     unittest.main()
