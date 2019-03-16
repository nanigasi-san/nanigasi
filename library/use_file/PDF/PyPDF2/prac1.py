# ページ数
import PyPDF2

FILE_PATH = "library/use_file/PDF/PyPDF2/Fukuyama-ss03.pdf"
with open(FILE_PATH, mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    print(f"Number of pages: {reader.getNumPages()}")
