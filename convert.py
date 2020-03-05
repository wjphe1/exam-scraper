import pdfkit
path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# REMEMBER TO CHANGE THE CHAPTER NUMBER 

pdfkit.from_file("question1.html","pdf/Chem_Q_P1CH2.pdf", configuration=config)
pdfkit.from_file("answer1.html","pdf/Chem_A_P1CH2.pdf", configuration=config)

pdfkit.from_file("question2.html","pdf/Chem_Q_P2CH2.pdf", configuration=config)
pdfkit.from_file("answer2.html","pdf/Chem_A_P2CH2.pdf", configuration=config)

pdfkit.from_file("question3.html","pdf/Chem_Q_P3CH2.pdf", configuration=config)
pdfkit.from_file("answer3.html","pdf/Chem_A_P3CH2.pdf", configuration=config)

pdfkit.from_file("question4.html","pdf/Chem_Q_P4CH2.pdf", configuration=config)
pdfkit.from_file("answer4.html","pdf/Chem_A_P4CH2.pdf", configuration=config)

pdfkit.from_file("question5.html","pdf/Chem_Q_P5CH2.pdf", configuration=config)
pdfkit.from_file("answer5.html","pdf/Chem_A_P5CH2.pdf", configuration=config)

pdfkit.from_file("question6.html","pdf/Chem_Q_P6CH2.pdf", configuration=config)
pdfkit.from_file("answer6.html","pdf/Chem_A_P6CH2.pdf", configuration=config)