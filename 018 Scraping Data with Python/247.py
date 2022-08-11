from hashlib import new
import requests
from bs4 import BeautifulSoup

pages = ['https://news.ycombinator.com/news',
         'https://news.ycombinator.com/news?p=2']

news = []
subtext = []

for page in pages:
    res = requests.get(page)
    # print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    news += soup.select('.titlelink')
    subtext += soup.select('.subtext')


def create_my_hackerset(news, subtext):
    data = []
    for idx, item in enumerate(news):
        item_text = item.getText()

        score_class = subtext[idx].select('.score')

        if len(score_class):
            score = int(score_class[0].getText().replace(' points', ''))
            data.append({'title': item_text, 'score': score
                         })
        else:
            data.append({'title': item_text, 'score': 0})

    return data


def sort_hackerset_byscore(data):
    return sorted(data, key=lambda k: k['score'], reverse=True)


def display_hackerset(data):
    for idx, i in enumerate(data):
        print(str(idx+1)+'.', i['title'], ' - ', i['score'])


data = create_my_hackerset(news, subtext)
data = sort_hackerset_byscore(data)
display_hackerset(data)
