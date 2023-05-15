import requests
import os
from get_photo_and_parce_file import download_photo
from dotenv import load_dotenv
from datetime import datetime, timedelta


EPIC_API_URL = 'https://api.nasa.gov/EPIC/api/natural/date'


def get_epic_photos(date, token):
    EPIC_API_PARAMS = {'api_key': token}
    date_string = date.strftime('%Y-%m-%d')
    url = f'{EPIC_API_URL}/{date_string}'
    response = requests.get(url, params=EPIC_API_PARAMS)
    response.raise_for_status()
    data = response.json()
    image_urls = [f"https://api.nasa.gov/EPIC/archive/natural/{date.year}/{date.strftime('%m')}/{date.strftime('%d')}/png/{image['image']}.png?api_key={token}" for image in data]
    return image_urls


def main():

    load_dotenv()
    token = os.environ['NASA_TOKEN']

    start_date = datetime.utcnow() - timedelta(days=4)

    for i in range(5):
        date = start_date + timedelta(days=i)
        image_urls = get_epic_photos(date, token)

        for num, url_photo in enumerate(image_urls):
            try:
                download_photo(url_photo, f'epic_{num}')
                print(f'Фото {num + 1} загружено')
            except Exception as e:
                print(f'Ошибка загрузки фото {num + 1}: {e}')


if __name__ == '__main__':
    main()
