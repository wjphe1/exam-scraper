import urllib.request
from hello import * 
import time

CH_count = 1

#Question
""" titlenum = 0
for i in range(len(quest)):
    time.sleep(1)
    if len(quest[i]) > 25:
        if quest[i][-5] != '1':
            filename = NewArr[titlenum-1].replace('/','-') + '_' + quest[i][-5] + '.png'
            filename = filename.replace('(','').replace(')','')
            fpath = 'png/IB/Biology/'+ filename[19] +'L/Paper'+filename[35]+'/CH'+str(CH_count)+'/Question/'
            urllib.request.urlretrieve(quest[i], fpath+filename)
            print(i+1, "-> Saved", fpath+filename)
        else:
            filename = NewArr[titlenum].replace('/','-') + '.png'
            filename = filename.replace('(','').replace(')','')
            fpath = 'png/IB/Biology/'+ filename[19] +'L/Paper'+filename[35]+'/CH'+str(CH_count)+'/Question/'
            titlenum = titlenum + 1
            urllib.request.urlretrieve(quest[i], fpath+filename)
            print(i+1, "-> Saved", fpath+filename)"""
            
# Answer
atitnum = 0
for i in range(len(answe)):
    time.sleep(1)
    if len(answe[i]) > 25: # THIS IS IMAGE SUBJECTIVE ANSWER
        if answe[i][-5] != '1':
            filename = NewArr[atitnum-1].replace('/','-') + '_' + answe[i][-5] + '.png'
            filename = filename.replace('Q','A').replace('(','').replace(')','')
            fpath = 'png/IB/Biology/'+ filename[19] +'L/Paper'+filename[35]+'/CH'+str(CH_count)+'/Answer/'
            urllib.request.urlretrieve(answe[i], fpath+filename)
            print(i+1, "-> Saved", fpath+filename)
        else:
            filename = NewArr[atitnum].replace('/','-') + '.png'
            filename = filename.replace('Q','A').replace('(','').replace(')','')
            fpath = 'png/IB/Biology/'+ filename[19] +'L/Paper'+filename[35]+'/CH'+str(CH_count)+'/Answer/'
            atitnum = atitnum + 1
            urllib.request.urlretrieve(answe[i], fpath+filename)
            print(i+1, "-> Saved", fpath+filename)
    else: # THIS IS TXT OBJECTIVE ANSWER
        filename = NewArr[atitnum].replace('/','-') + '.txt'
        filename = filename.replace('Q','A').replace('(','').replace(')','')
        fpath = 'png/IB/Biology/'+ filename[19] +'L/Paper'+filename[35]+'/CH'+str(CH_count)+'/Answer/'
        f = open(fpath + filename, "w")
        f.write(answe[i])
        f.close
        atitnum = atitnum + 1
        print(i+1, "-> Saved", fpath+filename)