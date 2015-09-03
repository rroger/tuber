#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Standup Module to Play a song


Setup:
Install python-pip, pyglet python library and avbin library.
on Ubuntu:
sudo apt-get install pyhton python-pip
sudo pip install pyglet
sudo apt-get install libavbin-dev libavbin0
sudo pip install --upgrade youtube_dl
sudo apt-get install libavcodec-extra-53

"""

import pyglet
import youtube_dl
import sys

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
          'preferredcodec': 'mp3',
          'preferredquality': '192',
      }],
      'outtmpl': '/home/rruettimann/workspace/tuber/music/%(id)s.%(ext)s'
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
music = pyglet.resource.media('/home/rruettimann/workspace/tuber/music/'+ yt_videos[0]['display_id'] + '.mp3')
music.play()
print('Start Pyglet App')
print('/home/rruettimann/workspace/tuber/music/'+ yt_videos[0]['display_id'] + '.mp3')
pyglet.app.run()
