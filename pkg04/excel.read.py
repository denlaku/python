# coding=UTF-8
# pylint: disable=invalid-name
'''
write.excel
'''
from openpyxl import load_workbook

wb = load_workbook(filename='pkg04/empty_book.xlsx')
# sheet_ranges = wb['range names']
# print sheet_ranges['D18'].value
sheetNames = wb.get_sheet_names()
print(sheetNames)
smap = {}
for sheetName in sheetNames:
    sheet = wb[sheetName]
    if not sheetName in smap:
        smap[sheetName] = []
    rows = sheet.rows
    rowsdata = smap[sheetName]
    for row in rows:
        rowdata = []
        for cell in row:
            rowdata.append(cell.value)
        rowsdata.append(rowdata)

print(smap)

print("-------------------------------")
