import requests
from bs4 import BeautifulSoup
def news():
    url='http://www.hindustantimes.com/top-news'
    resp=requests.get(url)
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'html.parser')
        l=soup.find("ul",{"class":"latest-news-bx more-latest-news more-separate"})
        for i in l.findAll("a"):
            var=i.text
            x=var.replace('read more',' ')
            print(x)
    else:
        print("Error,Internet connection is not available")

news()
input("Press enter to exit ;)")
