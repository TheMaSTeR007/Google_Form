import openpyxl

# load workbook
wb = openpyxl.load_workbook('g_form_data.xlsx')
sheet = wb.active
cell_value = sheet['A1'].value
print(cell_value)