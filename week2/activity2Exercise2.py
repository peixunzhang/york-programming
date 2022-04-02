#Activity 2: File processing
#Exercise 2
import csv
from datetime import datetime
from email import header

class Dataset:
    def __init__(self, rows, lengths):
        self.header = rows[0]
        self.data = rows[1:]
        self.lengths = lengths

    def sort(self, f):
        self.data.sort(key = f)

    def show(self):
        for fields in [self.header] + self.data:
            output = []
            for i, v in enumerate(fields):
                output.append(v.ljust(self.lengths[i]))
            print("\t".join(output))

def parse_file(file):
    maxLen = {}
    result = []    
    with open(file) as file:
        for line in file:
            if line:
                fields = split_line(line, ",")
                for inx, val in enumerate(fields):
                    max = len(val)
                    if inx not in maxLen or max >= maxLen[inx]:
                        maxLen[inx] = max
                result.append(fields)
    return Dataset(result, maxLen)

def split_line(line, delimiter=","):
    out = [] # [Mr.]
    current = [] #[]
    escaped = False #T
    for c in line:
        if not escaped and c == delimiter:
            out.append("".join(current).strip())
            current = []
        elif c == "\"":
            escaped = not escaped
        else:
            current.append(c)
    out.append("".join(current).strip())
    return out

def main():
    data = parse_file("week2/PeopleTrainngDate.csv")

    def sortKey(line):
        return datetime.strptime(line[5], '%d/%m/%Y')
    
    data.sort(lambda x: datetime.strptime(x[5], '%d/%m/%Y'))
    data.show()

if __name__ == "__main__":
    main()
