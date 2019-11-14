import requests
from bs4 import BeautifulSoup
import mechanize

'''
br = mechanize.Browser()
br.open('https://chess-db.com/public/execute.jsp?age=99&countries=all&sex=a&start=0')
br.select_form(nr = 0)
br.form['username'] = 'sargentbrett18@hotmail.com'
br.form['password'] = 'chinchico'
br.submit()
print(br.response().read())
'''

n = 1000
url = 'https://chess-db.com/public/'

login_url = 'https://chess-db.com/public/login.jsp?'
login_data = dict(username='sargentbrett18@hotmail.com', password='chinchico')
session = requests.session()

r = session.post(login_url, data=login_data)

print(r.text)

page = session.get('https://chess-db.com/public/execute.jsp?age=99&countries=all&sex=a&start=0')
soup = BeautifulSoup(page.content, 'html.parser')

links = soup.find_all('a')

cnt = 0
for link in links:
	if 'download.jsp?id=' in link['href']:
		cnt = cnt + 1
		url_full = url + link['href']
		id = link['href'][16:]
		
		print('Requesting page at {}'.format(url_full))
		r = session.get(url_full, allow_redirects=True)
		
		print('Got page at {}. Writing...'.format(url_full))
		open('../pgn_by_id/{}.pgn'.format(id), 'wb').write(r.content)

		print('Saved page at {} as /data/pgn_by_id/{}.pgn'.format(url_full, id))
		print('{}/{}'.format(cnt, n))
		print('\n\n=================\n\n\n')