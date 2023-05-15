import telegram


def send_photo_to_tg(BOT_TOKEN, CHAT_ID, filename):
    bot = telegram.Bot(token=BOT_TOKEN)
    bot.send_photo(chat_id=CHAT_ID, photo=open(f'images/{filename}', 'rb'))


def main():
    pass


if __name__ == '__main__':
    main()
