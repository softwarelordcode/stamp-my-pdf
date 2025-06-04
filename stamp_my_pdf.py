'''
This script put a stamp on all pdf pages.
Usage: python stamp_my_pdf.py <pdf_file> <pdf_stamp_file> <>
'''

import sys
import os
from pypdf import PdfReader, PdfWriter

try:
    if sys.argv[1] == '-w':
        pdf_file = sys.argv[2]
        stamp_file = sys.argv[3]
        STAMP = False
    else:
        pdf_file = sys.argv[1]
        stamp_file = sys.argv[2]
        STAMP = True
except IndexError:
    print("Usage: python stamp_my_pdf.py <pdf_file> <stamp_file>")
    print("or")
    print("Usage: python stamp_my_pdf.py -w <pdf_file> <stamp_file>")
    sys.exit(1)

if not (os.path.exists(pdf_file) and os.path.exists(stamp_file)):
    print("pdf file or stamp file does not exist.")
    sys.exit(1)

if not (pdf_file.endswith('.pdf') and stamp_file.endswith('.pdf')):
    print("Both files must be PDF files.")
    sys.exit(1)

stamp = PdfReader(stamp_file).pages[0]
writer = PdfWriter(clone_from=pdf_file)

for page in writer.pages:
    page.merge_page(stamp, over=STAMP)

writer.write(pdf_file.replace('.pdf', '_stamped.pdf'))
print(f"Stamp applied. Stamped PDF saved as {pdf_file.replace('.pdf', '_stamped.pdf')}")
