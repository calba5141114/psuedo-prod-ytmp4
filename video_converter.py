from flask import send_from_directory
from pytube import YouTube
from helper import clear_dir


def convert(youtube_url, download_directory, downloads_list):
    ''' converts youtbe video and ques download '''
    clear_dir(download_directory, downloads_list)
    yt = YouTube(youtube_url)
    yt.streams.first().download(download_directory)
    new_filename = yt.streams.first().default_filename
    return send_from_directory(download_directory, new_filename, as_attachment=True)
