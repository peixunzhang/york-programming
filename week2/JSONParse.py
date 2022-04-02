
import json

details = {"name": "Adam Pa", "age": 27, "height": 1.54, "is_male": True}
print(json.dumps(details))

data = {'T1': [1, 2, 3, 4, 5],
        'T2': [2, 4, 6, 8, 10],
        'T3': [3, 6, 9, 12, 15]}

# outFile = open("week2/JSONPratice.json", 'w')
# json.dump(data, outFile)
# outFile.close()

inFile = open("week2/horseRace.json")
dataFile = json.load(inFile)
print(dataFile)

print(json.dumps(dataFile, sort_keys=True, indent=2))
inFile.close()

for h in dataFile['races']:
    print(h['number'], h['type'], h['weather'])
