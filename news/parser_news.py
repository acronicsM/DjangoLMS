from requests import get
from datetime import datetime
import json


def parser():
    today = datetime.today()
    param = {
        'q': 'Python',
        'from': f'{today:%Y-%m-%d}',
        'sortBy': 'popularity',
        'apiKey': 'cf70d17d42014a649e48fd0bbb5b6b41',
        'page': 1,
    }

    response = get('https://newsapi.org/v2/everything', params=param)

    if not response.ok:
        pass

    with open(f'news/json_news/news{today:%Y%m%d}.json', 'w') as outfile:
        json.dump(response.json(), outfile)
