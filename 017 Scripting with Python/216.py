from ast import Pass
import PyPDF2 as pdf
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+'\pdf\samplepdf_1.pdf', "rb") as file:
    # Open Reader and Rotate a page
    pdfreader = pdf.PdfFileReader(file)
    print(pdfreader.getNumPages())
    rotatedpage = pdfreader.getPage(0).rotateClockwise(90)

    # Open Writer and write the rotated page
    pdfwriter = pdf.PdfFileWriter()
    pdfwriter.addPage(rotatedpage)

    with open(dir_path+'\pdf\editedsamplepdf.pdf', 'wb') as newfile:
        pdfwriter.write(newfile)
