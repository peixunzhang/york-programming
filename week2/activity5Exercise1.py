import json
import xml.etree.ElementTree as ET

from more_itertools import first

tree = ET.parse('week2/People.xml')
root = tree.getroot()
forJson = {"students": []}
for student in root:
    fullName = student.find('fullName')
    title = fullName.get('title')
    firstN = fullName.find('firstName').text
    surN = fullName.find('surname').text
    try:
        other = fullName.find('other')
        names = list(map(lambda x: x.text, other.findall('name')))
    except:
        names = []
    age = int(student.find('age').text)
    city = student.find('city').text
    entry = {"fullName": {"title": title, "first": firstN, "surname": surN, "other": names}, "age": age, "city": city}
    forJson["students"].append(entry)
print(forJson)
with open("week2/xToJ.json", 'w') as jFile:
    json.dump(forJson, jFile, indent=2)
