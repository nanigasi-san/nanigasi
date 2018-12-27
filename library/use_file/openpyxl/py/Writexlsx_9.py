#Excel関数の埋め込み
import openpyxl

book = openpyxl.Workbook()

active_sheet = book.active
active_sheet["B2"] = 1
active_sheet["B3"] = 10
active_sheet["B4"] = 100
active_sheet["B5"] = "=sum(B2,B3,B4)"

book.save("library/use_file/openpyxl/xlsx/sample9.xlsx")
