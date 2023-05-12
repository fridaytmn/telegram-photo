import requests
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint
from os import path, environ
from urllib import parse


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
              'count': 25}
    
    responce = requests.get(link, params=params)
    responce.raise_for_status()
    responce = responce.json()
    pprint(responce)
    # urls_photos = [url['url'] for url in responce]
    # pprint(urls_photos)
        #url_photos = responce


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
        
    fetch_nasa_photos()
    # try:
    #     for number_photo, url_photo in enumerate(fetch_spacex_last_launch()):
    #         download_photo(url_photo, f'spacex_{number_photo}.jpg')
    # except FileNotFoundError:
    #     Path('images').mkdir(parents=True, exist_ok=True)
    #     main()

if __name__ == '__main__':
    main()
