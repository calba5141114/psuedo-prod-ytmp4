from flask import Flask, request, Blueprint, render_template, send_from_directory, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from helper import clear_dir, validate_str
from video_converter import convert
from pytube import YouTube
import os

app = Flask(__name__)

# for accessing the directories and working with them
current_directory = os.getcwd()
current_directory_list = os.listdir(current_directory)
downloads = current_directory + '/downloads'
downloads_list = os.listdir(downloads)

# limiting the number of request that can be sent to the server in a day
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


@app.route("/", methods=['GET'])
@limiter.exempt
def index():
    ''' index page is returned '''
    clear_dir(downloads, downloads_list)
    return render_template("index.html")


@app.route("/actor", methods=['POST'])
@limiter.limit("50/hour")
def actor():
    ''' returns an mp4 file'''

    val_str = "youtube.com/watch?v="
    youtube_url = str(request.form['youtube_url'])
    val_str_res = validate_str(youtube_url, val_str)

    try:
        if(val_str_res == True):
            clear_dir(downloads, downloads_list)
            return convert(youtube_url, downloads, downloads_list)
    except:
        clear_dir(downloads, downloads_list)
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
