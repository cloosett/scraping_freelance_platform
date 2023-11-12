import time
import telebot
import requests
from bs4 import BeautifulSoup

TOKEN = 'your token'

bot = telebot.TeleBot(TOKEN)

detected_first_name = None

def scraping_first_title():
    url = 'https://freelance.ua/orders/?orders=web-development%2Cprikladnoj-programmist%2Cdatabases%2C1c-programming%2Cqa-testing%2Cgame-programming%2Cembedded-systems%2Cdata-protection%2Cplugins-scripts-utilities%2Cweb-proektirovanie%2Cdevelopment-crm-erp%2Csystem-programming%2Cproject-management-development%2Candroid-development%2Cios-development&page=1&pc=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    search_first = soup.find('li', class_='j-order')
    search_first_title = soup.find('header', class_='l-project-title').text.strip()
def scraping(message, i, url):
    bot.send_message(message.chat.id, 'Scraping starting..🟢')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    search = soup.find_all('li', class_='j-order')

    for row in search:
        href = row.find('a').get('href')
        try:
            response = requests.get(href)
            soup = BeautifulSoup(response.text, 'lxml')
            find_date_ul = soup.find('ul', class_='l-item-features')
            find_all_li = find_date_ul.find_all('li')

            title = soup.find('h1', style='word-break: break-word;').text.strip()
            description = soup.find('article').text.strip()
            price = soup.find('div', class_='o-project-price o-project-price_show-sm').text.strip()
            if len(find_all_li) == 6:
                date = find_all_li[2].text.strip()
                bot.send_message(message.chat.id,
                                 f'Title📝: {title}\nDescription💬: {description}\nPrice💸: {price}\nDate📅: {date}\nHref🔎: {href}\n\n')

            else:
                date = find_all_li[1].text.strip()
                bot.send_message(message.chat.id,
                                 f'Title📝: {title}\nDescription💬: {description}\nPrice💸: {price}\nDate📅: {date}\nHref🔎: {href}\n\n')
        except Exception as e:
            bot.send_message(message.chat.id, e)
    bot.send_message(message.chat.id, 'Scraping ended successfully✅')


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    programming_order_button = telebot.types.KeyboardButton("Scraping programming order👨🏽‍💻")
    all_order_button = telebot.types.KeyboardButton("Scraping all order👁👁")
    markup.row(programming_order_button, all_order_button)

    bot.send_message(message.chat.id, "Hello, this is a bot for parsing orders from 'freelance.ua' ", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Scraping programming order👨🏽‍💻":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        scraping_full_order_button = telebot.types.KeyboardButton("Scraping full order😳")
        message_new_task = telebot.types.KeyboardButton("Message, if new task😉")
        enter_pages_button = telebot.types.KeyboardButton("Enter the number of pages to be scraping👇")
        markup.row(scraping_full_order_button,message_new_task, enter_pages_button)

        bot.send_message(message.chat.id, "Choose option👇 ",
                         reply_markup=markup)
    elif message.text == "Scraping full order😳":
        bot.send_message(message.chat.id, "Please wait, parsing is in progress⏳")
        for i in range(1, 12):
            url = f'https://freelance.ua/orders/?orders=web-development%2Cprikladnoj-programmist%2Cdatabases%2C1c-programming%2Cqa-testing%2Cgame-programming%2Cembedded-systems%2Cdata-protection%2Cplugins-scripts-utilities%2Cweb-proektirovanie%2Cdevelopment-crm-erp%2Csystem-programming%2Cproject-management-development%2Candroid-development%2Cios-development&page={i}&pc=1'
            scraping(message, i, url)
    elif message.text == "Enter the number of pages to be scraping👇":
        bot.send_message(message.chat.id, 'Enter the number pages..')
        bot.register_next_step_handler(message, scraping_programing_number_pages)
    elif message.text == "Scraping all order👁👁":
        bot.send_message(message.chat.id, 'Enter the number pages..')
        bot.register_next_step_handler(message, scraping_all_number_pages)
    elif message.text == "Message, if new task😉":
        global detected_first_name
        bot.send_message(message.chat.id, 'Wait new message..😮')
        while True:
            url = 'https://freelance.ua/orders/?orders=web-development%2Cprikladnoj-programmist%2Cdatabases%2C1c-programming%2Cqa-testing%2Cgame-programming%2Cembedded-systems%2Cdata-protection%2Cplugins-scripts-utilities%2Cweb-proektirovanie%2Cdevelopment-crm-erp%2Csystem-programming%2Cproject-management-development%2Candroid-development%2Cios-development&page=1&pc=1'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            search_first = soup.find('li', class_='j-order')
            search_first_title = soup.find('header', class_='l-project-title').text.strip()

            if detected_first_name is None:
                detected_first_name = search_first_title

            if detected_first_name != search_first_title:
                bot.send_message(message.chat.id, 'New task detected! Check it out.')
                detected_first_name = search_first_title

            time.sleep(300)


def scraping_programing_number_pages(message):
    int_message_text = int(message.text)
    for i in range(1, int_message_text + 1):
        url = f'https://freelance.ua/orders/?orders=web-development%2Cprikladnoj-programmist%2Cdatabases%2C1c-programming%2Cqa-testing%2Cgame-programming%2Cembedded-systems%2Cdata-protection%2Cplugins-scripts-utilities%2Cweb-proektirovanie%2Cdevelopment-crm-erp%2Csystem-programming%2Cproject-management-development%2Candroid-development%2Cios-development&page={i}&pc=1'
        scraping(message, i, url)

def scraping_all_number_pages(message):
    int_message_text = int(message.text)
    for i in range(1, int_message_text + 1):
        url = f'https://freelance.ua/orders/?page={i}&pc=1'
        scraping(message, i, url)



bot.polling(none_stop=True)
