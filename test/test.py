import os
from PyPDF2 import PdfFileMerger

target_path = '/Users/xiaogeyang/Documents/GitHub/work-experience/test/pdfs'

pdf_list = [f for f in os.listdir(target_path)if f.endswith('pdf')]
pdf_list = [os.path.join(target_path, filename) for filename in pdf_list]

file_merger = PdfFileMerger()
for pdf in pdf_list:
         file_merger.append(pdf)

file_merger.write("/Users/xiaogeyang/Documents/GitHub/work-experience/test/new.pdf")