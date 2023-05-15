from urllib import parse
import requests
from os import path


def get_extension_file(url):

    file = parse.urlparse(url).path
    url_file = parse.unquote(file)
    path_file = path.splitext(url_file)[1]

    return path_file


def download_photo(url, filename):

    responce = requests.get(url)
    responce.raise_for_status()

    with open(f'images/{filename}{get_extension_file(url)}', 'wb') as file:
        file.write(responce.content)


if __name__ == '__main__':
    pass
