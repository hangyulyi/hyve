import openpyxl
import json

# TODO: find fix to display korean in json file

workbook = openpyxl.load_workbook('leniverse/1.xlsx')
worksheet = workbook.active

data_list = []

for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=3, max_col=4, values_only=True):
    data_list.append({
        'kr': row[0],
        'eng': row[1]
    })

json_data = json.dumps(data_list, indent=4)

with open('data.json', 'w') as f:
    f.write(json_data)