import requests
from bs4 import BeautifulSoup as Bs

url = "https://horoscopes.rambler.ru/zodiac/general/all/today/"
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/53.0.2785.143 Safari/537.36'
}


def parser_horoscope(url) -> str:
    r = requests.get(url, headers=headers)
    soup = Bs(r.text, 'html.parser')
    horoscope = soup.find('div', {'class': "_1E4Zo _3BLIa"})
    return horoscope.text


esoteric = parser_horoscope(url)
