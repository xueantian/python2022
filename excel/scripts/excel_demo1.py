import openpyxl
a=openpyxl.load_workbook('Book1.xlsx')
sheet=a['Sheet1']
print(sheet.dimensions)
print(sheet['A']+sheet['B'])

i=2
while i < 10:
    cell=sheet['B{}'.format(i)]
    print(cell.value)
    i+=1
