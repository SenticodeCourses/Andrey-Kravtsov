import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open ('films.csv', 'a') as f:
        writer = csv.writer(f)

    writer.writerow(({  data['rus_title'],
                        data['eng_title'],
                        data['url']}))



def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    ads = soup.find('div', class_= 'art content').find_all('div', class_= 'post-home')
    for ad in ads:

        try:
            url = ad.find('div', class_='post-home').find('a').get('href')
        except:
            url = ''
        try:
            rus_title = ad.find('div', class_='post-home').find('a').find('img').get('alt')
        except:
            rus_title = ''
        try:
            eng_title = ad.find('div', class_='original').text.strip()
        except:
            eng_title = ''

    data = {'url' : url,
            'rus_title': rus_title,
            'eng_title': eng_title}
    return data



def get_total_pages(html):
    soup = BeautifulSoup(html, 'html.parser')

    pages = soup.find('div', class_ = 'art-pager').find_all('a', class_='page-numbers')[-1].get('href')
    print(pages)


def main():
    url = 'http://cobrafilm.club/films'
    base_url = 'http://cobrafilm.club/film/god/'
    year_part = '2014-year'
    page_part = '/page/'
    for i in range (1, 20):
        gen_url = base_url + year_part + page_part + str(i)

def write_into_file(data):
    my_file = open('films.txt', 'a')
    my_file.write('%s : %s\n' % (data['rus_title'], data['eng_title'], data['url']))
    my_file.close()


write_csv('data')
