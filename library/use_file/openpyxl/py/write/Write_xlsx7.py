#文字寄せ設定
import openpyxl
from openpyxl.styles import Alignment

book = openpyxl.Workbook()

active_sheet = book.active
active_sheet.cell(column=2,row=2,value="write B2")
active_sheet["C3"] = "write C3"
active_sheet["D4"] = "write D4"
active_sheet["E5"] = "write E5"

active_sheet["B2"].alignment = Alignment(
    horizontal="center",
    vertical="bottom",
)

align_C3 = Alignment()
align_C3.horizontal = "right"
align_C3.vertical = "center"
active_sheet["C3"].alignment = align_C3


align_D4 = Alignment()
align_D4.horizontal = "left"
align_D4.vertical = "center"
active_sheet["D4"].alignment = align_D4


align_E5 = Alignment()
align_E5.horizontal = "left"
align_E5.vertical = "top"
active_sheet["E5"].alignment = align_E5

book.save("library/use_file/openpyxl/xlsx/sample7.xlsx")
