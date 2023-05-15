import telegram
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
bot = telegram.Bot(token='6002224684:AAEoFSTjFYCRRRqgu3ampD0I_3iBax2_Vzk')
print(bot.get_me())
bot.send_photo(chat_id='-1001514356106', photo=open('images/SpaceX_0.jpg', 'rb'))