from Config.Util import *
from Config.Config import *
from pytube import YouTube
Title("Youtube Downloader")
video_url = input(f"{color.RED}\n{INPUT} Video URL -> {color.RESET}")
print(f"""
{color.WHITE}[{color.RED}01{color.WHITE}] {color.RED}->{color.WHITE} Audio Mp3
{color.WHITE}[{color.RED}02{color.WHITE}] {color.RED}->{color.WHITE} Video Mp4
""")
file_type = input(f"{color.RED}{INPUT} Format -> {color.RESET}")

path_destination_relative = "./1-File-Output/YoutubeDownloader"
path_destination = os.path.abspath(path_destination_relative)

try:
    yt = YouTube(video_url)
    if file_type in ['1', '01']:
        print(f"{color.RED}{INFO} Download...")
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path=path_destination)
        print(f"{color.RED}{INFO} Audio downloaded successfully. The mp3 file is located in the folder \"{color.WHITE}{path_destination}{color.RED}\"")
        try:
            directory = os.getcwd()
            print(f"{color.RED}{INFO} Open \"{color.WHITE}{path_destination}{color.RED}\"")
            path = directory + "/1-File-Create/YoutubeDownloader"
            path = os.path.realpath(path)
            os.startfile(path)
        except:
             ()
    elif file_type in ['2', '02']:
        print(f"{color.RED}{INFO} Download...")
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path=path_destination)
        print(f"{color.RED}{INFO} Video downloaded successfully. The mp3 file is located in the folder \"{color.WHITE}{path_destination}{color.RED}\"")
        try:
            directory = os.getcwd()
            print(f"{color.RED}{INFO} Open \"{color.WHITE}{path_destination}{color.RED}\"")
            path = directory + "/1-File-Create/YoutubeDownloader"
            path = os.path.realpath(path)
            os.startfile(path)
        except:
             ()
    else:
        ErrorChoice()
except:
    ErrorUrl()

Continue()
Reset()


