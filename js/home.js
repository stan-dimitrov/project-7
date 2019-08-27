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

            var cardElement = document.createElement('div');
            cardElement.setAttribute('class', 'card');

            var mapElement = document.createElement('iframe');
            mapElement.setAttribute('src', url);
            mapElement.setAttribute('class', 'card-image-top');
            mapElement.setAttribute('height', 400);
            mapElement.setAttribute('frameborder', 0);

            var infoElement = document.createElement('div');
            infoElement.setAttribute('class', 'card-body');

            var headingElement = document.createElement('h5');
            headingElement.setAttribute('class', 'card-title');
            headingElement.innerText = searchValue;

            var textElement = document.createElement('p');
            textElement.setAttribute('class', 'card-text');
            textElement.innerText = text.slice(0, 500) + (text.length > 500 ? '...' : '');

            infoElement.appendChild(headingElement);
            infoElement.appendChild(textElement);

            cardElement.appendChild(mapElement);
            cardElement.appendChild(infoElement);

            var resultElement = document.getElementById('result')
            resultElement.prepend(cardElement);

            document.getElementById('search').value = '';
        }
    }
}