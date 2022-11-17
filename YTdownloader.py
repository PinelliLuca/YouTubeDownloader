from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Do you want Video or music of this file?")
print("If you want video press v, if you want audio press a")

if input() == "v":
    print("VIDEO")
    ydvideo = yt.streams.get_highest_resolution()
    ydvideo.download('C:/Users/lpine/PycharmProjects/YouTubeDownloader/Video downloaded')
elif input() == "a":
    print("AUDIO")
    ytaudio = yt.streams.get_audio_only()
    ytaudio.download('C:/Users/lpine/PycharmProjects/YouTubeDownloader/Audio downloaded')
