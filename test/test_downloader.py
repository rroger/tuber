import os
import sys
import shutil
import unittest
sys.path.append('..')
import tuber.downloader as downloader

_test_folder = os.path.dirname(os.path.abspath(__file__))

class TestGetYtVideo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global _test_folder
        cls._music_folder = os.path.join(_test_folder, 'music')
        if os.path.exists(cls._music_folder):
            shutil.rmtree(cls._music_folder)
        os.mkdir(cls._music_folder)
        downloader.init(cls._music_folder)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls._music_folder):
            shutil.rmtree(cls._music_folder)

    def testGetYtVideo(self):
        video = downloader.get_yt_video(
            'https://www.youtube.com/watch?v=wycjnCCgUes')
        self.assertTrue(
            os.path.isfile(
                os.path.join(self._music_folder,video['display_id'] + '.mp3')))

if __name__ == "__main__":
     unittest.main()
