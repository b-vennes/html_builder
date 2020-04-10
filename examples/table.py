import sys
import os

# need to add html_builder to python path
html_builder_path = os.path.join(os.getcwd(), '..')
sys.path.append(html_builder_path)

from html_builder.html_builder.html import Html

header_data = Html('th', colspan='2')
header_data.children += ['Two column table header']

header_row = Html('tr')
header_row.children += [header_data]

table_header = Html('thead')
table_header.children += [header_row]

table_body = Html('tbody')

data_list = [
    ['a', 'b'],
    ['c', 'd'],
    ['e', 'f']
]

for row in data_list:
    table_row = Html('tr')
    
    for item in row:
        row_data = Html('td')
        row_data.children += [item]
        table_row.children += [row_data]
    table_body.children += [table_row]

table = Html('table')

table.children += [table_header, table_body]

print(table.render())