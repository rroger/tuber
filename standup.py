#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Standup Module to Play a song


Setup:

on Ubuntu:
sudo apt-get install pyhton3 python3-pip
sudo pip install pyglet
sudo apt-get install libavbin-dev libavbin0
sudo pip install --upgrade youtube_dl
sudo apt-get install libavcodec-extra-53

On MacOsX:
brew install python3
sudo pip3 install --upgrade youtube_dl
brew install libav

Go to:
http://avbin.github.io/AVbin/Download.html
And install Binaries

PyGame
Current Instructions

Create and add the following to ~/.bash_profile:
     # Homebrew binaries now take precedence over Apple defaults
     export PATH=/usr/local/bin:$PATH

Install Apple Xcode command line tools:
xcode-select --install

Install homebrew:
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

Install Python3 "proper" and packages we’ll need for installing PyGame from bitbucket:
brew install python3 hg sdl sdl_image sdl_mixer sdl_ttf portmidi

Install PyGame:
pip3 install hg+http://bitbucket.org/pygame/pygame

Restart the Mac for XQuartz changes


"""
import os
#import pyglet
import sys
import time
import youtube_dl
