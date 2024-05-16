import ast
with open('stock_info.txt', 'r') as file:
    lines = file.readlines()

allinfo = []
'''for line in lines:
    line.strip('{}')
    l = line.split(', ')
    info = {}
    for data in line:
        key, value = data.split(': ')
        info[key.strip()] = value.strip()
'''
for line in lines:
    info = ast.literal_eval(line)
    allinfo.append(info)