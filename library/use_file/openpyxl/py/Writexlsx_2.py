#セル値の設定
import openpyxl

book = openpyxl.Workbook()

active_sheet = book.active
active_sheet.cell(column=1,row=1,value="Write A1")
active_sheet["A2"] = "Write A2"

book.save("library/use_file/openpyxl/xlsx/sample2.xlsx")
