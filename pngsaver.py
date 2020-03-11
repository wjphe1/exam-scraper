import urllib.request

ques = ['https://www.exam-mate.com/questions/1264/2771/1264_q_2771_17_1.png', 'https://www.exam-mate.com/questions/1394/4424/1394_q_4424_7_1.png', 'https://www.exam-mate.com/questions/1277/3146/1277_q_3146_7_1.png', 'https://www.exam-mate.com/questions/1294/3224/1294_q_3224_19_1.png', 'https://www.exam-mate.com/questions/1405/4527/1405_q_4527_8_1.png', 'https://www.exam-mate.com/questions/3552/4590/3552_q_4590_3_1.png', 'https://www.exam-mate.com/questions/7465/41831/7465_q_41831_21_1.png', 'https://www.exam-mate.com/questions/14028/47767/14028_q_47767_19_1.png', 'https://www.exam-mate.com/questions/17643/51854/17643_q_51854_21_1.png', 'https://www.exam-mate.com/questions/19875/54937/19875_q_54937_1_1.png', 'https://www.exam-mate.com/questions/20673/56913/20673_q_56913_14_1.png', 'https://www.exam-mate.com/questions/20674/56945/20674_q_56945_22_1.png', 'https://www.exam-mate.com/questions/21407/62034/21407_q_62034_2_1.png']
answ = ['https://www.exam-mate.com/questions/1264/2771/1264_a_2771_17_1.png', 'https://www.exam-mate.com/questions/1394/4424/1394_a_4424_7_1.png', 'https://www.exam-mate.com/questions/1277/3146/1277_a_3146_7_1.png', 'https://www.exam-mate.com/questions/1294/3224/1294_a_3224_19_1.png', 'https://www.exam-mate.com/questions/1405/4527/1405_a_4527_8_1.png', 'https://www.exam-mate.com/questions/3552/4590/3552_a_4590_3_1.png', 'https://www.exam-mate.com/questions/7465/41831/7465_a_41831_21_1.png', 'https://www.exam-mate.com/questions/14028/47767/14028_a_47767_19_1.png', 'https://www.exam-mate.com/questions/17643/51854/17643_a_51854_21_1.png', 'https://www.exam-mate.com/questions/19875/54937/19875_a_54937_1_1.png', 'https://www.exam-mate.com/questions/20673/56913/20673_a_56913_14_1.png', 'https://www.exam-mate.com/questions/20674/56945/20674_a_56945_22_1.png', 'https://www.exam-mate.com/questions/21407/62034/21407_a_62034_2_1.png']
title = ['(0580-S 2013-Paper 1/3-Q17)', '(0580-W 2013-Paper 3/3-Q7)', '(0580-S 2014-Paper 1/3-Q7)', '(0580-W 2014-Paper 1/1-Q19)', '(0580-W 2014-Paper 3/3-Q8)', '(0580-W 2015-Paper 3/2-Q3)', '(0580-S 2017-Paper 1/1-Q21)', '(0580-W 2017-Paper 1/2-Q19)', '(0580-S 2018-Paper 1/1-Q21)', '(0580-W 2018-Paper 3/2-Q1)', '(0580-S 2019-Paper 1/2-Q14)', '(0580-S 2019-Paper 1/3-Q22)', '(0580-W 2019-Paper 3/1-Q2)']

#Question
ja = 0
for i in range(len(ques)):
    filename = title[i+ja].replace('/','-') + '.png'
    fpath = 'png/Mathematics/Paper'+filename[19]+'/CH50/Question/'
    urllib.request.urlretrieve(ques[i+ja], fpath+filename)
    print(i+1+ja, "-> Saved", fpath+filename)

# Answer
jo = 0
for i in range(len(answ)):

    if len(answ[i+jo]) == 2:
        filename = title[i+jo].replace('/','-')
        filename = filename.replace('Q','A')
        fpath = 'png/Mathematics/Paper'+filename[19]+'/CH50/Answer/'
        f = open(fpath+filename+".txt", "w")
        f.write(answ[i+jo])
        f.close
        print(i+1+jo, "-> Saved", fpath+filename+".txt")
    else:
        filename = title[i+jo].replace('/','-') + '.png'
        filename = filename.replace('Q','A')
        fpath = 'png/Mathematics/Paper'+filename[19]+'/CH50/Answer/'
        urllib.request.urlretrieve(answ[i+jo], fpath+filename)
        print(i+1+jo, "-> Saved", fpath+filename)