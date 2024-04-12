# Pandas: Out of bounds nanosecond timestamp

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl'],
    'salary': [175.1, 180.2, 190.3],
    'date': ['2023-01-05', '2023-03-25', '2362-01-24']
})

# 1677-09-21 00:12:43.145224193
print(pd.Timestamp.min)

# 2262-04-11 23:47:16.854775807
print(pd.Timestamp.max)