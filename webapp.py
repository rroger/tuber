#!/usr/bin/python
# -*- coding: utf-8 -*-
import cherrypy


class Tuber(object):
    def index(self):
        return "Hello World!"
    index.exposed = True

if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    cherrypy.quickstart(Tuber())
