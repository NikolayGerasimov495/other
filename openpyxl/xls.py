import openpyxl

book = openpyxl.open('../work on file/table.xlsx', read_only = True) # открываем файл (read_only - файл запускается на открытие)
# sheets = book.worksheets # обращаемся ко всем листам
sheet_2 = book.worksheets[2] # обращаемся ко 2 листу
print(sheet_2['A1'].value)
# sheet = book.active # берем лист в файле (active - берет по умолчанию первый лист)
# print(sheet['B2'].value)
# print(sheet[1][2].value)  # можно обратиться по ячейке ряд и колонка
# for row in range(1, 10):
#     print(sheet[row])
#
# for row in range(1, sheet.max_row + 1):
#     track_id = sheet[row][0].value
#     name = sheet[row][1].value
#     composer = sheet[row][2].value
#     milliseconds = sheet[row][3].value
#     print(row, track_id, name, composer, milliseconds)

# cells = sheet['B2' : 'C14']
# for name, composer in cells:
#     print(name.value, composer.value, sep = '-----')

# for row in sheet.iter_rows(min_row=2, max_row=20, min_col=1, max_col=3):
#     for cell in row:
#         print(cell.value, end = ' ')
#     print()