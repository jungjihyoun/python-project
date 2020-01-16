import pandas as pd

office = pd.read_csv('office.csv', index_col=1)
office
my_office = pd.DataFrame(columns=office.columns)
my_office
a =
len_of_rows = office.shape[0]
for i in range(len_of_rows):
    if ("시계" in office.iloc[i, 0]) or ("도계" in office.iloc[i, 0]):
        my_office.loc[i, :] = office.iloc[i, :]
my_office = result.set_index("Unnamed: 0")
my_office

my_office.index.names = ["name"]
my_office.to_dict()
