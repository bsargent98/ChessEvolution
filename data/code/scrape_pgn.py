#Import libraries
import os
import requests
from bs4 import BeautifulSoup
import mechanize

#Set up requests session
login_url = 'https://chess-db.com/public/login.jsp?'
login_data = dict(username='YourEmail@something.com', password='password')
session = requests.session()

r = session.post(login_url, data=login_data)


def scrape_page(start):
    page = session.get('https://chess-db.com/public/execute.jsp?age=99&countries=all&sex=a&start={}'.format(start))
    soup = BeautifulSoup(page.content, 'html.parser')
    url = 'https://chess-db.com/public/'

    os.mkdir("../pgn_by_id/" + str(round(start/1000)))
    
    links = soup.find_all('a')
    
    cnt = 0
    n = 1000
    for link in links:
        if 'download.jsp?id=' in link['href']:
            cnt = cnt + 1
            url_full = url + link['href']
            id = link['href'][16:]
                
            print('Requesting page at {}'.format(url_full))
            r = session.get(url_full, allow_redirects=True)
                
            print('Got page at {}. Writing...'.format(url_full))
            open('../pgn_by_id/{}/{}.pgn'.format(round(start / 1000), id), 'wb').write(r.content)
    
            print('Saved page at {} as /data/pgn_by_id/{}.pgn'.format(url_full, id))
            print('{}/{}'.format(cnt, n))
            print('\n\n=================\n\n\n')
			

start = 0
stop = 100000

i = start
while i < stop:
    scrape_page(i)
    i = i + 1000
