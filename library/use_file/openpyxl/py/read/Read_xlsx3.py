#指定のシートを取得
import openpyxl

book = openpyxl.load_workbook("library/use_file/openpyxl/xlsx/test_book.xlsx")

print(book.active.title)
print(book.worksheets[1].title)
print(book["テストシート３"].title)
#print(book.get_sheet_by_name("テストシート３").title)　はなくなった(8行目に統一)
