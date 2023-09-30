import openpyxl


filename="products.xlsx"

book = openpyxl.load_workbook(filename = filename)
# sheet = book.active
sheet : sheet = book["List"]

sheet.column_dimensions["A"].width = 50 # прим. колво символов
sheet.column_dimensions["B"].width = 50
sheet.column_dimensions["C"].width = 50
# sheet.row_dimensions[1].font = Font(b=True, size=18, color="EE0000") # не будет работать -> Styles can also applied to columns and rows but note that this applies only to cells created (in Excel)

# стилизация ячеек
# font = Font(b=True, size=14, color="00DD00")
# fill1 = PatternFill("darkTrellis") # solid, darkVertical, mediumGray ...
# fill2 = PatternFill("solid", fgColor="FFFF99")
# sheet['A3'].font = font
# sheet['A3'].fill = fill1
# sheet['B3'].font = font
# sheet['B3'].fill = fill2

# встроенные стили https://openpyxl.readthedocs.io/en/stable/styles.html?highlight=styles
# sheet['A2'].style = "Good"
# sheet['B2'].style = "Bad"



book.save(filename)