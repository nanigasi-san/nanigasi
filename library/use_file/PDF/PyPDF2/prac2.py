# ページ数
import PyPDF2

FILE_PATH = "PDF/春休み宿題（基礎数学II）.pdf"

with open(FILE_PATH, mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(3)
    print(page.extractText())
