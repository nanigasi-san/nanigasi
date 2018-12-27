# 塗りつぶし設定
import openpyxl
from openpyxl.styles.colors import (
    Color,
    BLUE,
    RED,
    GREEN,
)
from openpyxl.styles.fills import (
    PatternFill,
    FILL_SOLID,
    FILL_PATTERN_MEDIUMGRAY,
    FILL_PATTERN_GRAY125,
)

book = openpyxl.Workbook()

active_sheet = book.active
active_sheet.cell(column=2, row=2, value="Write B2")
active_sheet["C3"] = "Write C3"
active_sheet["D4"] = "Write D4"

active_sheet["B2"].fill = PatternFill(
    patternType=FILL_SOLID,
    fgColor=openpyxl.styles.colors.Color(rgb=BLUE),
)

fill_C3 = PatternFill()
fill_C3.patternType = FILL_PATTERN_MEDIUMGRAY
fill_C3.fgColor = RED
active_sheet["C3"].fill = fill_C3

fill_D4 = PatternFill()
fill_D4.patternType = FILL_PATTERN_GRAY125
fill_D4.fgColor = GREEN
active_sheet["D4"].fill = fill_D4

book.save("library/use_file/openpyxl/xlsx/sample7.xlsx")
