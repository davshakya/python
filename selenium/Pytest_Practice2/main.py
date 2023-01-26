import xlrd 
wb=xlrd.open_workbook("F:\Computer_Programmes\selenium\sample.xlsx")
sh=wb.sheet_by_index(0)
cl=sh.cell(2,0).value
print(cl)
 