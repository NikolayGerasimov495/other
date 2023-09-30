import openpyxl

#wb = openpyxl.open('products.xlsx') тоже самое что и нижняя строка
wb = openpyxl.load_workbook(filename='products.xlsx')


sheet = wb['List']

cells = sheet['A1' : 'B12']
for name, phone in cells:
    print(name.value, phone.value, sep = '-----')
#
# for row in sheet.iter_rows():
#     for cell in row:
#         print(cell.value)

