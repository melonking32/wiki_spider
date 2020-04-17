import urllib.request as ur
import urllib
from bs4 import BeautifulSoup
import xlrd
import os
import unicodedata
import requests
import numpy
import random
#urls='https://en.wikipedia.org/wiki/les_Escaldes'
UA=[]
Domain=[]
def Google_find(url):
    USER_AGENT =random.choice(UA)
    USER_AGENT=USER_AGENT[:len(USER_AGENT)-1]
    print(USER_AGENT)
    #USER_AGENT="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/12.0.702.0 Safari/534.24"
    #USER_AGENT="Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
    #print(USER_AGENT)
    #USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    headers={"user-agent":USER_AGENT}
    #print(url)
    re =requests.get(url,headers=headers)
    if re.status_code == 200:
        soup = BeautifulSoup(re.content, "html.parser")
        #print(soup)
        results = []
        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                if anchors[0]['href'][:20]=="https://en.wikipedia":
                    print(anchors[0]['href'])
                    return anchors[0]['href']
def get_supplement(urls):   #功能和get_information一样，不过这个是获取谷歌搜索出来的网址的信息
    kk=1
    response=None
    try:
        response=ur.urlopen(urls)
    except ur.URLError as e:
        kk+=1
    if response!=None:
        soup=BeautifulSoup(response.read(),"html.parser",from_encoding="utf-8")
        content=soup.find("table",class_="infobox geography vcard")
        if content!=None:
            tb=content.find_all("tr")
            k=0 
            x=0
            for i in range(len(tb)):
                if tb[i].find("th")!=None and tb[i].find("th").get_text()!=None and ((len(tb[i].find("th").get_text())==7 and tb[i].find("th").get_text()[0]=="A" and tb[i].find("th").get_text()[1]=="r" and tb[i].find("th").get_text()[2]=="e" and tb[i].find("th").get_text()[3]=="a")or(len(tb[i].find("th").get_text())==4 and tb[i].find("th").get_text()[0]=="A" and tb[i].find("th").get_text()[1]=="r" and tb[i].find("th").get_text()[2]=="e" and tb[i].find("th").get_text()[3]=="a")):
                    if tb[i].find("td"):
                        k=i
                    else:
                        k=i+1
                if tb[i].find("th")!=None and tb[i].find("th").get_text()!=None and len(tb[i].find("th").get_text())>=10 and tb[i].find("th").get_text()[0]=="P" and tb[i].find("th").get_text()[1]=="o" and tb[i].find("th").get_text()[2]=="p" and tb[i].find("th").get_text()[3]=="u":
                    if tb[i].find("td"):
                        x=i
                    else:
                        x=i+1   
            if k!=0:          
                print("Area:"+tb[k].find("td").get_text())
            else:               #维基百科对此城市的情况概括中没有关于面积的描述
                print("No information about the area can be found-2")
            if x!=0:    
                print("Population:"+tb[x].find("td").get_text())
            else:
                print("No information about the population can be found-2")
        else:
            print("No information about the population and the Area can be found-2")

def get_information(str):
    print("\n")
    print(str)
    urls="https://en.wikipedia.org/wiki/"+str
    urls=unicodedata.normalize('NFKD', urls).encode('ascii','ignore')
    kk=1
    response=None
    try:
        response=ur.urlopen(urls.decode())
    except ur.URLError as e:
        kk+=1
    if response!=None:
        soup=BeautifulSoup(response.read(),"html.parser",from_encoding="utf-8")
        content=soup.find("table",class_="infobox geography vcard")
        if content!=None:
            tb=content.find_all("tr")
            k=0 
            x=0
            for i in range(len(tb)):
                if tb[i].find("th")!=None and tb[i].find("th").get_text()!=None and ((len(tb[i].find("th").get_text())==7 and tb[i].find("th").get_text()[0]=="A" and tb[i].find("th").get_text()[1]=="r" and tb[i].find("th").get_text()[2]=="e" and tb[i].find("th").get_text()[3]=="a")or(len(tb[i].find("th").get_text())==4 and tb[i].find("th").get_text()[0]=="A" and tb[i].find("th").get_text()[1]=="r" and tb[i].find("th").get_text()[2]=="e" and tb[i].find("th").get_text()[3]=="a")):
                    if tb[i].find("td"):
                        k=i
                    else:
                        k=i+1
                if tb[i].find("th")!=None and tb[i].find("th").get_text()!=None and len(tb[i].find("th").get_text())>=10 and tb[i].find("th").get_text()[0]=="P" and tb[i].find("th").get_text()[1]=="o" and tb[i].find("th").get_text()[2]=="p" and tb[i].find("th").get_text()[3]=="u":
                    if tb[i].find("td"):
                        x=i
                    else:
                        x=i+1   
            if k!=0:          
                print("Area:"+tb[k].find("td").get_text())
            else:               #维基百科对此城市的情况概括中没有关于面积的描述
                print("No information about the area can be found")
            if x!=0:    
                print("Population:"+tb[x].find("td").get_text())
            else:
                print("No information about the population can be found")
        else:
            print("No information about the population and the Area can be found")
    else:
        mainurl =random.choice(Domain)
        mainurl=mainurl[:len(mainurl)-1]
        url_g= "https://"+mainurl+f"/search?q={str}"
        #url_g= f"https://www.google.ba/search?q={str}"
        #print(url_g)
        url_g=unicodedata.normalize('NFKD', url_g).encode('ascii','ignore')
        url2=Google_find(url_g.decode())
        if url2==None:
            print("Can not find this city in Google")
        else:
            #print(url2)
            get_supplement(url2)
    
#urls="https://en.wikipedia.org/wiki/Bāzār-e_Yakāwlang" 
if __name__ == "__main__":    
    filepath=os.path.join(os.path.dirname(__file__)+'/data.xlsx')
    datalist=xlrd.open_workbook(filepath)
    sheet=datalist.sheet_by_name('Sheet1')
    City_list=sheet.col_values(0,1)
    City=City_list[3:100]
    with open(os.path.dirname(__file__)+"/c-UA.txt", 'r') as f:
        UA=f.readlines()
    with open(os.path.dirname(__file__)+"/c-domain.txt", 'r') as dd:
        Domain=dd.readlines()
    for i in range(100):
        for j in range(len(City[i])):
            if City[i][j]==' ':
                City[i]=City[i][:j]+"_"+City[i][j+1:]
        get_information(City[i])
#Shibirghān