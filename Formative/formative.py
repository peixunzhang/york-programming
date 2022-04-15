import csv
import pandas as pd
import sys

class Frequency:
    def __init__(self, id, airport_ref, freq):
        self.id = id
        self.airport_ref = airport_ref
        self.freq = freq
    @classmethod
    def from_row(cls, row):
        id = row.get('id')
        airport_ref = row.get('airport_ref')
        freq = float(row.get('frequency_mhz'))
        return cls(id, airport_ref, freq)

class Airport:
    def __init__(self, id, type):
        self.id = id
        self.type = type
    @classmethod
    def from_row(cls, row):
        id = row.get('id')
        type = row.get('type')
        return cls(id, type)

class AirportFreq:
    def __init__(self, airport, freq):
        self.airport = airport
        self.freq = freq
    def to_dict(self):
        return{'airport_id': self.airport.id, 'freq': self.freq.freq, 'type': self.airport.type}

type_values = {'small_airport', 'medium_airport', 'large_airport'}


def parse(file_freq, file_airport):
    print(f"Reading frequency file {file_freq}")
    f_map = {}
    with open(file_freq) as f:
        freq_reader = csv.DictReader(f)
        for line in freq_reader:
            freq = Frequency.from_row(line)
            if freq.airport_ref in f_map:
                f_map[freq.airport_ref].append(freq)
            else:
                f_map[freq.airport_ref] = [freq]

    af_list = []
    print(f"Reading airport file {file_airport}")
    with open(file_airport) as f:
        csvReader = csv.DictReader(f)
        for line in csvReader:
            airport = Airport.from_row(line)
            if airport.type in type_values:
                freqs = f_map.get(airport.id, [])
                for fq in freqs:
                    af_list.append(AirportFreq(airport, fq))
    return pd.DataFrame.from_records([a.to_dict() for a in af_list])

def save(df: pd.DataFrame, file: str):
    print(f"Saving data to {file}")
    df.to_json(file, orient="records")

def main():
    airport_freq = sys.argv[1]
    airport = sys.argv[2]
    save_json = sys.argv[3]
    save(parse(airport_freq, airport), save_json)


if __name__ == "__main__":
    main()
