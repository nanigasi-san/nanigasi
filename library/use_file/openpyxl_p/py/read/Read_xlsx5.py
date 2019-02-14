#セル値の取得
import openpyxl

book = openpyxl.load_workbook("library/use_file/openpyxl/xlsx/test_book.xlsx")

active_sheet = book.active
print(active_sheet.cell(column=1,row=1).value)
print(active_sheet["B2"].value)

print("\n＜列ベースでの取得＞")
#列ベースでの取得
for column in active_sheet.columns:
    print("-"*25)
    for cell in column:
        print(cell.value)

print("\n＜行ベースでの取得＞")
#行ベースでの取得
for row in active_sheet.rows:
    print("-"*25)
    for cell in row:
        print(cell.value)
