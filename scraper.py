#!/usr/bin/env python
# coding: utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date
import re

date1 = str(input("Enter your date in yyyy/mm/dd:"))
reason1= str(input("Enter your query:"))
reason1=reason1.lower()

year1,month1,day1 =map(int, date1.split('/'))

a= date(2001,1,1)
b=date(year1,month1,day1)
var=b-a
result=var.days + 36892
link="https://timesofindia.indiatimes.com/"+str(date1)+"/archivelist/year-"+str(year1)+",month-"+str(month1)+",starttime-"+str(result)+".cms"


html = urlopen(link)

bsObj= BeautifulSoup(html.read(),'lxml')

tags=bsObj.find_all('a')
lst=[]
for tag in tags:
    var1=tag.get('href')
    var2=tag.text
    var2=var2.lower()
    x=re.findall(reason1,var2)
    if(len(x)!=0):
        if("http://timesofindia.indiatimes.com/" or "https://timesofindia.indiatimes.com/" not in var1):
            var1="http://timesofindia.indiatimes.com/"+str(var1)
            lst.append(var1)
        else:
            lst.append(var1)
for i in lst:
    print(i)

