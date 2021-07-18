import requests
from bs4 import BeautifulSoup


def get_web_infor(url):

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')

    return links, subtext
# res = requests.get('https://news.ycombinator.com/news')
# soup = BeautifulSoup(res.text, 'html.parser')
# links = soup.select('.storylink')
# subtext = soup.select('.subtext')

links_page_1, subtext_page_1 = get_web_infor('https://news.ycombinator.com/news')
links_page_2, subtext_page_2 = get_web_infor('https://news.ycombinator.com/news?p=2')

links = links_page_1 + links_page_2
subtexts = subtext_page_1 + subtext_page_2

def sort_stories_by_votes(hnlist):

    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtexts):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtexts[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 90:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)

hn_sorted = create_custom_hn(links, subtexts)

import pandas as pd

df = pd.DataFrame(hn_sorted)
print(df)