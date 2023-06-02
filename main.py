import sys
from pypdf import PdfMerger


def mergeThat(pdfs):
    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()


mergeThat(sys.argv[1:])
