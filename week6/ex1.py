import csv
from this import d
import numpy as np
import pandas as pd

file1_path = 'week6/CollegeGrades1.csv'
file2_path = 'week6/CollegeGrades2.csv'

skiprows = lambda row: row % 2 != 0
index_cols = [0, 1]
header_cols = [0, 1, 2]

headers = pd.read_csv(file1_path, skiprows=skiprows, header=None, nrows=len(header_cols), index_col=index_cols)
df = pd.read_csv(file1_path, skiprows=skiprows, index_col=index_cols, header=header_cols)
df.columns = pd.MultiIndex.from_arrays(headers.fillna(method="ffill", axis=1).values)
df.set_index(pd.MultiIndex.from_arrays(df.index.to_frame().fillna(method="ffill").T.values), inplace=True)
