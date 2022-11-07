import pandas as pd

data = pd.read_csv("data.csv")

col = data["firstname"]

##convert the series to a list
col_list = col.to_list()

#print(col_list)
found_names = []
for item in col_list:
    if item[0] == "J":
        found_names.append(item)
        
print(found_names)

found_name_series = pd.Series(found_names)

print(found_name_series)

