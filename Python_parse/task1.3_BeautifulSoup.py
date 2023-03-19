from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://stepik.org/media/attachments/lesson/245130/6.html').read().decode('utf8')# скачиваем файл
s = str(html)
soup = BeautifulSoup(s, 'html.parser') # делаем суп

for a in soup.find_all('a', href=True):
    print(a['href'])
