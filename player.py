#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import signal
from subprocess import Popen

_status = 'idle'

def play(song, kill_after=0):
    global _status
    if _status == 'idle':
        try:
            _status = 'playing'
            if sys.platform.startswith('darwin'): # On Macosx
                player_name = 'afplay'
            else: # On Rasparian
                player_name = 'omxplayer'

            player = Popen([player_name, song], preexec_fn=os.setsid)

            if kill_after > 0:
                time.sleep(30)
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


if __name__ == '__main__':
    play('music/X2W3aG8uizA.mp3')
