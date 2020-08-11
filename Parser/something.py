from bs4 import BeautifulSoup
import requests

def save_1():
    with open('parse_info_1.text','a', encoding="utf-8") as file:
       file.write(f'{comp["title"]}->Price:{comp["price"]}->Link:{comp["link"]}->Image:{["image"]}\n') 

def parse_1():
    URL ='https://allepnina.ru/catalog/moldingi-s-gladkim-profilem/filter/manufacturer-is-decor%20dizayn/apply/'
    HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.95'
    }

    response = requests.get(URL,headers = HEADERS)
    soup = BeautifulSoup(response.content,"html.parser")
    items = soup.findAll('div',class_ = 'catalog-item-info')
    comps = []


    for item in items:
        comps.append({
            'title': item.find('a', class_="item-title").get_text(strip=True),
            'price': item.find('span', class_="catalog-item-price").get_text(strip=True),
            'link': item.find('a', class_="item-title").get('href'),
            'image': item.find('img',class_="item_img").get('src')
        })

        global comp
        for comp in comps:
            print(f'{comp["title"]}->Price:{comp["price"]}->Link:{comp["link"]}->Image:{["image"]}')
            save_1()
parse_1()

###parsing second page###
def save_2():
    with open('parse_info_2.text','a', encoding="utf-8") as file:
       file.write(f'{comp["title"]}->Price:{comp["price"]}->Link:{comp["link"]}->Image:{["image"]}\n') 

def parse_2():
    URL ='https://allepnina.ru/catalog/molding-uglovoy/filter/manufacturer-is-decor%20dizayn/apply/'
    HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.95'
    }

    response = requests.get(URL,headers = HEADERS)
    soup = BeautifulSoup(response.content,"html.parser")
    items = soup.findAll('div',class_ = 'catalog-item-info')
    comps = []

    ###a little note##
    ### hello there##
    for item in items:
        comps.append({
            'title': item.find('a', class_="item-title").get_text(strip=True),
            'price': item.find('span', class_="catalog-item-price").get_text(strip=True),
            'link': item.find('a', class_="item-title").get('href'),
            'image': item.find('img',class_="item_img").get('img')
        })

        global comp
        for comp in comps:
            print(f'{comp["title"]}->Price:{comp["price"]}->Link:{comp["link"]}->Image:{["image"]}')
            save_2()
parse_2()