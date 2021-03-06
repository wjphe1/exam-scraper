from bs4 import BeautifulSoup
import urllib.request
import requests
from requests import Session
import time


from requests.packages.urllib3 import add_stderr_logger
import urllib
from urllib.error import HTTPError
from urllib.request import urlopen
import re, random, datetime
random.seed(datetime.datetime.now())

#add_stderr_logger()

session = requests.Session()
per_session = session.post("https://www.exam-mate.com/reguser/checklogin", 
data={'email':'lawliet5145@gmail.com', 'password':'kAmehAmehA1!'}, timeout=None)


chs=[328]  # 1. CHANGE THIS ARRAY TO ALL CHAPTER NUMBERS
CH_count = 1

current_paper = ''  # 2. CHANGE THE PAPER NUMBER


for x in chs:    
    NewArr=[]
    arr=[]
    arrUrl=[]
    lenOfArr = []
    AlasOfLast = []
    url = "https://www.exam-mate.com/topicalpastpapers/?cat=7&subject=75&years=&seasons=&chapter="+ str(x) +"&paper="+ current_paper +"&zone=&offset=0"
    ins = url.split("=")                               #  ^^^^^^^^^^ 3. CHANGE THIS URL CAT=??? and subject=??? 
    eqn = "="
    for s in range(0,400,20):   # 4. CHANGE THE RANGE FROM TO TOTAL QUESTION NUMBER, X -> range(0, X, 20)
        ins[-1] = str(s)
        j = eqn.join(ins)
        arrUrl.append(j)
    CountStr = 0
    counting = 0
    count = 0

    try:
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
                    if len(spli) > 15:  # add more to prevent treating some long objective answer as url strings
                        adding = "https://www.exam-mate.com"+spli
                        spli = adding.replace(" ","")
                    arr.append(spli)

                for tit in content.find_all("div" , class_="question"):
                    for title in tit.find_all("div"):
                        if "(" in title.find(text=True, recursive=False):                 # For IB DIPLOMA
                            AlasOfLast.append(title.find(text=True, recursive=False))     # For IB DIPLOMA
                        #AlasOfLast.append(title.string)                                   # For Other Papers

                while (CountStr < len(AlasOfLast)):
                    if (AlasOfLast[CountStr] == None):
                        del AlasOfLast[CountStr]
                    CountStr += 1

                while (counting < len(AlasOfLast)):
                    if (counting % 2 == 0):
                        lenOfArr.append(AlasOfLast[counting])
                    counting += 1
                        
                count += 1

        for n in range(len(AlasOfLast)) :            # For IB DIPLOMA
            NewArr.append(AlasOfLast[n].strip())     # For IB DIPLOMA
        #for n in range(len(lenOfArr)) :            # For Other Papers
            #NewArr.append(lenOfArr[n].strip())     # For Other Papers

    except:
        print("timeout or connection reset by peer")

    f = open("hello.py", "w")
    f.write("NewArr = {}\n".format(NewArr))
    f.close

    ques = []
    answ = []

    for j in range(len(arr)):
        if (j % 2) == 0:
            ques.append(arr[j])
                

    for i in range(len(arr)):
        if (i % 2) == 1:
            answ.append(arr[i])

        
    if len(ques)==len(answ)==len(NewArr):
        print('~\n~\n~\nNumber of Questions: {}\n'.format(len(NewArr)))

    quest = []
    answe = []
    try:
        for i in range(len(ques)):
            print('{} in {}'.format(i+1,len(ques)))
            for k in range(1,11):
                cont = ques[i].replace('_1.png',"_{k}.png".format(k=k)) if (ques[i].endswith("png")) else ques[i].replace('_1.jpg',"_{k}.jpg".format(k=k)) if (ques[i].endswith("jpg")) else ques[i].replace('_1.jpeg',"_{k}.jpeg".format(k=k))
                if (requests.get(cont).status_code == 200):
                    quest.append(cont)
                    print(cont)
                cant = answ[i].replace('_1.png',"_{k}.png".format(k=k)) if (answ[i].endswith("png")) else answ[i].replace('_1.jpg',"_{k}.jpg".format(k=k)) if (answ[i].endswith("jpg")) else answ[i].replace('_1.jpeg',"_{k}.jpeg".format(k=k)) if (answ[i].endswith('jpeg')) else answ[i]
                try:
                    if (answ[i].endswith("png") or answ[i].endswith("jpg") or answ[i].endswith("jpeg")):
                        if (requests.get(cant).status_code == 200):
                            answe.append(cant)
                            print(cant)
                        else:
                            pass
                            break
                    else:
                        answe.append(cant)
                        print(cant)
                        break
                except:
                    print("not image error")

            time.sleep(3)
    except:
        print("connection reset by peer or time out")

    print('~\n~\n~\nNumber of Questions: {}\nQuestion Images: {}\nAnswer Images: {}'.format(len(NewArr),len(quest),len(answe)))


    f = open("hello.py", "a")
    f.write("quest = {}\n".format(quest))
    f.close
    f = open("hello.py", "a")
    f.write("answe = {}\n".format(answe))
    f.close
    

    import urllib.request

    #Question
    titlenum = 0
    for i in range(len(quest)):
        time.sleep(1)
        if len(quest[i]) > 25:
            if quest[i][-5] != '1':
                filename = NewArr[titlenum-1].replace('/','-') + '_' + quest[i][-5] + '.png'
                filename = filename.replace('(','').replace(')','')
                fpath = 'png/IB/Biology/'+ filename[-10] +'L/Paper'+filename[18]+'/CH'+str(CH_count)+'/Question/'
                urllib.request.urlretrieve(quest[i], fpath+filename)
                print(i+1, "-> Saved", fpath+filename)
            else:
                filename = NewArr[titlenum].replace('/','-') + '.png'
                filename = filename.replace('(','').replace(')','')
                fpath = 'png/IB/Biology/'+ filename[-10] +'L/Paper'+filename[18]+'/CH'+str(CH_count)+'/Question/'
                titlenum = titlenum + 1
                urllib.request.urlretrieve(quest[i], fpath+filename)
                print(i+1, "-> Saved", fpath+filename)

    # Answer
    atitnum = 0
    for i in range(len(answe)):
        time.sleep(1)
        if len(answe[i]) > 25: # THIS IS IMAGE SUBJECTIVE ANSWER
            if answe[i][-5] != '1':
                filename = NewArr[atitnum-1].replace('/','-') + '_' + answe[i][-5] + '.png'
                filename = filename.replace('Q','A').replace('(','').replace(')','')
                fpath = 'png/IB/Biology/'+ filename[19] +'L/Paper'+filename[34]+'/CH'+str(CH_count)+'/Answer/'
                urllib.request.urlretrieve(answe[i], fpath+filename)
                print(i+1, "-> Saved", fpath+filename)
            else:
                filename = NewArr[atitnum].replace('/','-') + '.png'
                filename = filename.replace('Q','A').replace('(','').replace(')','')
                fpath = 'png/IB/Biology/'+ filename[19] +'L/Paper'+filename[34]+'/CH'+str(CH_count)+'/Answer/'
                atitnum = atitnum + 1
                urllib.request.urlretrieve(answe[i], fpath+filename)
                print(i+1, "-> Saved", fpath+filename)
        else: # THIS IS TXT OBJECTIVE ANSWER
            filename = NewArr[atitnum].replace('/','-') + '.txt'
            filename = filename.replace('Q','A').replace('(','').replace(')','')
            fpath = 'png/IB/Biology/'+ filename[19] +'L/Paper'+filename[34]+'/CH'+str(CH_count)+'/Answer/'
            f = open(fpath + filename, "w")
            f.write(answe[i])
            f.close
            atitnum = atitnum + 1
            print(i+1, "-> Saved", fpath+filename)
    
    CH_count = CH_count + 1
    


