var ques = ['https://www.exam-mate.com/questions/458/9363/458_q_9363_2_1.png', 'https://www.exam-mate.com/questions/457/9289/457_q_9289_2_1.png', 'https://www.exam-mate.com/questions/458/9364/458_q_9364_3_1.png', 'https://www.exam-mate.com/questions/457/9290/457_q_9290_3_1.png', 'https://www.exam-mate.com/questions/456/9539/456_q_9539_1_1.png', 'https://www.exam-mate.com/questions/455/9440/455_q_9440_2_1.png', 'https://www.exam-mate.com/questions/455/9442/455_q_9442_3_1.png', 'https://www.exam-mate.com/questions/459/9643/459_q_9643_2_1.png', 'https://www.exam-mate.com/questions/5814/12918/5814_q_12918_5_1.png', 'https://www.exam-mate.com/questions/460/9778/460_q_9778_5_1.png', 'https://www.exam-mate.com/questions/462/9942/462_q_9942_2_1.png', 'https://www.exam-mate.com/questions/461/9855/461_q_9855_2_1.png', 'https://www.exam-mate.com/questions/462/9944/462_q_9944_3_1.png', 'https://www.exam-mate.com/questions/461/9859/461_q_9859_3_1.png', 'https://www.exam-mate.com/questions/463/10049/463_q_10049_4_1.png', 'https://www.exam-mate.com/questions/463/10052/463_q_10052_5_1.png', 'https://www.exam-mate.com/questions/464/10123/464_q_10123_2_1.png', 'https://www.exam-mate.com/questions/464/10124/464_q_10124_3_1.png', 'https://www.exam-mate.com/questions/466/10308/466_q_10308_4_1.png', 'https://www.exam-mate.com/questions/465/10205/465_q_10205_4_1.png', 'https://www.exam-mate.com/questions/466/10310/466_q_10310_5_1.png', 'https://www.exam-mate.com/questions/465/10206/465_q_10206_5_1.png', 'https://www.exam-mate.com/questions/467/10405/467_q_10405_2_1.png', 'https://www.exam-mate.com/questions/508/10557/508_q_10557_3_1.png', 'https://www.exam-mate.com/questions/467/10407/467_q_10407_3_1.png', 'https://www.exam-mate.com/questions/469/10680/469_q_10680_4_1.png', 'https://www.exam-mate.com/questions/508/10562/508_q_10562_5_1.png', 'https://www.exam-mate.com/questions/469/10683/469_q_10683_5_1.png', 'https://www.exam-mate.com/questions/471/10883/471_q_10883_2_1.png', 'https://www.exam-mate.com/questions/470/10763/470_q_10763_2_1.png', 'https://www.exam-mate.com/questions/473/10986/473_q_10986_3_1.png', 'https://www.exam-mate.com/questions/476/11221/476_q_11221_2_1.png', 'https://www.exam-mate.com/questions/475/11172/475_q_11172_2_1.png', 'https://www.exam-mate.com/questions/474/11122/474_q_11122_2_1.png', 'https://www.exam-mate.com/questions/475/11173/475_q_11173_3_1.png', 'https://www.exam-mate.com/questions/474/11123/474_q_11123_3_1.png', 'https://www.exam-mate.com/questions/479/11348/479_q_11348_3_1.png', 'https://www.exam-mate.com/questions/478/11279/478_q_11279_3_1.png', 'https://www.exam-mate.com/questions/480/11420/480_q_11420_4_1.png', 'https://www.exam-mate.com/questions/483/11585/483_q_11585_2_1.png', 'https://www.exam-mate.com/questions/483/11586/483_q_11586_3_1.png', 'https://www.exam-mate.com/questions/482/11528/482_q_11528_3_1.png', 'https://www.exam-mate.com/questions/481/11474/481_q_11474_3_1.png', 'https://www.exam-mate.com/questions/483/11591/483_q_11591_8_1.png', 'https://www.exam-mate.com/questions/481/11482/481_q_11482_8_1.png', 'https://www.exam-mate.com/questions/482/11534/482_q_11534_9_1.png', 'https://www.exam-mate.com/questions/486/11786/486_q_11786_2_1.png', 'https://www.exam-mate.com/questions/485/11640/485_q_11640_2_1.png', 'https://www.exam-mate.com/questions/486/11787/486_q_11787_3_1.png', 'https://www.exam-mate.com/questions/485/11642/485_q_11642_3_1.png', 'https://www.exam-mate.com/questions/484/11708/484_q_11708_3_1.png', 'https://www.exam-mate.com/questions/488/11914/488_q_11914_1_1.png', 'https://www.exam-mate.com/questions/489/11986/489_q_11986_2_1.png', 'https://www.exam-mate.com/questions/487/11836/487_q_11836_2_1.png', 'https://www.exam-mate.com/questions/489/11987/489_q_11987_3_1.png', 'https://www.exam-mate.com/questions/488/11920/488_q_11920_3_1.png', 'https://www.exam-mate.com/questions/487/11838/487_q_11838_3_1.png', 'https://www.exam-mate.com/questions/492/12186/492_q_12186_2_1.png', 'https://www.exam-mate.com/questions/539/12781/539_q_12781_2_1.png', 'https://www.exam-mate.com/questions/538/12835/538_q_12835_2_1.png', 'https://www.exam-mate.com/questions/537/12861/537_q_12861_2_1.png', 'https://www.exam-mate.com/questions/539/12782/539_q_12782_3_1.png', 'https://www.exam-mate.com/questions/538/12836/538_q_12836_3_1.png', 'https://www.exam-mate.com/questions/537/12862/537_q_12862_3_1.png', 'https://www.exam-mate.com/questions/5553/7931/5553_q_7931_2_1.png', 'https://www.exam-mate.com/questions/5554/8019/5554_q_8019_2_1.png', 'https://www.exam-mate.com/questions/5555/8059/5555_q_8059_2_1.png', 'https://www.exam-mate.com/questions/5553/7934/5553_q_7934_3_1.png', 'https://www.exam-mate.com/questions/5554/8020/5554_q_8020_3_1.png', 'https://www.exam-mate.com/questions/5555/8060/5555_q_8060_3_1.png', 'https://www.exam-mate.com/questions/7399/42433/7399_q_42433_2_1.png', 'https://www.exam-mate.com/questions/7400/42473/7400_q_42473_2_1.png', 'https://www.exam-mate.com/questions/7401/42513/7401_q_42513_2_1.png', 'https://www.exam-mate.com/questions/7399/42434/7399_q_42434_3_1.png', 'https://www.exam-mate.com/questions/7400/42474/7400_q_42474_3_1.png', 'https://www.exam-mate.com/questions/7401/42514/7401_q_42514_3_1.png', 'https://www.exam-mate.com/questions/7399/42451/7399_q_42451_20_1.png', 'https://www.exam-mate.com/questions/7400/42491/7400_q_42491_20_1.png', 'https://www.exam-mate.com/questions/7401/42531/7401_q_42531_20_1.png', 'https://www.exam-mate.com/questions/13986/48436/13986_q_48436_1_1.png', 'https://www.exam-mate.com/questions/13984/48337/13984_q_48337_2_1.png', 'https://www.exam-mate.com/questions/13985/48397/13985_q_48397_2_1.png', 'https://www.exam-mate.com/questions/13986/48437/13986_q_48437_2_1.png', 'https://www.exam-mate.com/questions/13984/48338/13984_q_48338_3_1.png', 'https://www.exam-mate.com/questions/13985/48398/13985_q_48398_3_1.png', 'https://www.exam-mate.com/questions/13986/48438/13986_q_48438_3_1.png', 'https://www.exam-mate.com/questions/13986/48439/13986_q_48439_4_1.png', 'https://www.exam-mate.com/questions/13984/48368/13984_q_48368_29_1.png', 'https://www.exam-mate.com/questions/13985/48424/13985_q_48424_29_1.png', 'https://www.exam-mate.com/questions/13986/48464/13986_q_48464_29_1.png', 'https://www.exam-mate.com/questions/17671/51651/17671_q_51651_2_1.png', 'https://www.exam-mate.com/questions/17672/51691/17672_q_51691_2_1.png', 'https://www.exam-mate.com/questions/17673/51731/17673_q_51731_2_1.png', 'https://www.exam-mate.com/questions/17671/51652/17671_q_51652_3_1.png', 'https://www.exam-mate.com/questions/17672/51692/17672_q_51692_3_1.png', 'https://www.exam-mate.com/questions/17673/51732/17673_q_51732_3_1.png', 'https://www.exam-mate.com/questions/19779/54604/19779_q_54604_2_1.png', 'https://www.exam-mate.com/questions/19780/54644/19780_q_54644_2_1.png', 'https://www.exam-mate.com/questions/19781/54684/19781_q_54684_2_1.png', 'https://www.exam-mate.com/questions/20639/57121/20639_q_57121_2_1.png', 'https://www.exam-mate.com/questions/20640/57161/20640_q_57161_2_1.png', 'https://www.exam-mate.com/questions/20641/57201/20641_q_57201_2_1.png', 'https://www.exam-mate.com/questions/20639/57122/20639_q_57122_3_1.png', 'https://www.exam-mate.com/questions/20640/57162/20640_q_57162_3_1.png', 'https://www.exam-mate.com/questions/20641/57202/20641_q_57202_3_1.png', 'https://www.exam-mate.com/questions/21417/62412/21417_q_62412_3_1.png', 'https://www.exam-mate.com/questions/21418/62492/21418_q_62492_3_1.png', 'https://www.exam-mate.com/questions/21419/62559/21419_q_62559_3_1.png'];
var answ = [' D', ' B', ' B', ' D', ' D', ' C', ' D', ' A', ' A', ' A', ' A', ' B', ' B', ' A', ' A', ' B', ' A', ' B', ' A', ' A', ' B', ' B', ' D', ' D', ' D', ' D', ' D', ' D', ' D', ' D', ' D', ' B', ' C', ' B', ' B', ' C', ' B', ' C', ' C', ' C', ' A', ' A', ' A', ' A', ' A', ' A', ' C', ' A', ' A', ' C', ' B', ' D', ' C', ' A', ' D', ' A', ' D', ' B', ' C', ' C', ' A', ' D', ' B', ' D', ' B', ' B', ' B', ' C', ' C', ' D', ' C', ' C', ' D', ' D', ' A', ' B', ' D', ' A', ' D', ' C', ' C', ' B', ' C', ' B', ' B', ' C', ' D', ' C', ' C', ' C', ' D', ' C', ' D', ' A', ' D', ' A', ' A', ' A', ' A', ' A', ' C', ' C', ' B', ' C', ' B', ' C', ' C', ' C'];
var title = ['(0620-S 2009-Paper 2/2-Q2)', '(0620-S 2009-Paper 2/1-Q2)', '(0620-S 2009-Paper 2/2-Q3)', '(0620-S 2009-Paper 2/1-Q3)', '(0620-W 2009-Paper 2/2-Q1)', '(0620-W 2009-Paper 2/1-Q2)', '(0620-W 2009-Paper 2/1-Q3)', '(0620-S 2010-Paper 2/1-Q2)', '(0620-S 2010-Paper 2/3-Q5)', '(0620-S 2010-Paper 2/2-Q5)', '(0620-W 2010-Paper 2/2-Q2)', '(0620-W 2010-Paper 2/1-Q2)', '(0620-W 2010-Paper 2/2-Q3)', '(0620-W 2010-Paper 2/1-Q3)', '(0620-W 2010-Paper 2/3-Q4)', '(0620-W 2010-Paper 2/3-Q5)', '(0620-S 2011-Paper 2/1-Q2)', '(0620-S 2011-Paper 2/1-Q3)', '(0620-S 2011-Paper 2/3-Q4)', '(0620-S 2011-Paper 2/2-Q4)', '(0620-S 2011-Paper 2/3-Q5)', '(0620-S 2011-Paper 2/2-Q5)', '(0620-W 2011-Paper 2/1-Q2)', '(0620-W 2011-Paper 2/2-Q3)', '(0620-W 2011-Paper 2/1-Q3)', '(0620-W 2011-Paper 2/3-Q4)', '(0620-W 2011-Paper 2/2-Q5)', '(0620-W 2011-Paper 2/3-Q5)', '(0620-S 2012-Paper 2/2-Q2)', '(0620-S 2012-Paper 2/1-Q2)', '(0620-S 2012-Paper 2/3-Q3)', '(0620-W 2012-Paper 2/3-Q2)', '(0620-W 2012-Paper 2/2-Q2)', '(0620-W 2012-Paper 2/1-Q2)', '(0620-W 2012-Paper 2/2-Q3)', '(0620-W 2012-Paper 2/1-Q3)', '(0620-S 2013-Paper 2/2-Q3)', '(0620-S 2013-Paper 2/1-Q3)', '(0620-S 2013-Paper 2/3-Q4)', '(0620-W 2013-Paper 2/3-Q2)', '(0620-W 2013-Paper 2/3-Q3)', '(0620-W 2013-Paper 2/2-Q3)', '(0620-W 2013-Paper 2/1-Q3)', '(0620-W 2013-Paper 2/3-Q8)', '(0620-W 2013-Paper 2/1-Q8)', '(0620-W 2013-Paper 2/2-Q9)', '(0620-S 2014-Paper 2/3-Q2)', '(0620-S 2014-Paper 2/1-Q2)', '(0620-S 2014-Paper 2/3-Q3)', '(0620-S 2014-Paper 2/1-Q3)', '(0620-S 2014-Paper 2/2-Q3)', '(0620-W 2014-Paper 2/2-Q1)', '(0620-W 2014-Paper 2/3-Q2)', '(0620-W 2014-Paper 2/1-Q2)', '(0620-W 2014-Paper 2/3-Q3)', '(0620-W 2014-Paper 2/2-Q3)', '(0620-W 2014-Paper 2/1-Q3)', '(0620-S 2015-Paper 2/3-Q2)', '(0620-S 2016-Paper 2/1-Q2)', '(0620-S 2016-Paper 2/3-Q2)', '(0620-S 2016-Paper 2/2-Q2)', '(0620-S 2016-Paper 2/1-Q3)', '(0620-S 2016-Paper 2/3-Q3)', '(0620-S 2016-Paper 2/2-Q3)', '(0620-W 2016-Paper 2/1-Q2)', '(0620-W 2016-Paper 2/2-Q2)', '(0620-W 2016-Paper 2/3-Q2)', '(0620-W 2016-Paper 2/1-Q3)', '(0620-W 2016-Paper 2/2-Q3)', '(0620-W 2016-Paper 2/3-Q3)', '(0620-S 2017-Paper 2/1-Q2)', '(0620-S 2017-Paper 2/2-Q2)', '(0620-S 2017-Paper 2/3-Q2)', '(0620-S 2017-Paper 2/1-Q3)', '(0620-S 2017-Paper 2/2-Q3)', '(0620-S 2017-Paper 2/3-Q3)', '(0620-S 2017-Paper 2/1-Q20)', '(0620-S 2017-Paper 2/2-Q20)', '(0620-S 2017-Paper 2/3-Q20)', '(0620-W 2017-Paper 2/3-Q1)', '(0620-W 2017-Paper 2/1-Q2)', '(0620-W 2017-Paper 2/2-Q2)', '(0620-W 2017-Paper 2/3-Q2)', '(0620-W 2017-Paper 2/1-Q3)', '(0620-W 2017-Paper 2/2-Q3)', '(0620-W 2017-Paper 2/3-Q3)', '(0620-W 2017-Paper 2/3-Q4)', '(0620-W 2017-Paper 2/1-Q29)', '(0620-W 2017-Paper 2/2-Q29)', '(0620-W 2017-Paper 2/3-Q29)', '(0620-S 2018-Paper 2/1-Q2)', '(0620-S 2018-Paper 2/2-Q2)', '(0620-S 2018-Paper 2/3-Q2)', '(0620-S 2018-Paper 2/1-Q3)', '(0620-S 2018-Paper 2/2-Q3)', '(0620-S 2018-Paper 2/3-Q3)', '(0620-W 2018-Paper 2/1-Q2)', '(0620-W 2018-Paper 2/2-Q2)', '(0620-W 2018-Paper 2/3-Q2)', '(0620-S 2019-Paper 2/1-Q2)', '(0620-S 2019-Paper 2/2-Q2)', '(0620-S 2019-Paper 2/3-Q2)', '(0620-S 2019-Paper 2/1-Q3)', '(0620-S 2019-Paper 2/2-Q3)', '(0620-S 2019-Paper 2/3-Q3)', '(0620-W 2019-Paper 2/1-Q3)', '(0620-W 2019-Paper 2/2-Q3)', '(0620-W 2019-Paper 2/3-Q3)'];
