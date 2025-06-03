'''
This script put a watermark in all pdf pages.
Usage: python stamp_my_pdf.py <pdf_file> <pdf_watermark_file>
'''

import sys
import os
from pypdf import PdfReader, PdfWriter

try:
    pdf_file = sys.argv[1]
    watermark_file = sys.argv[2]
except IndexError:
    print("Usage: python stamp_my_pdf.py <pdf_file> <pdf_watermark_file>")
    sys.exit(1)

if not (os.path.exists(pdf_file) and os.path.exists(watermark_file)):
    print("pdf file or watermark file does not exist.")
    sys.exit(1)

if not (pdf_file.endswith('.pdf') and watermark_file.endswith('.pdf')):
    print("Both files must be PDF files.")
    sys.exit(1)

stamp = PdfReader(watermark_file).pages[0]
writer = PdfWriter(clone_from=pdf_file)

for page in writer.pages:
    page.merge_page(stamp, over=False)

writer.write(pdf_file.replace('.pdf', '_stamped.pdf'))
print(f"Watermark applied. Stamped PDF saved as {pdf_file.replace('.pdf', '_stamped.pdf')}")
