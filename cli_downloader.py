import argparse
import sys
from pytube import YouTube
from moviepy.editor import *
import threading

def mp4_to_mp3(mp4, mp3):     
    mp4_without_frames = AudioFileClip(mp4)     
    mp4_without_frames.write_audiofile(mp3)     
    mp4_without_frames.close()

def showProgress(stream, data, bytes):
    print(bytes)

def downloadVideo(url):

    yt = YouTube(url=url, on_progress_callback=showProgress)
    video = yt.streams.filter(res="1080p")
    audio = yt.streams.filter(only_audio=True)

    if video:
        print("Video download started1")
        #video[0].download()
        print("Video download completed!\n")

        print("Audio download started1\n")
        audio[-1].download()
        print("Audio download completed!\n")

        mp4_to_mp3(f"{yt.title}.webm", f"mo.mp3")



    else:
        print("Quality not available")


def threadDownload(arguments):
    thread_func = threading.Thread(target=downloadVideo, args=arguments)
    thread_func.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", type=str)

    args = parser.parse_args()

    threadDownload((args.u,))


