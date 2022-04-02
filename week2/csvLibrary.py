import csv
from re import L
#read
with open("week2/PeopleTrainngDate.csv", newline='') as file:
    dataReader = csv.reader(file)
    for row in dataReader:
        print(row[0], row[5])
# dicRead
with open("week2/PeopleTrainngDate.csv", newline='') as file:
    dataDicReader = csv.DictReader(file)
    for line in dataDicReader:
        if str(line.get('Name')) == "Clarke, Nita Z.":
            print(line.get('Name'), line.get('Company'))

# write
data = [['T1', 'T2', 'T3', 'T4', 'T5'],
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [3, 6, 9, 12, 15]]
with open('newFile.csv', 'w', newline='') as newFile:
    dataWriter = csv.writer(newFile)
    for x in data:
        dataWriter.writerow(x)

with open('newFile2.csv', 'w', newline='') as newFile:
    dataWriter = csv.writer(newFile)
    dataWriter.writerows(data)

# dictWrite
dataD = [{'T1': 1, 'T2': 2, 'T3': 3, 'T4': 4},
         {'T1': 2, 'T2': 4, 'T3': 6, 'T4': 8},
         {'T1': 3, 'T2': 6, 'T3': 9, 'T4': 123}]
# no header
with open('newDictWrote.csv', 'w', newline='') as newFile:
    dataWriter = csv.DictWriter(newFile, ['T1', 'T2', 'T3', 'T4', 'T5'])
    for x in dataD:
        dataWriter.writerow(x)

# header
with open('newdataDictWrite.csv', 'w', newline='') as newDictWrite:
    dataWrite = csv.DictWriter(newDictWrite,['T1', 'T2', 'T3', 'T4'])
    dataWrite.writeheader()
    dataWrite.writerows(dataD)
