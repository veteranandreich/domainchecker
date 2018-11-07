import urllib.request
import multiprocessing
import time
from bs4 import BeautifulSoup


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html, site):
    soup = BeautifulSoup(html, "html.parser")
    answer = soup.find('div', class_="_1_uOq")
    if answer is None:
        print('{}свободен'.format(site[0:-1]))
    else:
        print(answer.text)


def main():
    name = input('Enter your wished name ')
    f = open('domainlist.txt', 'r')
    for str in f:
        t = multiprocessing.Process(target=parse, args=[get_html('https://www.nic.ru/whois/?searchWord=' + name + str), name + str])
        t.start()


if __name__ == '__main__':
    main()
