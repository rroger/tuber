#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import youtube_dl

# Define default download folder:
_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)),'music')

def init(download_folder):
    global _folder
    _folder = download_folder

# Bob Marley -- Get up, stand up .. stand up for your rights..

# if len(sys.argv) <= 1:
#   yt_urls = ["https://www.youtube.com/watch?v=X2W3aG8uizA"]
# else:
#   yt_urls = sys.argv[1:]
# yt_videos = []


def get_yt_video(yt_url):
  """Download a youtube video and convert it to mp3"""

  global _folder
  ydl_opts = {
      'format': 'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
      }],
      'outtmpl': os.path.join(_folder,'%(id)s.%(ext)s')
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

    # # get all videos
    # for yt_url in yt_urls:
    #   yt_videos.append(get_yt_video(yt_url))
