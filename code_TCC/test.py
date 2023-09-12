import json

with open(f'json_data_files/2023-08-01.json', 'r') as json_file:
    json_data = json.load(json_file)

list_items = list(json_data.keys())

# count_items = list_items.count()
i = 0
for keys in json_data:
    i = i + 1

print(i)
# print(count_items)