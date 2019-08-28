function inputKeydown(event) {
    if(event.keyCode == 13) {
        search();
    }
}

function search() {
    var loadingElement = document.getElementById('loading');
    loadingElement.style.display = 'block';

    var mapElement = document.getElementById('map');
    var searchValue = document.getElementById('search').value;

    var request = new XMLHttpRequest();
    request.open('GET', '/get-search-info?data=' + searchValue);
    request.send();

    request.onreadystatechange = function(event) {
        if (request.readyState === 4) {
            loadingElement.style.display = 'none';

            var data = JSON.parse(request.response);

            var url = data.url;
            var text = data.info;
            var articleURL = data.article_url;
            var searchData = data.search_data;
            var additionalMessage = data.additional_info;

            addMessage(url, searchData, text, articleURL);

            if (additionalMessage) {
                addMessage(null, null, additionalMessage, null);
            }
        }
    }
}

function addMessage(mapUrl, searchData, text, articleURL) {
    var cardElement = document.createElement('div');
    cardElement.setAttribute('class', 'card');

    var mapElement = document.createElement('iframe');
    mapElement.setAttribute('src', mapUrl);
    mapElement.setAttribute('class', 'card-image-top');
    mapElement.setAttribute('height', 400);
    mapElement.setAttribute('frameborder', 0);

    var infoElement = document.createElement('div');
    infoElement.setAttribute('class', 'card-body');

    var headingElement = document.createElement('h5');
    headingElement.setAttribute('class', 'card-title');
    headingElement.innerText = searchData;

    var textElement = document.createElement('p');
    textElement.setAttribute('class', 'card-text');
    textElement.innerHTML = (text || '').slice(0, 500) + ((text || '').length > 500 ? '...' : '');

    if (searchData) {
        infoElement.appendChild(headingElement);
    }
    infoElement.appendChild(textElement);

    var wikiArticleLink = document.createElement('a');
    wikiArticleLink.href = articleURL;
    wikiArticleLink.innerText = 'En savoir plus sur Wikipedia';

    if(articleURL) {
        infoElement.appendChild(wikiArticleLink);
    }

    if (mapUrl) {
        cardElement.appendChild(mapElement);
    }

    cardElement.appendChild(infoElement);

    var resultElement = document.getElementById('result')
    resultElement.appendChild(cardElement);

    resultElement.scrollTop = resultElement.scrollHeight;

    document.getElementById('search').value = '';
}