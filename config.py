GOOGLE_MAPS_API = {
    'URL': 'https://www.google.com/maps/embed/v1/place',
    'KEY': 'keykey' 
}

WIKI_API = {
    'ARTICLE_URL': 'https://fr.wikipedia.org/wiki/',
    'SEARCH_REQUEST': {
        'URL': 'https://fr.wikipedia.org/w/api.php',
        'PARAMS': {
            'action': 'query',
            'format': 'json',
            'list': 'search'
        }
    },
    'SELECT_REQUEST': {
        'URL': 'https://fr.wikipedia.org/w/api.php',
        'PARAMS': {
            'action': 'query',
            'format': 'json',
            'prop': 'extracts',
            'exlimit': 1,
            'explaintext': True,
            'exsectionformat': 'plain',
            'exsectionformat': 'plain',
            'exintro': True
        }
    }
}
