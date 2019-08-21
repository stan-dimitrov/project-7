function getData() {
    var request = new XMLHttpRequest();
    request.open('GET', '/get-data');

    request.send();

    request.onreadystatechange = function(event) {
        if (request.readyState === 4) {
            var randomNumber = request.response;
            var listElement = document.getElementById('list');
            var randomNumberElement = document.createElement('li');
            randomNumberElement.innerText = randomNumber;

            listElement.appendChild(randomNumberElement);
        }
    }
}

function getRandomWikiArticles() {
    var request = new XMLHttpRequest();
    request.open('GET', '/get-random-wiki-article');

    request.send();

    request.onreadystatechange = function(event) {
        if (request.readyState === 4) {
            var wikiJSONResponse = JSON.parse(request.response);
            var articles = wikiJSONResponse.query.random;
            var listElement = document.getElementById('wiki-articles');

            for (var i = 0; i <= articles.length; i++) {
                var article = articles[i];

                var randomWikiElement = document.createElement('p');
                randomWikiElement.innerText = article.title + '(' + article.id + ')';

                listElement.appendChild(randomWikiElement);
            }
        }
    }
}