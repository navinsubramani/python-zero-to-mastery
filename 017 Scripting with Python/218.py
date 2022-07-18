import PyPDF2 as pdf
import os

# Find the relative pdf utilities folder path from the python file location
dir_path = os.path.dirname(os.path.realpath(__file__))

Original_pdf = dir_path+'\pdf\mergedsample.pdf'
watermark_pdf = dir_path+'\pdf\wtr.pdf'
new_pdf = dir_path+'\pdf\watermarkedsample.pdf'

# Open the files

with open(Original_pdf, "rb") as OrigFile, open(watermark_pdf, 'rb') as WtmFile:
    OrigPdf = pdf.PdfFileReader(OrigFile)
    # WtmPdf = pdf.PdfFileReader(WtmFile)
    watermark = pdf.PdfFileReader(WtmFile).getPage(0)

    # Merge the pages
    OutPdf = pdf.PdfFileWriter()
    for i, page in enumerate(OrigPdf.pages):
        page.merge_page(watermark)
        OutPdf.addPage(page)

    # write the merged pages
    with open(new_pdf, "wb") as newfile:
        OutPdf.write(newfile)
