import requests
import random
from bs4 import BeautifulSoup as Bs

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/53.0.2785.143 Safari/537.36'
}
url = "https://www.anekdot.ru/last/good"


def parser() -> list:
    url = "https://www.anekdot.ru/last/good"
    r = requests.get(url, headers=headers)
    soup = Bs(r.text, 'html.parser')
    anekdots = soup.find_all('div', {'class': 'text'})
    return [c.text for c in anekdots]


list_of_jokes = parser()
random.shuffle(list_of_jokes)
