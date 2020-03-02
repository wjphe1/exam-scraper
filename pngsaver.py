import urllib.request

ques = ['https://www.exam-mate.com/questions/102/70/102_q_70_6_1.png', 'https://www.exam-mate.com/questions/103/79/103_q_79_4_1.png', 'https://www.exam-mate.com/questions/105/93/105_q_93_7_1.png', 'https://www.exam-mate.com/questions/106/105/106_q_105_7_1.png', 'https://www.exam-mate.com/questions/108/137/108_q_137_3_1.png', 'https://www.exam-mate.com/questions/110/453/110_q_453_1_1.png', 'https://www.exam-mate.com/questions/112/477/112_q_477_4_1.png', 'https://www.exam-mate.com/questions/118/272/118_q_272_1_1.png', 'https://www.exam-mate.com/questions/123/294/123_q_294_1_1.png', 'https://www.exam-mate.com/questions/125/320/125_q_320_4_1.png', 'https://www.exam-mate.com/questions/126/332/126_q_332_4_1.png', 'https://www.exam-mate.com/questions/128/354/128_q_354_3_1.png', 'https://www.exam-mate.com/questions/133/411/133_q_411_3_1.png', 'https://www.exam-mate.com/questions/139/540/139_q_540_1_1.png', 'https://www.exam-mate.com/questions/137/521/137_q_521_6_1.png', 'https://www.exam-mate.com/questions/138/533/138_q_533_6_1.png', 'https://www.exam-mate.com/questions/141/431/141_q_431_1_1.png', 'https://www.exam-mate.com/questions/5520/979/5520_q_979_1_1.png', 'https://www.exam-mate.com/questions/5521/990/5521_q_990_1_1.png', 'https://www.exam-mate.com/questions/7347/41753/7347_q_41753_1_1.png', 'https://www.exam-mate.com/questions/7348/41764/7348_q_41764_1_1.png', 'https://www.exam-mate.com/questions/13950/47239/13950_q_47239_1_1.png', 'https://www.exam-mate.com/questions/13951/47249/13951_q_47249_1_1.png', 'https://www.exam-mate.com/questions/20612/56514/20612_q_56514_1_1.png', 'https://www.exam-mate.com/questions/20613/56525/20613_q_56525_1_1.png', 'https://www.exam-mate.com/questions/20614/56536/20614_q_56536_1_1.png', 'https://www.exam-mate.com/questions/21395/61826/21395_q_61826_1_1.png', 'https://www.exam-mate.com/questions/21397/61849/21397_q_61849_1_1.png']
answ = ['https://www.exam-mate.com/questions/102/70/102_a_70_6_1.png', 'https://www.exam-mate.com/questions/103/79/103_a_79_4_1.png', 'https://www.exam-mate.com/questions/105/93/105_a_93_7_1.png', 'https://www.exam-mate.com/questions/106/105/106_a_105_7_1.png', 'https://www.exam-mate.com/questions/108/137/108_a_137_3_1.png', 'https://www.exam-mate.com/questions/110/453/110_a_453_1_1.png', 'https://www.exam-mate.com/questions/112/477/112_a_477_4_1.png', 'https://www.exam-mate.com/questions/118/272/118_a_272_1_1.png', 'https://www.exam-mate.com/questions/123/294/123_a_294_1_1.png', 'https://www.exam-mate.com/questions/125/320/125_a_320_4_1.png', 'https://www.exam-mate.com/questions/126/332/126_a_332_4_1.png', 'https://www.exam-mate.com/questions/128/354/128_a_354_3_1.png', 'https://www.exam-mate.com/questions/133/411/133_a_411_3_1.png', 'https://www.exam-mate.com/questions/139/540/139_a_540_1_1.png', 'https://www.exam-mate.com/questions/137/521/137_a_521_6_1.png', 'https://www.exam-mate.com/questions/138/533/138_a_533_6_1.png', 'https://www.exam-mate.com/questions/141/431/141_a_431_1_1.png', 'https://www.exam-mate.com/questions/5520/979/5520_a_979_1_1.png', 'https://www.exam-mate.com/questions/5521/990/5521_a_990_1_1.png', 'https://www.exam-mate.com/questions/7347/41753/7347_a_41753_1_1.png', 'https://www.exam-mate.com/questions/7348/41764/7348_a_41764_1_1.png', 'https://www.exam-mate.com/questions/13950/47239/13950_a_47239_1_1.png', 'https://www.exam-mate.com/questions/13951/47249/13951_a_47249_1_1.png', 'https://www.exam-mate.com/questions/20612/56514/20612_a_56514_1_1.png', 'https://www.exam-mate.com/questions/20613/56525/20613_a_56525_1_1.png', 'https://www.exam-mate.com/questions/20614/56536/20614_a_56536_1_1.png', 'https://www.exam-mate.com/questions/21395/61826/21395_a_61826_1_1.png', 'https://www.exam-mate.com/questions/21397/61849/21397_a_61849_1_1.png']
title = ['(0606-W 2009-Paper 1/1-Q6)', '(0606-S 2010-Paper 1/1-Q4)', '(0606-W 2010-Paper 1/1-Q7)', '(0606-W 2010-Paper 1/2-Q7)', '(0606-S 2011-Paper 1/1-Q3)', '(0606-W 2011-Paper 1/1-Q1)', '(0606-W 2011-Paper 1/3-Q4)', '(0606-W 2012-Paper 1/3-Q1)', '(0606-S 2013-Paper 1/2-Q1)', '(0606-W 2013-Paper 1/1-Q4)', '(0606-W 2013-Paper 1/2-Q4)', '(0606-S 2014-Paper 1/1-Q3)', '(0606-W 2014-Paper 1/3-Q3)', '(0606-W 2015-Paper 1/3-Q1)', '(0606-W 2015-Paper 1/1-Q6)', '(0606-W 2015-Paper 1/2-Q6)', '(0606-S 2016-Paper 1/2-Q1)', '(0606-W 2016-Paper 1/1-Q1)', '(0606-W 2016-Paper 1/2-Q1)', '(0606-S 2017-Paper 1/2-Q1)', '(0606-S 2017-Paper 1/3-Q1)', '(0606-W 2017-Paper 1/1-Q1)', '(0606-W 2017-Paper 1/2-Q1)', '(0606-S 2019-Paper 1/1-Q1)', '(0606-S 2019-Paper 1/2-Q1)', '(0606-S 2019-Paper 1/3-Q1)', '(0606-W 2019-Paper 1/1-Q1)', '(0606-W 2019-Paper 1/3-Q1)']

""" #Question
for i in range(len(ques)):
    filename = title[i].replace('/','-') + '.png'
    urllib.request.urlretrieve(ques[i], 'png/AddMath/Paper1/CH2/Question/'+filename)
    print(i+1, "-> Saved", filename) """


# Answer
for i in range(len(answ)):

    if len(answ[i]) == 2:
        filename = title[i].replace('/','-')
        filename = filename.replace('Q','A')
        f = open(filename+".txt", "w")
        f.write(answ[i])
        f.close
        print(i+1, "-> Saved", filename+".txt")
    else:
        filename = title[i].replace('/','-') + '.png'
        filename = filename.replace('Q','A')
        urllib.request.urlretrieve(answ[i], 'png/AddMath/Paper1/CH2/Answer/'+filename)
        print(i+1, "-> Saved", filename)