from xlsxwriter import Workbook

workbook = Workbook('g_form_data.xlsx')
worksheet = workbook.add_worksheet()

# Start from the first cell.
# Rows and columns are zero indexed.
rows = 1
columns = 8

short_list = ['ram', 'shyam', 'gopal']
para_list = ['para_1', 'para_2', 'para_3']
multiple_list = ['multi_1', 'multi_2', 'multi_3']
check_list = ['check_1', 'check_2', 'check_3']
drop_list = ['drop_1', 'drop_2', 'drop_3']
date_list = ['date_1', 'date_2', 'date_3']
time_list = ['time_1', 'time_2', 'time_3']

# Writing headers
headers = ['This is Short Answer', 'This is Paragraph', 'This is a Multiple Choice', 'This is Check Box', 'This is Dropdown', 'This is Date', 'This is Time']
worksheet.write_row(0, 0, headers)

for row in range(3):
    data_row = [
        short_list[row],
        para_list[row],
        multiple_list[row],
        check_list[row],
        drop_list[row],
        date_list[row],
        time_list[row]
    ]
    worksheet.write_row(row=row+1, col=0, data=data_row)

workbook.close()
