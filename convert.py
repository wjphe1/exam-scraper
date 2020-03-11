import pdfkit
path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# REMEMBER TO CHANGE THE CHAPTER NUMBER 
# Paper 1
pdfkit.from_file("question1.html","pdf/PhyAlvlC_Q_P1CH26.pdf", configuration=config)
""" pdfkit.from_file("answer1.html","pdf/PhyAlvlC_A_P1CH26.pdf", configuration=config) """
# Paper 2
""" pdfkit.from_file("question2.html","pdf/PhyAlvlC_Q_P2CH26.pdf", configuration=config)
pdfkit.from_file("answer2.html","pdf/PhyAlvlC_A_P2CH26.pdf", configuration=config) """
# Paper 3
""" pdfkit.from_file("question3.html","pdf/PhyAlvlC_Q_P3CH26.pdf", configuration=config)
pdfkit.from_file("answer3.html","pdf/PhyAlvlC_A_P3CH26.pdf", configuration=config) """
# Paper 4
""" pdfkit.from_file("question4.html","pdf/PhyAlvlC_Q_P4CH26.pdf", configuration=config)
pdfkit.from_file("answer4.html","pdf/PhyAlvlC_A_P4CH26.pdf", configuration=config) """
# Paper 5
""" pdfkit.from_file("question5.html","pdf/PhyAlvlC_Q_P5CH26.pdf", configuration=config)
pdfkit.from_file("answer5.html","pdf/PhyAlvlC_A_P5CH26.pdf", configuration=config) """
# Paper 6
""" pdfkit.from_file("question6.html","pdf/PhyAlvlC_Q_P6CH26.pdf", configuration=config)
pdfkit.from_file("answer6.html","pdf/PhyAlvlC_A_P6CH26.pdf", configuration=config) """