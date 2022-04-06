import time
import youtube_search
import yt_dlp
import os
import datetime
import pygame

def download_song(song_url):
    """
    Download a song using youtube url and song title
    """

    outtmpl = "song" + '.%(ext)s'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'postprocessors': [
            {'key': 'FFmpegExtractAudio','preferredcodec': 'mp3',
             'preferredquality': '192',
            },
            {'key': 'FFmpegMetadata'},
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(song_url, download=True)

def setupAlarm():
    print(datetime.datetime.now().strftime("%H:%M"))
    endTime = input("Select what time to set alarm to in 24 hour time format(military time. HH:MM)")
    song = input("What is the name of the song you want to use?")
    ytsearch = youtube_search.YoutubeSearch(song, 1)
    ytdict = ytsearch.to_dict()
    actualytdict = dict(ytdict[0])
    ytlink = "https://www.youtube.com{}".format(actualytdict['url_suffix'])
    download_song(ytlink)

def startAlarm(endTime):
    while True:
        Standard_time=datetime.datetime.now().strftime("%H:%M")
        # Put the program to sleep for a second
        time.sleep(1)
        if endTime==Standard_time:
            pygame.mixer.init
            pygame.mixer.music.load("song.mp3")
            pygame.mixer.music.play()

            




    


setupAlarm()
startAlarm()