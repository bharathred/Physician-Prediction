import requests 
from bs4 import BeautifulSoup 
import csv 
csvfile = open('doctors.csv','w') 
filewriter = csv.writer(csvfile,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
filewriter.writerow(['Name','Specialization','Location','Rating in %', 'Link'])
LOCATION = "mumbai"
# LOCATION = input()
def sol(page):
    #Extracting links from page=i on practo.com/LOACTION
    URL = "https://www.practo.com/"+LOCATION+"/doctors?page=" + str(page)
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    l = list()
    # x = soup.find_all(class_="c-card-info")
    x = soup.find_all(class_="info-section")
    #Saving all the links
    for p in x:
        y = p.find('a',href=True)
        if y!=None:
            l.append(y['href'])
    prev = ''
    # print(l)
    #Going on each link and extracting details
    for i in l:
        url = "https://www.practo.com" + i 
        n = requests.get(url)
        soup_new = BeautifulSoup(n.content, 'html5lib') 
        name = soup_new.find(class_="c-profile__title u-bold u-d-inlineblock")
        # location = 'mumbai'
        location = LOCATION
        rate = soup_new.find(class_="u-green-text u-bold u-large-font")
        specialization = 'General Physician'
        # print(url,' ::',rate.text)
        # return
        try:
            location = i.split('/')[1]
            specialization = i.split('/')[3].split('specialization=')[1].split('&')[0]
            if specialization == None or specialization == '':
                specialization = 'General Physician'
        except:
            pass 
        if name !=None and rate!=None:
            if prev!=name.text:
                print(name.text,'::',specialization)
                filewriter.writerow([name.text,specialization,location,rate.text, url])
                prev = name.text

def main():
    for i in range(1,900):
        print('<=======Scraping page ',i,'========>')
        sol(i) 
        

if __name__== '__main__':
    main()
