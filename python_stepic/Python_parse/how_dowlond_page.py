from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
s = str(html)
list =[]
state = 0
for c in s:
    if c == '<':
        state = 1
    if c == '>':
        state = 0
    elif  state == 0:
        list.append(c)
s = ''.join(list)
print(s)
# print(s.count('C++'))
