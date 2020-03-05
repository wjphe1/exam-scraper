var ques = ['https://www.exam-mate.com/questions/626/5770/626_q_5770_7_1.png', 'https://www.exam-mate.com/questions/629/5784/629_q_5784_1_1.png', 'https://www.exam-mate.com/questions/630/5801/630_q_5801_1_1.png', 'https://www.exam-mate.com/questions/629/5785/629_q_5785_2_1.png', 'https://www.exam-mate.com/questions/630/5802/630_q_5802_2_1.png', 'https://www.exam-mate.com/questions/631/5826/631_q_5826_7_1.png', 'https://www.exam-mate.com/questions/635/5902/635_q_5902_1_1.png', 'https://www.exam-mate.com/questions/636/5935/636_q_5935_1_1.png', 'https://www.exam-mate.com/questions/634/5879/634_q_5879_3_1.png', 'https://www.exam-mate.com/questions/640/6023/640_q_6023_1_1.png', 'https://www.exam-mate.com/questions/638/5964/638_q_5964_3_1.png', 'https://www.exam-mate.com/questions/638/5973/638_q_5973_6_1.png', 'https://www.exam-mate.com/questions/640/6031/640_q_6031_6_1.png', 'https://www.exam-mate.com/questions/642/6086/642_q_6086_1_1.png', 'https://www.exam-mate.com/questions/641/6067/641_q_6067_3_1.png', 'https://www.exam-mate.com/questions/648/6246/648_q_6246_1_1.png', 'https://www.exam-mate.com/questions/649/6271/649_q_6271_6_1.png', 'https://www.exam-mate.com/questions/652/6284/652_q_6284_1_1.png', 'https://www.exam-mate.com/questions/651/6279/651_q_6279_2_1.png', 'https://www.exam-mate.com/questions/653/6301/653_q_6301_1_1.png', 'https://www.exam-mate.com/questions/656/6349/656_q_6349_3_1.png', 'https://www.exam-mate.com/questions/656/6357/656_q_6357_6_1.png', 'https://www.exam-mate.com/questions/657/6370/657_q_6370_6_1.png', 'https://www.exam-mate.com/questions/659/6390/659_q_6390_1_1.png', 'https://www.exam-mate.com/questions/659/6392/659_q_6392_3_1.png', 'https://www.exam-mate.com/questions/662/6431/662_q_6431_2_1.png', 'https://www.exam-mate.com/questions/664/6475/664_q_6475_1_1.png', 'https://www.exam-mate.com/questions/5566/8572/5566_q_8572_1_1.png', 'https://www.exam-mate.com/questions/5567/8610/5567_q_8610_4_1.png', 'https://www.exam-mate.com/questions/7412/42600/7412_q_42600_1_1.png', 'https://www.exam-mate.com/questions/7414/42608/7414_q_42608_1_1.png', 'https://www.exam-mate.com/questions/7414/42610/7414_q_42610_3_1.png', 'https://www.exam-mate.com/questions/7412/42603/7412_q_42603_4_1.png', 'https://www.exam-mate.com/questions/13996/48526/13996_q_48526_1_1.png', 'https://www.exam-mate.com/questions/13998/48534/13998_q_48534_1_1.png', 'https://www.exam-mate.com/questions/17199/51822/17199_q_51822_1_1.png', 'https://www.exam-mate.com/questions/17200/51826/17200_q_51826_1_1.png', 'https://www.exam-mate.com/questions/17201/51830/17201_q_51830_1_1.png', 'https://www.exam-mate.com/questions/17201/51833/17201_q_51833_4_1.png', 'https://www.exam-mate.com/questions/19791/54773/19791_q_54773_1_1.png', 'https://www.exam-mate.com/questions/19793/54781/19793_q_54781_1_1.png', 'https://www.exam-mate.com/questions/19791/54776/19791_q_54776_4_1.png', 'https://www.exam-mate.com/questions/19793/54784/19793_q_54784_4_1.png', 'https://www.exam-mate.com/questions/20651/57291/20651_q_57291_1_1.png', 'https://www.exam-mate.com/questions/20653/57299/20653_q_57299_1_1.png', 'https://www.exam-mate.com/questions/21430/62687/21430_q_62687_4_1.png'];
var answ = ['https://www.exam-mate.com/questions/626/5770/626_a_5770_7_1.png', 'https://www.exam-mate.com/questions/629/5784/629_a_5784_1_1.png', 'https://www.exam-mate.com/questions/630/5801/630_a_5801_1_1.png', 'https://www.exam-mate.com/questions/629/5785/629_a_5785_2_1.png', 'https://www.exam-mate.com/questions/630/5802/630_a_5802_2_1.png', 'https://www.exam-mate.com/questions/631/5826/631_a_5826_7_1.png', 'https://www.exam-mate.com/questions/635/5902/635_a_5902_1_1.png', 'https://www.exam-mate.com/questions/636/5935/636_a_5935_1_1.png', 'https://www.exam-mate.com/questions/634/5879/634_a_5879_3_1.png', 'https://www.exam-mate.com/questions/640/6023/640_a_6023_1_1.png', 'https://www.exam-mate.com/questions/638/5964/638_a_5964_3_1.png', 'https://www.exam-mate.com/questions/638/5973/638_a_5973_6_1.png', 'https://www.exam-mate.com/questions/640/6031/640_a_6031_6_1.png', 'https://www.exam-mate.com/questions/642/6086/642_a_6086_1_1.png', 'https://www.exam-mate.com/questions/641/6067/641_a_6067_3_1.png', 'https://www.exam-mate.com/questions/648/6246/648_a_6246_1_1.png', 'https://www.exam-mate.com/questions/649/6271/649_a_6271_6_1.png', 'https://www.exam-mate.com/questions/652/6284/652_a_6284_1_1.png', 'https://www.exam-mate.com/questions/651/6279/651_a_6279_2_1.png', 'https://www.exam-mate.com/questions/653/6301/653_a_6301_1_1.png', 'https://www.exam-mate.com/questions/656/6349/656_a_6349_3_1.png', 'https://www.exam-mate.com/questions/656/6357/656_a_6357_6_1.png', 'https://www.exam-mate.com/questions/657/6370/657_a_6370_6_1.png', 'https://www.exam-mate.com/questions/659/6390/659_a_6390_1_1.png', 'https://www.exam-mate.com/questions/659/6392/659_a_6392_3_1.png', 'https://www.exam-mate.com/questions/662/6431/662_a_6431_2_1.png', 'https://www.exam-mate.com/questions/664/6475/664_a_6475_1_1.png', 'https://www.exam-mate.com/questions/5566/8572/5566_a_8572_1_1.png', 'https://www.exam-mate.com/questions/5567/8610/5567_a_8610_4_1.png', 'https://www.exam-mate.com/questions/7412/42600/7412_a_42600_1_1.png', 'https://www.exam-mate.com/questions/7414/42608/7414_a_42608_1_1.png', 'https://www.exam-mate.com/questions/7414/42610/7414_a_42610_3_1.png', 'https://www.exam-mate.com/questions/7412/42603/7412_a_42603_4_1.png', 'https://www.exam-mate.com/questions/13996/48526/13996_a_48526_1_1.png', 'https://www.exam-mate.com/questions/13998/48534/13998_a_48534_1_1.png', 'https://www.exam-mate.com/questions/17199/51822/17199_a_51822_1_1.png', 'https://www.exam-mate.com/questions/17200/51826/17200_a_51826_1_1.png', 'https://www.exam-mate.com/questions/17201/51830/17201_a_51830_1_1.png', 'https://www.exam-mate.com/questions/17201/51833/17201_a_51833_4_1.png', 'https://www.exam-mate.com/questions/19791/54773/19791_a_54773_1_1.png', 'https://www.exam-mate.com/questions/19793/54781/19793_a_54781_1_1.png', 'https://www.exam-mate.com/questions/19791/54776/19791_a_54776_4_1.png', 'https://www.exam-mate.com/questions/19793/54784/19793_a_54784_4_1.png', 'https://www.exam-mate.com/questions/20651/57291/20651_a_57291_1_1.png', 'https://www.exam-mate.com/questions/20653/57299/20653_a_57299_1_1.png', 'https://www.exam-mate.com/questions/21430/62687/21430_a_62687_4_1.png'];
var title = ['(0620-W 2009-Paper 6/1-Q7)', '(0620-S 2010-Paper 6/2-Q1)', '(0620-S 2010-Paper 6/3-Q1)', '(0620-S 2010-Paper 6/2-Q2)', '(0620-S 2010-Paper 6/3-Q2)', '(0620-W 2010-Paper 6/1-Q7)', '(0620-S 2011-Paper 6/2-Q1)', '(0620-S 2011-Paper 6/3-Q1)', '(0620-S 2011-Paper 6/1-Q3)', '(0620-W 2011-Paper 6/3-Q1)', '(0620-W 2011-Paper 6/1-Q3)', '(0620-W 2011-Paper 6/1-Q6)', '(0620-W 2011-Paper 6/3-Q6)', '(0620-S 2012-Paper 6/2-Q1)', '(0620-S 2012-Paper 6/1-Q3)', '(0620-S 2013-Paper 6/2-Q1)', '(0620-S 2013-Paper 6/3-Q6)', '(0620-W 2013-Paper 6/3-Q1)', '(0620-W 2013-Paper 6/2-Q2)', '(0620-S 2014-Paper 6/1-Q1)', '(0620-W 2014-Paper 6/1-Q3)', '(0620-W 2014-Paper 6/1-Q6)', '(0620-W 2014-Paper 6/2-Q6)', '(0620-S 2015-Paper 6/1-Q1)', '(0620-S 2015-Paper 6/1-Q3)', '(0620-W 2015-Paper 6/2-Q2)', '(0620-S 2016-Paper 6/1-Q1)', '(0620-W 2016-Paper 6/2-Q1)', '(0620-W 2016-Paper 6/3-Q4)', '(0620-S 2017-Paper 6/1-Q1)', '(0620-S 2017-Paper 6/3-Q1)', '(0620-S 2017-Paper 6/3-Q3)', '(0620-S 2017-Paper 6/1-Q4)', '(0620-W 2017-Paper 6/1-Q1)', '(0620-W 2017-Paper 6/3-Q1)', '(0620-S 2018-Paper 6/1-Q1)', '(0620-S 2018-Paper 6/2-Q1)', '(0620-S 2018-Paper 6/3-Q1)', '(0620-S 2018-Paper 6/3-Q4)', '(0620-W 2018-Paper 6/1-Q1)', '(0620-W 2018-Paper 6/3-Q1)', '(0620-W 2018-Paper 6/1-Q4)', '(0620-W 2018-Paper 6/3-Q4)', '(0620-S 2019-Paper 6/1-Q1)', '(0620-S 2019-Paper 6/3-Q1)', '(0620-W 2019-Paper 6/2-Q4)'];