#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import player
import sqlite3
import cherrypy
 

class TubeServer(object):
    def __init__(self):
        if sys.platform.startswith('darwin'): # On Macosx
            self._player = player.MacPlayer()
        else: # On Rasparian
            self._player = player.RaspPlayer()

    def index(self):
        return "Hello World!"
    index.exposed = True

if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    cherrypy.quickstart(TubeServer())
