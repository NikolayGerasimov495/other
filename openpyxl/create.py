import openpyxl
from faker import Faker

wb = openpyxl.Workbook()
wb.remove(wb.active)
list1 = wb.create_sheet("List")
list2 = wb.create_sheet('list2')
def data_samples():
    fk = Faker('ru_RU')
    return [[fk.name(), fk.phone_number(), fk.address()] for _ in range(50)]

for sheet in wb.worksheets:  # перебираю таблицы
        for row in data_samples():  # получаю данные
            sheet.append(row)

print(wb.sheetnames)
wb.save('products.xlsx')