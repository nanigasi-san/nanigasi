#ブックの保存とシートの追加
import openpyxl
book = openpyxl.Workbook()
book.create_sheet("nanigasi_1")

book.save("library/use_file/openpyxl/sample.xlsx")
