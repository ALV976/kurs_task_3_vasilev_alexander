import sys
sys.path.append('utils')

from functions import open_file, get_format, list_executed


data = open_file()
data = list_executed(data)
data = sorted(data, key=lambda x: x['date'], reverse=True)[:5]

for trans in data:
    trans_format = get_format(trans)
    print(trans['date'], ' ', trans['description'])
    print(trans['from'], '->', trans['to'])
    print(trans['operationAmount']['amount'], trans['operationAmount']['currency']['name'])
    print()