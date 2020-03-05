from bs4 import BeautifulSoup
import urllib.request
import requests
from requests import Session

from requests.packages.urllib3 import add_stderr_logger
import urllib
from urllib.error import HTTPError
from urllib.request import urlopen
import re, random, datetime
random.seed(datetime.datetime.now())

add_stderr_logger()

session = requests.Session()
per_session = session.post("https://www.exam-mate.com/reguser/checklogin", 
data={'email':'lawliet5145@gmail.com', 'password':'kAmehAmehA1!'})
    
NewArr=[]
arr=[]
arrUrl=[]
lenOfArr = []
AlasOfLast = []
url = "https://www.exam-mate.com/topicalpastpapers/?cat=3&subject=16&years=&seasons=&chapter=71&paper=&unit=&zone=&level=&offset=0"
ins = url.split("=")
eqn = "="
for s in range(0,340,20):
    ins[-1] = str(s)
    j = eqn.join(ins)
    arrUrl.append(j)
CountStr = 0
counting = 0
count = 0
while (count < len(arrUrl)):
    """ response = urllib.request.urlopen(arrUrl[count]) """
    content = BeautifulSoup(session.get(arrUrl[count]).content , "html.parser") # Use the session to get url
    with open('try.html', "w", encoding="utf-8") as f:
        f.write(str(content.find_all('a', class_="form-control")))
    if (content.find_all('a', class_="qabtn") == None):
        break
    else:
        for anc in content.find_all('a', class_="qabtn"):
            splitting = anc['onclick'].split(",")[1]
            spli = splitting.translate({ord("'"): None})
            if len(spli) > 2:
                adding = "https://www.exam-mate.com"+spli
                spli = adding.replace(" ","")
            arr.append(spli)

        for tit in content.find_all("div" , class_="question"):
            for title in tit.find_all("div"):
                AlasOfLast.append(title.string)

        while (CountStr < len(AlasOfLast)):
            if (AlasOfLast[CountStr] == None):
                del AlasOfLast[CountStr]
            CountStr += 1

        while (counting < len(AlasOfLast)):
            if (counting % 2 == 0):
                lenOfArr.append(AlasOfLast[counting])
            counting += 1
                
        count += 1


for n in range(len(lenOfArr)) :
    NewArr.append(lenOfArr[n].strip())

ques = []
answ = []

for j in range(len(arr)):
    if (j % 2) == 0:
        ques.append(arr[j])
            

for i in range(len(arr)):
    if (i % 2) == 1:
        answ.append(arr[i])

f = open("hello.py", "w")
f.write("ques = {}\n".format(ques))
f.close
f = open("hello.py", "a")
f.write("answ = {}\n".format(answ))
f.close
f = open("hello.py", "a")
f.write("title = {}\n".format(NewArr))
f.close

print('Questions Answers Titles:',len(ques),len(answ),len(NewArr))

""" from PIL import Image
from io import BytesIO

outmage = 0
widthImg = []
while (outmage < len(ques)):
    file = BytesIO(urllib.request.urlopen(ques[outmage]).read())
    ima = Image.open(file)
    width , height = ima.size
    widthImg.append(width)
    outmage += 1

ansmage = 0
answidth = []
while (ansmage < len(answ)):
    if (len(answ[ansmage]) < 5):
        None
    else:
        fileans = BytesIO(urllib.request.urlopen(answ[ansmage]).read())
        imans = Image.open(fileans)
        widthans , heightans = imans.size
        answidth.append(widthans)
        ansmage += 1

f = open("hello.py", "a")
f.write("widthQues = {}\n".format(widthImg))
f.close
f = open("hello.py", "a")
f.write("widthAnsw = {}\n".format(answidth))
f.close """
