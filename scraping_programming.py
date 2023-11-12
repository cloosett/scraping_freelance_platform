import time
import requests
from bs4 import BeautifulSoup

number_pages = int(input('How many pages should be parsed?: '))
def scraping(number_pages):
    for i in range(1, number_pages + 1):
        url = f'https://freelance.ua/orders/?orders=web-development%2Cprikladnoj-programmist%2Cdatabases%2C1c-programming%2Cqa-testing%2Cgame-programming%2Cembedded-systems%2Cdata-protection%2Cplugins-scripts-utilities%2Cweb-proektirovanie%2Cdevelopment-crm-erp%2Csystem-programming%2Cproject-management-development%2Candroid-development%2Cios-development&page={i}&pc=1'
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
                    print(f'\nTitle📝: {title}\nDescription💬: {description}\nPrice💸: {price}\nDate📅: {date}\nHref🔎: {href}\n\n')

                else:
                    date = find_all_li[1].text.strip()
                    print(f'\nTitle📝: {title}\nDescription💬: {description}\nPrice💸: {price}\nDate📅: {date}\nHref🔎: {href}\n\n')
            except Exception as e:
                print(e)


scraping(number_pages)