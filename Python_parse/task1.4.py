from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html').read().decode('utf8')# скачиваем файл
soup = BeautifulSoup(html, 'html.parser')
print(sum(int(i.get_text()) for i in soup.find_all('td')))
print(html)
