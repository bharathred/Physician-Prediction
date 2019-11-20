import requests 
from bs4 import BeautifulSoup 
import csv 
csvfile = open('practo.csv','w') 
filewriter = csv.writer(csvfile,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
filewriter.writerow(['Name','Specialization','Location', 'Link'])

def sol(page):
    URL = "https://www.practo.com/bangalore/doctors?page=" + str(page)
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    l = list()
    x = soup.find_all(class_="c-card-info")
    for p in x:
        y = p.find('a',href=True)
        if y!=None:
            l.append(y['href'])
    prev = ''
    for i in l:
        url = "https://www.practo.com" + i 
        n = requests.get(url)
        soup_new = BeautifulSoup(n.content, 'html5lib') 
        name = soup_new.find(class_="c-profile__title u-bold u-d-inlineblock")
        location = 'bangalore'
        specialization = 'general physician'
        try:
            location = i.split('/')[1]
            specialization = i.split('/')[3].split('specialization=')[1].split('&')[0]
            if specialization == None or specialization == '':
                specialization = 'general physician'
        except:
            pass 
        if name !=None :
            if prev!=name.text:
                print(name.text,'::',specialization)
                filewriter.writerow([name.text,specialization,location, url])
                prev = name.text

def main():
    for i in range(1,900):
        sol(i) 

if __name__== '__main__':
    main()
