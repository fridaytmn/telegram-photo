import requests
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint
from os import path, environ
from urllib import parse
from datetime import datetime


def fetch_epic_photos():
    token = environ['NASA_TOKEN']
    link = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': token}
    try:
        responce = requests.get(link, params=params)
        responce.raise_for_status()
    except:
        pass
    responce = responce.json()
    for number, photo in enumerate(responce[-5:]):
        photo_date = datetime.strptime(photo['date'], '%Y-%m-%d %H:%M:%S')
        image = photo['image']
        link_foto = 'https://api.nasa.gov/EPIC/archive/natural'
        url_for_foto = f'{link_foto}/{photo_date.year}/{photo_date.month:0{2}}/{photo_date.day:0{2}}/png/{image}.png'
        responce = requests.get(url_for_foto, params=params)
        responce.raise_for_status()
        
        with open(f'images/epic_{number}.png', 'wb') as file:
            file.write(responce.content)


def main():

    load_dotenv()

    fetch_epic_photos()


if __name__ == '__main__':
    main()
