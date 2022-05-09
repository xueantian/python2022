import openpyxl

workbook=openpyxl.load_workbook('ISR1K_1D_Scale_2_3.xlsx')
sheet=workbook['ISR1K - 1D Scale']
#get all cols
cols=sheet.columns
sub_lst=[]
lst=[]
for col in cols:
    #print(col[0].value)
    if col[0].value == 'ISR1161X-8P':

        for i in range(0,10):
            sub_lst.append(col[i].value)
            i+=1

        print(sub_lst)

lst.append(sub_lst)

print(lst)
new_workbook=openpyxl.Workbook()
new_sheet=new_workbook.active
for row in lst:
        new_sheet.append(row)

new_workbook.save('ISR1161X-8P.xlsx')





