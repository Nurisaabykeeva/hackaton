










import requests
from bs4 import BeautifulSoup as BS
import csv


def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html, 'lxml')
    return soup

def get_data(soup):
    # catalog = soup.find('div', class_ = 'list-view')
    catalog = soup.find(
        'div', 
        {'id': 'w0'}
    )
    phones = catalog.find_all('div', class_='item product_listbox oh')
    print(phones)

    for phone in phones:
        # title = phone.find('a', target = '_blank').text.strip()
        try:
            title = phone.find('div', class_ = 'listbox_title oh').find('a').text.strip()
        except AttributeError:
            title = 'not found'
        
        print(title)
        image = phone.find('img').get('data-ssrc')
        # print(image)
        price = phone.find('div', class_ = 'listbox_price text-center').text.strip
        print(price)

        d = {
            'title': title, 
            'image': image, 
            'price': price
        }
        write_scv(d)

def write_scv(data):
    with open('phones.csv', 'a') as file:
        name = ['title', 'price', 'image']
        write = csv.DictWriter(file, delimiter=',', fieldnames=name)
        write.writerow(data)


def main():
    for i in range(1, 100):
        BASE_URL = f'https://www.kivano.kg/mobilnye-telefony?page={i + 1}'
        print(BASE_URL)
        html = get_html(BASE_URL)
        soup = get_soup(html)
        get_data(soup)



if __name__ == '__main__':
    main()