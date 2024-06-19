from cgitb import html
import re
import requests
from bs4 import BeautifulSoup

class Bing_Img:
    def __init__(self) -> None:
        self.url="https://cn.bing.com"
        self.header=[]

        
if __name__=='__main__':
    BI = Bing_Img()  
    html = requests.get(BI.url).text
    url_img = re.findall('<link rel=\"preload\" href=\"(.*?)&amp;',html,re.S)
    print(url_img)
    BI.url = BI.url + url_img[0]
    print(BI.url)
    pic = requests.get(BI.url)
    fp = open("D:\\project\\program\\1.jpg",'wb+')
    fp.write(pic.content)
    fp.close()