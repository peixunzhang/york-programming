#Activity 2: File processing
#Exercise one
import csv

def split_line(line, delimiter=","):
    out = [] # [Mr.]
    current = [] #[]
    escaped = False #T
    for c in line:
        if not escaped and c == delimiter:
            out.append("".join(current))
            current = []
        elif c == "\"":
            escaped = not escaped
        else:
            current.append(c)
    return out

def main():
    with open("week2/PeopleTrainngDate.csv") as file:
        maxLen = {}
        for line in file:
            if line:
                fields = split_line(line, ",")
                for inx, val in enumerate(fields):
                    max = len(val)
                    if inx not in maxLen or max >= maxLen[inx]:
                        maxLen[inx] = max
        file.seek(0)
        for line in file:
            if line:
                fields = split_line(line, ",")
                output = []
                for i, v in enumerate(fields):
                    output.append(v.ljust(maxLen[i]))
                print("\t".join(output))

if __name__ == "__main__":
    main()
