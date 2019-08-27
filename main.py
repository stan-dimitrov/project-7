import random

from flask import Flask, send_from_directory, request, json
import config
import requests

app = Flask(__name__)


@app.route('/home')
def home():
    file = open("home.html", "r")
    file_content = file.read()

    return file_content


@app.route('/get-search-info')
def get_search_info():
    data = request.args.get('data')

    # Request wiki article
    wiki_search_url = config.WIKI_API['SEARCH_REQUEST']['URL']
    wiki_search_params = config.WIKI_API['SEARCH_REQUEST']['PARAMS']
    wiki_search_params['srsearch'] = data

    wiki_search_response = requests.get(url=wiki_search_url, params=wiki_search_params)
    wiki_search_data = wiki_search_response.json()

    pages_length = len(wiki_search_data['query']['search'])

    random_index_page = random.randint(0, pages_length - 1)
    random_page = wiki_search_data['query']['search'][random_index_page]['pageid']

    # Request wiki article
    wiki_select_url = config.WIKI_API['SELECT_REQUEST']['URL']
    wiki_select_params = config.WIKI_API['SELECT_REQUEST']['PARAMS']
    wiki_select_params['pageids'] = random_page

    wiki_select_response = requests.get(url=wiki_select_url, params=wiki_select_params)
    wiki_select_data = wiki_select_response.json()
    pages = wiki_select_data['query']['pages']

    page = {}
    for index in pages:
        page = pages[index]

    return \
        {
            'info': page['extract'],
            'url': config.GOOGLE_MAPS_API['URL'] + '?key=' + config.GOOGLE_MAPS_API['KEY'] + '&q=' + data
        }


@app.route('/js/<path:path>')
def serve_js_static_files(path):
    return send_from_directory('js', path)


@app.route('/css/<path:path>')
def serve_css_static_files(path):
    return send_from_directory('css', path)