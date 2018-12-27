#列幅指定
import openpyxl

book = openpyxl.Workbook()

active_sheet = book.active
active_sheet.cell(column=1,row=1,value="Write A1")
active_sheet["A2"] = "Write A2"

active_sheet.column_dimensions["A"].width = 50
book.save("library/use_file/openpyxl/xlsx/sample3.xlsx")
