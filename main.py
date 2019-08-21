from flask import Flask, send_from_directory
import random
import requests

app = Flask(__name__)

S = requests.Session()

@app.route('/home')
def home():
    file = open("home.html", "r")
    file_content = file.read()

    return file_content


@app.route('/get-random-wiki-article')
def get_random_wiki_article():
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnlimit": "5"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    return DATA

@app.route('/get-data')
def get_data():
    return str(random.randint(1, 100))


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
