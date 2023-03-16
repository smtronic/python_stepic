from re import findall
from urllib.request import urlopen
from collections import Counter

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
s = str(html)
list =[]
state = 0
# for c in s.split():
#     if c == '<code>':
#         state = 1
#     if c == '</code>':
#         state = 0
#     elif  state == 0:
#         list.append(c)

regex = '<code>(.*?)</code>'
l = sorted(findall(regex, s))
l = Counter(l)
maximum = max(l.values())
for key, value in l.items():
    if value == maximum:
        print(key, end = ' ')

print(maximum)
