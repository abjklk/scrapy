import PyPDF2
import os
import glob

def PDFmerge(pdfs, output):
    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()

    # appending pdfs one by one
    for pdf in pdfs:
        pdfMerger.append(PyPDF2.PdfFileReader(pdf,'rb'))

    # writing combined pdf to output pdf file
    # with open(output, 'wb') as f:
    pdfMerger.write('op.pdf')


pdfs = glob.glob("*.pdf")

# output pdf file name
output = 'combined.pdf'
# calling pdf merge function
PDFmerge(pdfs=pdfs, output=output)

# creating a pdf file object
pdfFileObj = open('combined.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
# print(pdfReader.numPages)

outfile = open('dict.csv', 'w')
outfile.write('usn' + ',' + 'sgpa' + '\n')

for i in range(pdfReader.numPages):
    # creating a page object
    mydict = {}
    pageObj = pdfReader.getPage(i)
    # extracting text from page
    txt = pageObj.extractText()
    mydict[txt[txt.find('USN') + 4:txt.find('USN') + 16]] = txt[txt.find('SGPA') + 4:txt.find('SGPA') + 8]
    print(mydict)

    for key, value in sorted(mydict.items()):
        outfile.write(str(key) + ',' + str(value) + '\n')

    # print(txt[txt.find('USN')+4:txt.find('USN')+16])
    # print(txt[txt.find('SGPA')+4:txt.find('SGPA')+8])
# closing the pdf file object
pdfFileObj.close()
