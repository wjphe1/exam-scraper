import urllib.request
from hello import ques, answ, title

#Question
ja = 0
for i in range(len(ques)):
    filename = title[i+ja].replace('/','-') + '.png'
    fpath = 'png/Biology/Paper1/CH1/Question/'
    urllib.request.urlretrieve(ques[i+ja], fpath+filename)
    print(i+1+ja, "-> Saved", fpath+filename)

# Answer
jo = 0
for i in range(len(answ)):

    if len(answ[i+jo]) == 2:
        filename = title[i+jo].replace('/','-')
        filename = filename.replace('Q','A')
        fpath = 'png/Biology/Paper1/CH1/Answer/'
        f = open(fpath+filename+".txt", "w")
        f.write(answ[i+jo])
        f.close
        print(i+1+jo, "-> Saved", fpath+filename+".txt")
    else:
        filename = title[i+jo].replace('/','-') + '.png'
        filename = filename.replace('Q','A')
        fpath = 'png/Biology/Paper1/CH1/Answer/'
        urllib.request.urlretrieve(answ[i+jo], fpath+filename)
        print(i+1+jo, "-> Saved", fpath+filename)