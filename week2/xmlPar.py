import xml.etree.ElementTree as ET

tree = ET.parse('week2/XLMPratice.xml')

root = tree.getroot()

root.tag

root.attrib

root.text

student = root[0]

print(student.tag, student.attrib, student.text)
 
for s in root:
    name = s.get('name')
print(f"name is: {name}")

newData = "math, test2, 0.45"
data = newData.split(',')
i = 0
for child in root:
    newElm = ET.Element('student', {'ID': "1234"})
    newElm.text = data[i]
    i = i + 1
    child.append(newElm)
ET.dump(root)

for p in root.findall('student'):
    for child in p:
        try:
            value = str(student.text)
            if value == "Pace":
                root.remove(p)
        except ValueError:
            pass

tree.write("week2/XLMPratice.xml")
