import requests 
from bs4 import BeautifulSoup 
URL = "https://www.practo.com/mangalore/doctors"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib') 

l = list()
x = soup.find_all(class_="c-card-info")
for i in x:
    y = i.find('a',href=True)
    if y!=None:
        l.append(y['href'])

prev = ''
for i in l:
    url = "https://www.practo.com/" + i 
    n = requests.get(url)
    soup_new = BeautifulSoup(n.content, 'html5lib') 
    name = soup_new.find(class_="c-profile__title u-bold u-d-inlineblock")
    if name !=None :
        if prev!=name.text:
            print(name.text)
        prev = name.text
