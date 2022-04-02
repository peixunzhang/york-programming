#Activity 2: File processing
#Exercise 3
import csv
from datetime import datetime
from email import header

class Dataset:
    def __init__(self, rows, lengths, has_header):
        if has_header:
            self.header = rows[0]
            self.data = rows[1:]
        else:
            self.data = rows
        self.lengths = lengths
        self.has_header = has_header

    def sort(self, f):
        self.data.sort(key = f)

    def show(self):
        if self.has_header:
            all_data = [self.header] + self.data
        else: 
            all_data = self.data
        for fields in all_data:
            output = []
            for i, v in enumerate(fields):
                output.append(v.ljust(self.lengths[i]))
            print("\t".join(output))

    def reorder(self, order):
        if self.has_header:
            new_header = []
            for field in order:
                new_header.append(self.header[field])
            self.header = new_header

        new_lengths = {}
        for new_index, old_index in enumerate(order):
            new_lengths[new_index] = self.lengths[old_index]
        self.lengths = new_lengths

        new_data = []
        for row in self.data:
            new_row = []
            for field in order:
                new_row.append(row[field])
            new_data.append(new_row)
        self.data = new_data

    def append(self, that):
        if self.has_header and that.has_header:
            assert(self.header == that.header)
        elif that.has_header:
            self.header = that.header

        self.data = self.data + that.data

        for k, v in self.lengths.items():
            self.lengths[k] = max(v, that.lengths[k])

def parse_file(file, has_header, delimiters):
    maxLen = {}
    result = []
    with open(file) as file:    
        for line in file:
            if line:
                fields = split_line(line, delimiters)
                for inx, val in enumerate(fields):
                    max = len(val)
                    if inx not in maxLen or max >= maxLen[inx]:
                        maxLen[inx] = max
                result.append(fields)
    return Dataset(result, maxLen, has_header)

def split_line(line, delimiters=[","]):
    out = [] # [Mr.]
    current = [] #[]
    escaped = False #T
    for c in line:
        if not escaped and c in delimiters:
            out.append("".join(current).strip())
            current = []
        elif c == "\"":
            escaped = not escaped
        else:
            current.append(c)
    out.append("".join(current).strip())
    return out

def main():
    data = parse_file("week2/PeopleTrainngDate.csv", True, [","])
    
    update = parse_file("week2/PeopleTrainingDateUpdate.csv", False, [",", " "])
    update.reorder([3, 4, 2, 1, 5, 0])
    data.append(update)

    data.sort(lambda x: datetime.strptime(x[5], '%d/%m/%Y'))
    data.show()


if __name__ == "__main__":
    main()
