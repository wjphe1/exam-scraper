import pdfkit
path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

""" pdfkit.from_file("question.html","pdf/addMath_Q_P1CH1.pdf", configuration=config) """
pdfkit.from_file("answer.html","pdf/addMath_A_P1CH1.pdf", configuration=config)