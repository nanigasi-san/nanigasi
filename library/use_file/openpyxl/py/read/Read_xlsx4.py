#シート内の列数・行数取得
import openpyxl

book = openpyxl.load_workbook("library/use_file/openpyxl/xlsx/test_book.xlsx")

active_sheet = book.active
print(active_sheet.max_column)
print(active_sheet.max_row)
