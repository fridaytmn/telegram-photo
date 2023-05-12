import requests
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint
from os import path, environ
from urllib import parse
from datetime import datetime


def fetch_spacex_last_launch():

    link = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
    try:
        responce = requests.get(link)
        responce.raise_for_status()
        responce = responce.json()
        urls_photos = responce['links']['flickr']['original']
        pprint(urls_photos)
        return urls_photos
    except requests.ConnectionError:
        print('Сайт недоступен')


def fetch_nasa_photos():
    token = environ['NASA_TOKEN']
    link = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': token,
              'count': 30,
              'thumbs': False,
              'hd': True}
    try:
        responce = requests.get(link, params=params)
        responce.raise_for_status()
        responce = responce.json()
        urls_photos = [url['url'] for url in responce if url['media_type'] == 'image']
        return urls_photos
    except requests.HTTPError:
        raise requests.ConnectionError


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
    


def get_extension_file(url):

    file = parse.urlparse(url).path
    url_file = parse.unquote(file)
    path_file = path.splitext(url_file)[1]
    return path_file


def download_photo(url, filename):

    responce = requests.get(url)
    responce.raise_for_status()

    with open(f'images/{filename}', 'wb') as file:
        file.write(responce.content)


def main():
    
    load_dotenv()
    
    fetch_epic_photos()
    # try:
    #     for number_photo, url_photo in enumerate(fetch_nasa_photos()):
    #         download_photo(url_photo,
    #                        f'nasa_{number_photo}{get_extension_file(url_photo)}')
    # except FileNotFoundError:
    #     Path('images').mkdir(parents=True, exist_ok=True)
    #     main()

if __name__ == '__main__':
    main()
