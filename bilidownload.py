# -*- coding:gb18030 -*-
from base64 import encode
from os import path
import re
import pprint
import subprocess
from matplotlib.pyplot import title
import requests
from bs4 import BeautifulSoup
from requests.packages import urllib3
import os 

class BiliDownload:
    def __init__(self):
        self.url="https://www.bilibili.com/video/BV1Xq4y1x7c6"
        
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
            'Referer': 'https://www.bilibili.com/',
        }
        
        self.path = " "
        
    def download(self,r,path):
        url=re.findall('"baseUrl\":"(.*?)\"',r.text)
         
        video=requests.get(url[0],headers=BD.header)
        audio=requests.get(url[-1],headers=BD.header) #每隔一段时间，音频的url就会发生变化
        
        title=re.findall('name=\"title\" content=\"(.*?)_哔哩哔哩',r.text)
        author=re.findall('name="author" content="(.*?)"',r.text)
        BD.path=path+author[0]+ '-' +title[0]
        
        fp=open(BD.path + ".mp4","wb+")
        fp.write(video.content)
        fp.close()
        
        fp=open(BD.path + ".mp3","wb+")
        fp.write(audio.content)
        fp.close()
    
        
        
    def combine(self,path):    
        print("合成音频和视频...")
        cmd ='ffmpeg -i '+path + ".mp4" +' -i '+path + ".mp3" +' -c copy '+path+"_.mp4"
        print (cmd)
        os.system(cmd)
        #subprocess.call(cmd, shell=True)  
    

    
    
    
if __name__=='__main__':
    BD = BiliDownload()

    urllib3.disable_warnings() #忽略报错信息
    req=requests.get(BD.url,headers=BD.header,verify=False)
    print(req.json())
    path=""
    #path=input("输入保存地址")
    #BD.url=input("输入视频链接")

    if req.status_code <400:
        BD.download(req,path)
        #print(BD.path)
        BD.combine(BD.path)
    
    