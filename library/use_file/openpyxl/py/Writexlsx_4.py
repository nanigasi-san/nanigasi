#フォント設定
import openpyxl

book = openpyxl.Workbook()

active_sheet = book.active
active_sheet.cell(column=1,row=1,value="Write A1")
active_sheet["A2"] = "Write A2"

cell_A1 = active_sheet["A1"]
cell_A1.font = openpyxl.styles.Font(bold=True)

font_A2 = openpyxl.styles.Font()
font_A2.bold = True
font_A2.color = openpyxl.styles.colors.BLUE
font_A2.name = "Arial"
active_sheet["A2"].font= font_A2

book.save("library/use_file/openpyxl/xlsx/sample4.xlsx")
