import pandas as pd

data = pd.read_csv("../first_project/data.csv")

print(data)

print(" -----  ")

data.rename(columns={"age": "age_in_years", "email": "email address"}, inplace=True)

print(data)
