import openpyxl
#configure workbook path
b = openpyxl.load_workbook("F:\\Computer_Programmes\\selenium\\Pytest_Practice\\data.xlsx")
#get active sheet
sht = b.active
#get cell address within active sheet
cl = sht.cell (row = 6, column = 2)
#read value with cell
print("Reading value from row-3, col-2: ")
print(cl.value)


# import xlrd 
# wb=xlrd.open_workbook("F:\Computer_Programmes\selenium\sample.xlsx")
# sh=wb.sheet_by_index(0)
# cl=sh.cell(2,0).value
# print(cl)