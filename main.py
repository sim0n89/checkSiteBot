import telebot
from config import TOKEN, CHANEL_ID, urls
import traceback
import requests


bot = telebot.TeleBot(TOKEN)

def send_message(url, status):
    try:
        message = f'Проблема с сайтом {url}, статус {status}'
        bot.send_message(CHANEL_ID, message)
    except Exception:
        traceback.print_exc()


def checkSite(url):
    r = requests.get(url)
    try:
        status = r.status_code
        if status!=200:
            send_message(url,status)

    except Exception:
        traceback.print_exc()

if __name__ == '__main__':
    for url in urls:
        checkSite(url)





