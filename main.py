import os
import time
import random
import telegram_space_bot
import argparse
from dotenv import load_dotenv


def create_parser():

    parser = argparse.ArgumentParser(description='Задает интервал публикации постов')
    parser.add_argument('--hour', default=4, help='Интервал публикаций')
    return parser


def main():
    load_dotenv()
    BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
    CHAT_ID = os.environ['CHAT_ID']
    interval = int(create_parser().parse_args().hour) * 60 * 60
    while True:
        photo_files = os.listdir('images')
        random.shuffle(photo_files)
        for photo in photo_files:
            telegram_space_bot.send_photo_to_tg(BOT_TOKEN, CHAT_ID, photo)
            time.sleep(interval)


if __name__ == '__main__':
    main()
