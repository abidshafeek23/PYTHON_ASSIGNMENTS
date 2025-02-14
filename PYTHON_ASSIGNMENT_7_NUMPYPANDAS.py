# %%
import numpy as np
import pandas as pd

# %%
array1 = np.arange(1, 11).reshape(2, 5)
print("numray:\n", array1)

# %%
array2 = np.arange(1, 21)
elements = array2[5:16]
print("numray_2:\n", elements)

# %%
series = pd.Series({'apples': 3, 'bananas': 2, 'oranges': 1})
series['pears'] = 4
print("\nfruit_list:\n", series)

# %%
data = {
    'name': ['Aneesha', 'Boby', 'Aslam', 'David', 'Evan', 'Sahil', 'Godwin', 'Hafsa', 'Ihsan', 'Jack'],
    'age': [25, 30, 22, 40, 29, 35, 27, 33, 26, 31],
    'gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'M', 'M']
}
df = pd.DataFrame(data)
print("\nDataset:\n", df)

# %%
df['occupation'] = ['Programmer', 'Manager', 'Analyst', 'Programmer', 'Manager', 
                    'Analyst', 'Programmer', 'Manager', 'Analyst', 'Programmer']
print("\nDataset:\n", df)

# %%
df_filtered = df[df['age'] >= 30]
print("\nage>=30:\n", df_filtered)

# %%
csv_filename = "dataframe.csv"
df.to_csv(csv_filename, index=False)

# %%
df_read = pd.read_csv(csv_filename)
print("\ndataset:\n", df_read)


