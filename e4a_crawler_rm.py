# -*- coding: utf-8 -*-

import urllib.request as urllib2
from bs4 import BeautifulSoup
from urllib.parse import quote
import os.path
import codecs
        
    
def parse_body(el): # pe 3 sub-niveluri
    text=''
    
    for s in el.find_all('span'):
        if(s.parent.name !='td'):
            t=s.find(text=True,recursive=False)
            if (t is not None):
                text=text+'\n' +t
    return text
                                 
          

url="https://www.reginamaria.ro/articole-medicale/coronavirus?specialitate=All&cauta=&page="
filecovrm="full.txt"
lista = []
limit = 8
lnk=1
for i in range(0,limit):
    url1=url+str(i)
    
    page = urllib2.urlopen(url1)
    soup = BeautifulSoup(page)
    for link in soup.find_all('article'):
        l=link.get('about')
        
        lista.append(l)
        print(lnk)
        lnk+=1
        

dt={}
dt2={}
burl="https://www.reginamaria.ro/"
for link in lista:
    url2=burl+link
    page = urllib2.urlopen(url2)
    soup = BeautifulSoup(page)
    txt=soup.get_text()
    dt[link]=txt
    ntxt=''
    for par in soup.find_all('p'):
        ntxt=ntxt+par.get_text()+"\n" 
    dt2[link]=ntxt
    

ftxt=''
for k, v in dt2.items():
    ftxt=ftxt+v+"\n"
 

f = codecs.open(filecovrm, "w",encoding='utf-8')
f.write(ftxt)
f.close()

    
                        



