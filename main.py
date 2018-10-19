from flask import Flask, request, Blueprint, render_template, send_from_directory, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)

from pytube import YouTube
import os
import time

current_directory_list = os.listdir(os.getcwd())
current_directory = os.getcwd()

# limiting the number of request that can be sent to the server in a day
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


def clear_dir(current_directory, current_directory_list):
    for item in current_directory_list:
        if item.endswith(".mp4"):
            os.remove(os.path.join(current_directory, item))


def validate_str(str, val_str):
    if val_str in str:
        return True


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/actor", methods=['POST'])
def actor():
    ''' returns an mp4 file'''

    # deletes mp4s in current directory
    clear_dir(current_directory, current_directory_list)

    # validates string
    validate_string = "youtube.com/watch?v="
    youtube_url = str(request.form['youtube_url'])

    val_string = validate_str(youtube_url, validate_string)

    if(val_string == True):
        # downloads video
        yt = YouTube(youtube_url)
        yt.streams.first().download()
        new_filename = yt.streams.first().default_filename
        return send_from_directory(current_directory, new_filename, as_attachment=True)
    else:
        return render_template("404.html", link=youtube_url)


if __name__ == "__main__":
    app.run()
