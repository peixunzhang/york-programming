import pandas as pd
from pandas import Series, DataFrame

# series
obj = pd.Series([4, 7, -5, 3])
print(obj.values)

#DataFrame
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame.describe())
