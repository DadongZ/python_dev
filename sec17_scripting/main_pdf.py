import PyPDF2
file = '/mnt/d/Data/Dadong/career/cover_letter.pdf'

with open(file, 'rb') as pdf:
    cv = PyPDF2.PdfFileReader(pdf)
    cvp1 = cv.getPage(1)
    print(cv.getDocumentInfo())
    cvp1.rotateClockwise(90)
    w = PyPDF2.PdfFileWriter()
    w.addPage(cvp1)

    with open('rotatecv.pdf', 'wb') as newfile:
        w.write((newfile))