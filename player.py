#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time
import signal
from abc import ABCMeta
from subprocess import Popen


_status = 'idle'


class Player(metaclass=ABCMeta):

    def play(self, song_path, kill_after=0):
        global _status
        if _status == 'idle':
            try:
                _status = 'playing'

                player = Popen([self._get_external_player_name, song_path],
                                preexec_fn=os.setsid)

                if kill_after > 0:
                    time.sleep(kill_after)
                    os.killpg(player.pid, signal.SIGTERM)
                else:
                    player.wait()
            except Exception as e:
                print(e)
                _status = 'idle'
            finally:
                _status = 'idle'
        else:
            print('There is already a song playing. Please try later.')

    @abstractmethod
    def _get_external_player_name(self):
        pass


class RaspPlayer(Player):
    def _get_external_player_name(self):
        return 'afplay'


class MacPlayer(Player):
    def _get_external_player_name(self):
        return 'omxplayer'


if __name__ == '__main__':
    _folder = os.path.dirname(os.path.abspath(__file__))
    play(os.path.join(_folder,'music/X2W3aG8uizA.mp3'), kill_after=10)
