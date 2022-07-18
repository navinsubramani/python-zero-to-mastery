from heapq import merge
import PyPDF2 as pdf
import os

# Find the relative pdf utilities folder path from the python file location
dir_path = os.path.dirname(os.path.realpath(__file__))
li_pdf = [dir_path+'\pdf\samplepdf_1.pdf', dir_path+'\pdf\samplepdf_2.pdf']

# merge the pdf files
merger = pdf.PdfFileMerger()
for i in li_pdf:
    merger.append(i)

# write the merger to the file
merger.write(dir_path+'\pdf\mergedsample.pdf')
