import requests 
from bs4 import BeautifulSoup 
import csv 
csvfile = open('doctors.csv','w') 
filewriter = csv.writer(csvfile,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
filewriter.writerow(['Name','Specialization','Location','Rating in %', 'Link'])

#Extracting links from doctors.csv
def getLinks():
    x = []
    y = []
    d = open('doctors.csv')
    docs = csv.reader(d,delimiter=',')
    for row in docs:
        if len(row)==0:
            pass
        else:
            # x.append(row[3])
            z = row[4].split('=')
            x.append([row[4],row[0]])
    return x
def sol(page):
    docs = getLinks()
    print(docs)
    docs.pop(0)
    # print(docs)
    # return
    # Extracting Comments from each doctors page and saving it in doctorname.txt
    for url,id in docs:
        u = url.split("?")
        url = "/recommended?".join(u)
        # print(url)
        # url = 'https://www.practo.com/bangalore/doctor/sheela-chakravarthy-internal-medicine/recommended?specialization=Internal%20Medicine&practice_id=1136311'
        n = requests.get(url)
        # print(n)
        soup_new = BeautifulSoup(n.content, 'html5lib') 
        # name = soup_new.find(class_="c-profile__title u-bold u-d-inlineblock")
        # location = 'bangalore'
        # rate = soup_new.find(class_="u-green-text u-bold u-large-font")
        # specialization = 'General Physician'
        comments = soup_new.findAll(class_="feedback__content u-large-font ")
        writing = open('comments/'+str(id+'.txt'),'w')
        # print(len(comments),len(recom),len(comments) == len(recom))
        for i in range(len(comments)):
            try:
                writing.write(str(comments[i].text)+'\n')
            except:
                pass 
        writing.close()
        print(id)

def main():
    for i in range(1):
        sol(i) 
        

if __name__== '__main__':
    main()
