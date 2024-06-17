from pypdf import PdfMerger

pdfs = ['s1.pdf', 's2.pdf', 's3.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("Sudeshna.pdf")
merger.close()