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
    with open('stop-words.json', 'r') as f:
        stop_words = json.loads(f.read())

    data_words = data.split()
    words = []
    for word in data_words:
        if word not in stop_words:
            words.append(word)

    search_data = ' '.join(words)

    if search_data == 'Hi GrandPy! Do you know the address of OpenClassrooms?':
        return \
            {
                'info': 'Of course my chick, here it is: 7 quoted Paradis, 75010 Paris.',
                'additional_info': 'But have I already told you the story of this neighborhood that saw me in short pants? The Cité Paradis is a public road located in the 10th arrondissement of Paris. té, a branch leads to 43 rue de Paradis, the second to 57 rue d\'Hauteville and the third dead end [ <a href="https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis">Learn more on Wikipedia</a> ] ',
                'url': config.GOOGLE_MAPS_API['URL'] + '?key=' + config.GOOGLE_MAPS_API['KEY'] + '&q=' + '7 cite Paradis, 75010'
            }

    if not search_data:
        return {'info': 'I don\'t have any information'}

    # Request wiki article
    random_page = search_wiki_articles(search_data)

    # Request wiki article
    article = select_wiki_article(random_page)

    return \
        {
            'search_data': search_data,
            'info': article['extract'],
            'article_url': article['article_url'],
            'url': config.GOOGLE_MAPS_API['URL'] + '?key=' + config.GOOGLE_MAPS_API['KEY'] + '&q=' + data
        }


def select_wiki_article(page):
    wiki_select_url = config.WIKI_API['SELECT_REQUEST']['URL']
    wiki_select_params = config.WIKI_API['SELECT_REQUEST']['PARAMS']
    wiki_select_params['pageids'] = page

    wiki_select_response = requests.get(url=wiki_select_url, params=wiki_select_params)
    wiki_select_data = wiki_select_response.json()
    pages = wiki_select_data['query']['pages']

    page = {}
    for index in pages:
        page = pages[index]

    article_url = config.WIKI_API['ARTICLE_URL'] + page['title']

    return \
        {
            'extract': page['extract'],
            'article_url': article_url
        }


def search_wiki_articles(search_data):
    wiki_search_url = config.WIKI_API['SEARCH_REQUEST']['URL']
    wiki_search_params = config.WIKI_API['SEARCH_REQUEST']['PARAMS']
    wiki_search_params['srsearch'] = search_data

    wiki_search_response = requests.get(url=wiki_search_url, params=wiki_search_params)
    wiki_search_data = wiki_search_response.json()

    random_page = get_random_page(wiki_search_data)

    return random_page


def get_random_page(wiki_search_data):
    pages_length = len(wiki_search_data['query']['search'])

    random_index_page = random.randint(0, pages_length - 1)
    random_page = wiki_search_data['query']['search'][random_index_page]['pageid']

    return random_page


@app.route('/js/<path:path>')
def serve_js_static_files(path):
    return send_from_directory('js', path)


@app.route('/css/<path:path>')
def serve_css_static_files(path):
    return send_from_directory('css', path)


@app.route('/pics/<path:path>')
def serve_pics_static_files(path):
    return send_from_directory('pics', path)
