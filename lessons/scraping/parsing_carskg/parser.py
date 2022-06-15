import csv
import requests

from bs4 import BeautifulSoup as bs
from datetime import datetime
from multiprocessing import Pool

links = []

def get_links(url):
    response = requests.get(url).text
    soup = bs(response, 'lxml')
    deputs = soup.find('div', class_='grid-deputs').find_all('div', class_='dep-item')
    
    for deput in deputs:
        a = deput.find('a', class_='name').get('href')
        a = 'http://www.kenesh.kg' + a
        links.append(a)


def get_all_links():
    for i in range(1,6):
        get_links(f'http://kenesh.kg/ky/deputy/list/35?page={i}')



def get_page_data(url):
    response = requests.get(url).text
    soup = bs(response, 'lxml')
    name = soup.find('div', class_='deput-name').text.strip()
    bio = soup.find('div', class_='ck-editor').text.strip()
    data = {'name': name, 'bio': bio, 'url': url}
    write_to_scv(data)

def write_to_scv(data):
    with open('deputs.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'], data['bio'], data['url']))

# start = datetime.now()
# get_all_links()
# for link in links:
#     get_page_data(link)
# end = datetime.now()
# print(end - start)

start = datetime.now()
with Pool(8) as proc:
    get_all_links()
    proc.map(get_page_data, links)

end = datetime.now()
print(end - start)



