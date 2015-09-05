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
import pygame
import youtube_dl
from subprocess import call


project_dir_path = os.path.dirname(os.path.abspath(__file__))
print(project_dir_path)

# Bob Marley -- Get up, stand up .. stand up for your rights..

if len(sys.argv) <= 1:
  yt_urls = ["https://www.youtube.com/watch?v=X2W3aG8uizA"]
else:
  yt_urls = sys.argv[1:]
yt_videos = []

def get_yt_video(yt_url):
  """Download a youtube video and convert it to mp3"""

  ydl_opts = {
      'format': 'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'wav',
          'preferredquality': '192',
      }],
      'outtmpl': 'music/%(id)s.%(ext)s'
  }
  ydl = youtube_dl.YoutubeDL(ydl_opts)

  with ydl:
      result = ydl.extract_info(
          #'http://www.youtube.com/watch?v=BaW_jenozKc',
          yt_url,
          download=True # We just want to extract the info
      )

  if 'entries' in result:
      # Can be a playlist or a list of videos
      video = result['entries'][0]
  else:
      # Just a video
      video = result

  return video

## Debug video object:
#for key in video:
#  print("key: %s value: %s" % (key,video[key]))

# get all videos
for yt_url in yt_urls:
  yt_videos.append(get_yt_video(yt_url))

# play first one
#music = pyglet.resource.media('music/'+ yt_videos[0]['display_id'] + '.wav')
#music.play()
print('Start Pyglet App')
print('music/'+ yt_videos[0]['display_id'] + '.wav')
#pyglet.app.run()
# Create our Music Player.

if sys.platform.startswith("darwin"): # On Macosx
    pygame.mixer.init()

    pygame.mixer.music.load('music/'+ yt_videos[0]['display_id'] + '.wav')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    time.sleep(90)
else: # On Rasparian
    call(["omxplayer", "-o local %s" % ('music/'+ yt_videos[0]['display_id'] + '.wav')])
