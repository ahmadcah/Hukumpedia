import csv,json

data = {}

with open('Data.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for rows in csvreader:
        id = rows['id']
        data[id] = rows

with open('Data.json', 'w') as jsonFile:
    jsonFile.write((json.dumps(data,indent=4)))