import urllib.request
import threading
from bs4 import BeautifulSoup
def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(lis,name):
    for i in lis:
        soup=BeautifulSoup(get_html('https://www.nic.ru/whois/?searchWord='+name+i),"html.parser")
        answer=soup.find('div', class_="_1_uOq")
        if answer is None:
            print('{} свободен'.format(name + i))
            finallist.append(i[1:])
        else:
            print(answer.text)


finallist=list()
def main():
    name=input('Enter your wished name ')
    f=open('domainlist.txt','r')
    mylist=[]
    for str in f:
        mylist.append(str.replace("\n",''))
    div=int(len(mylist)/2)
    lis2 = mylist[div:len(mylist)]
    lis1 = mylist[0:div]
    t1=threading.Thread(target=parse, args=[lis1,name])
    t2 = threading.Thread(target=parse, args=[lis2,name])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    finallist.sort()
    for i in finallist:
        print(name+'.'+i)
if __name__ == '__main__':
    main()