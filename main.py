import PyPDF2 as pi

pdffiles = ["1.pdf","2.pdf","3.pdf"]
merger = pi.PdfMerger()

for filename in pdffiles:
    pdffilename = open(filename,'rb')
    pdfreader = pi.PdfReader(pdffilename)
    merger.append(pdfreader)
pdffilename.close()
merger.write("merged.pdf")