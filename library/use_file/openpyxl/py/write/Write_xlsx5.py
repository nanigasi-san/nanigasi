#ボーダー設定
import openpyxl
from openpyxl.styles.borders import (
    Border,
    Side,
    BORDER_THIN,
    BORDER_DOTTED,
    BORDER_DOUBLE,
    BORDER_MEDIUM,
)

book = openpyxl.Workbook()

active_sheet = book.active
active_sheet.cell(column=2,row=2,value="Write B2")
active_sheet["C3"] = "Write C3"

active_sheet["B2"].border = Border(
    left = Side(style=BORDER_THIN),
    right = Side(style=BORDER_THIN),
    top = Side(style=BORDER_THIN),
    bottom=Side(style=BORDER_THIN),
)

border_C3 = Border()
border_C3.left = Side(style=BORDER_DOTTED)
border_C3.right = Side(style=BORDER_DOUBLE)
border_C3.top = Side(style=BORDER_MEDIUM)
border_C3.bottom = Side(style=BORDER_THIN)
active_sheet["C3"].border = border_C3
book.save("library/use_file/openpyxl/xlsx/sample5.xlsx")
