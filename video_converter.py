from flask import send_from_directory
from pytube import YouTube


def convert(youtube_url, current_directory):
    yt = YouTube(youtube_url)
    yt.streams.first().download()
    new_filename = yt.streams.first().default_filename
    return send_from_directory(current_directory, new_filename, as_attachment=True)
