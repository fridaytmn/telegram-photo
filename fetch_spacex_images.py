import requests
import argparse
from get_photo_and_parce_file import download_photo


def get_spacex_launch(id):

    link = f'https://api.spacexdata.com/v5/launches/{id}'
    try:
        response = requests.get(link)
        response.raise_for_status()
    except requests.HTTPError:
        raise requests.HTTPError('Неверный ID')

    return response.json()['links']['flickr']['original']


def create_parser():

    parser = argparse.ArgumentParser(description='Принимает ID запуска SpaceX')
    parser.add_argument('--id', default='latest', help='ID запуска')
    return parser


def main():

    parser = create_parser()
    id = parser.parse_args().id
    try:
        photos_urls = get_spacex_launch(id)
        if photos_urls:
            for num, photo in enumerate(photos_urls):
                download_photo(photo, f'SpaceX_{num}')
                print(f'Фото {num + 1} загружено')
            print('Загрузка завершена!')
        else:
            print('Нет фото для загрузки')
    except requests.HTTPError as error:
        print(error)


if __name__ == '__main__':
    main()
