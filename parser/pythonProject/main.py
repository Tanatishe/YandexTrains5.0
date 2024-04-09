import requests
from bs4 import BeautifulSoup
from http.cookies import SimpleCookie

rawdata = 'cookie_here'
cookie = SimpleCookie()
cookie.load(rawdata)
cookies = {}
for key, morsel in cookie.items():
    cookies[key] = morsel.value

dick = {}

sess = requests.Session()
test = sess.get('https://contest.yandex.ru/contest/59539/standings/?p=1', cookies=cookies)


contests = [59539, 59540, 59541, 59542]
for contest in contests:
    for page_number in range(1, 21):
        url = f'https://contest.yandex.ru/contest/{contest}/standings/?p={page_number}'
        response = sess.get(url)
        text = response.text
        soup = BeautifulSoup(text, 'html.parser')
        table = soup.find('tbody')

        for i in table.find_all('tr'):
            row = []
            for j in i.find_all('td'):
                row.append(j.text)
            if row[1] not in dick:
                dick[row[1]] = [int(row[-2]), int(row[-1])]
            else:
                dick[row[1]][0] += int(row[-2])
                dick[row[1]][1] += int(row[-1])

with open('dick.txt', 'w') as file:
    for i, j in dick.items():
        string = str(i) + ' ' + ' '.join(map(str, j)) + '\n'
        file.write(string)