#print('{} Questions {} Answers {} Titles'.format(len(ques),len(answ),len(NewArr)))

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

#ques1R=[];ques2R=[];ques1=[];ques2=[];ques3H=[];ques4H=[];ques3HR=[];ques4HR=[]



""" i = 0
for i in range(len(ques)) :
    if (NewArr[i][19] == "1"):
        if (NewArr[i][20] == "R"):
            ques1R.append(ques[i])
        else:
            ques1.append(ques[i])
    elif (NewArr[i][19] == "2"):
        if (NewArr[i][20] == "R"):
            ques2R.append(ques[i])
        else:
            ques2.append(ques[i])
    elif (NewArr[i][19] == "3"):
        if (NewArr[i][21] == "R"):
            ques3HR.append(ques[i])
        else:
            ques3H.append(ques[i])
    elif (NewArr[i][19] == "4"):
        if (NewArr[i][21] == "R"):
            ques4HR.append(ques[i])
        else:
            ques4H.append(ques[i])
    elif (NewArr[i][19] == "5"):
        ques5.append(ques[i])
    elif (NewArr[i][19] == "6"):
        ques6.append(ques[i])
    elif (NewArr[i][19] == "7"):
        ques7.append(ques[i])
        
print('Paper 1F : ',len(ques1))
print('Paper 1FR: ',len(ques1R))
print('Paper 2F : ',len(ques2))
print('Paper 2FR: ',len(ques2R))
print('Paper 3H : ',len(ques3H))
print('Paper 3HR: ',len(ques3HR))
print('Paper 4H : ',len(ques4H))
print('Paper 4HR: ',len(ques4HR))
print('Total    : ',len(ques1)+len(ques2)+len(ques1R)+len(ques2R))
#+len(ques4)+len(ques5)+len(ques6)+len(ques7) """
