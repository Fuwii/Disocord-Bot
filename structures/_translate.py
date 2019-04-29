import requests
from urllib import parse


def translate(text: str, lang: str = 'en',
              key="trnsl.1.1.20190401T141303Z.df3305cf098f00f8.836327f2e8520442fad0173356e900eaf4b92249"):
    request = f"https://translate.yandex.net/api/v1.5/tr.json/translate?key={key}&text={parse.quote(text)}&lang={lang}"

    response = requests.get(request)
    if response:
        json_response = response.json()
    else:
        raise ValueError
    return json_response
