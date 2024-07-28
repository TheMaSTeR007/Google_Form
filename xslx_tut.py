# import xlsxwriter module
import xlsxwriter

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('g_form_data.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

# Use the worksheet object to write
# data via the write() method.
worksheet.write('A1', 'This is Short Answer')
worksheet.write('B1', 'This is Paragraph')
worksheet.write('C1', 'This is a Multiple Choice')
worksheet.write('D1', 'This is Check Box')
worksheet.write('E1', 'This is Dropdown')
worksheet.write('F1', 'This is Date')
worksheet.write('G1', 'This is Time')

# Finally, close the Excel file
# via the close() method.
workbook.close()
