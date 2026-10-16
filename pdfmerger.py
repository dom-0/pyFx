from pypdf import PdfMerger

pdfs = ['1.pdf', '2.pdf', '3.pdf', '4.pdf', '5.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("FINAL.pdf")
merger.close()
# useless commentß