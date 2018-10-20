from flask import Flask, request, Blueprint, render_template, send_from_directory, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from helper import clear_dir, validate_str
from video_converter import convert
app = Flask(__name__)

from pytube import YouTube
import os

# for accessing the directories and working with them
current_directory_list = os.listdir(os.getcwd())
current_directory = os.getcwd()

# limiting the number of request that can be sent to the server in a day
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


@app.route("/", methods=['GET'])
def index():
    ''' index page is returned '''
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
        return convert(youtube_url, current_directory)
    else:
        return render_template("404.html", link=youtube_url)

if __name__ == "__main__":
    app.run()
