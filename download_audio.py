import os
from pytube import YouTube


def download_audio(video_url: str):
    """ Download audios of the highest quality to download_folder.
    """

    video_obj = YouTube(video_url)
    streams = video_obj.streams
    audio_best = streams.filter(only_audio=True).desc().first()
    # audio_best = streams.get_audio_only()
    file_name = audio_best.download("media_folder")
    print(file_name)
    mp3_name = file_name.replace(".webm", ".mp3")
    os.rename(file_name, mp3_name)

    return mp3_name


def get_video_name(video_url: str):
    try:
        return YouTube(video_url).title

    except Exception as exception:
        print("EXCEPTION OCCURRED: ", exception)
