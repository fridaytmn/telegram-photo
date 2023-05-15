import requests
from os import environ
from get_photo_and_parce_file import download_photo
from dotenv import load_dotenv


def get_apod_photos(token):
    link = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': token, 'count': 30, 'thumbs': False, 'hd': True}
    try:
        response = requests.get(link, params=params)
        response.raise_for_status()
    except requests.HTTPError:
        print('Сайт недоступен')
        return []

    data = response.json()
    urls_photos = [url['url'] for url in data if url['media_type'] == 'image']
    return urls_photos


def download_apod_photo(token):
    urls_photos = get_apod_photos(token)
    for num, url_photo in enumerate(urls_photos):
        try:
            download_photo(url_photo, f'apod_{num}')
            print(f'Фото {num + 1} загружено')
        except Exception as e:
            print(f'Ошибка загрузки фото {num + 1}: {e}')


def main():
    load_dotenv()
    token = environ['NASA_TOKEN']
    download_apod_photo(token)
    print('Загрузка завершена')


if __name__ == '__main__':
    main()
