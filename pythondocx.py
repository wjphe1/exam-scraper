from docx import Document
from docx.shared import Inches
from docx.oxml.shared import OxmlElement
import glob
import os

# Prevent table rows from breaking with page layout
def prevent_document_break(document):
    """https://github.com/python-openxml/python-docx/issues/245#event-621236139
       Globally prevent table cells from splitting across pages.
    """
    tags = document.element.xpath('//w:tr')
    rows = len(tags)
    for row in range(0, rows):
        tag = tags[row]  # Specify which <w:r> tag you want
        child = OxmlElement('w:cantSplit')  # Create arbitrary tag
        tag.append(child)  # Append in the new tag

# Scale the picture width ONLY when it is exceeding the docx page
def scale_picture(picture, new_width):
    aspect_ratio = float(picture.height) / float(picture.width)
    picture.height = int(aspect_ratio * new_width)
    picture.width = new_width

# Loop starts
for chap in range(21): ### 1. CHANGE CHAPTER NUMBER FOR THAT TOPIC

    document = Document()

    paragraph_format = document.styles['Normal'].paragraph_format
    paragraph_format.line_spacing = 1.5

    pic = []
    #pic = [f for f in glob.glob("png/Biology/Paper1/CH"+str(chap+1)+"/Question/*.png")] ### CHANGE PAPER NUMBER & QUESTION/ANSWER
    #pic = [f for f in glob.glob("png/Biology/Paper1/CH"+str(chap+1)+"/Answer/*.png")]
    pic = [h for h in glob.glob("png/Biology/Paper1/CH"+str(chap+1)+"/Answer/*.txt")] ### FOR TXT

    name = []
    for g in range(len(pic)):
        name.append(pic[g][33:-5])

    ans = []
    for j in range(len(pic)):
        with open(pic[j], 'r') as f:
            x = f.readlines()
            ans.append(x)

    if len(pic) == len(name):
        print('YES! CH{} has {} pictures' .format(chap+1, len(pic)))

    # CREATE TABLE FOR WRITING PNG FILES
    """ table = document.add_table(rows=0, cols=1)
    table.style = 'Table Grid'
    table.autofit = True

    for i in range(len(pic)):
        row_cells = table.add_row().cells
        paragraph = row_cells[0].paragraphs[0]
        run = paragraph.insert_paragraph_before(name[i]+'\n', style='List Number').add_run()
        picture = run.add_picture(pic[i])
        if picture.width > Inches(5.5):
            scale_picture(picture, Inches(5.5)) """
    
    # CREATE TABLE FOR WRITING TXT FILES
    table = document.add_table(rows=0, cols=5)
    table.style = 'Table Grid'
    table.autofit = True

    colcount = 0
    row_cells = table.add_row().cells
    for i in range(len(pic)):
        paragraph = row_cells[colcount].paragraphs[0]
        run = paragraph.insert_paragraph_before(ans[i], style='List Number').add_run()
        colcount = colcount + 1
        if colcount == 5:
            colcount = 0
            row_cells = table.add_row().cells
   

    # PREVENT BREAK
    prevent_document_break(document)

    # SAVE THE FILE
    document.save('docx/Biology/Paper1/A_P1CH'+str(chap+1)+'.docx') ### CHANGE PAPER NUMBER