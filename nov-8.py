import pandas as pd

# Create the DataFrame
Df = pd.read_csv("first_project/data.csv")
        
print(Df)

# 1. create the filter mask 
# filter_mask = Df["firstname"] == "Joshua"
filter_mask = ( Df["firstname"].str.startswith("J") &  Df["hobbies"].str.contains("Reading") )

# data = Df[filter_mask]

data = Df.loc[ ~filter_mask, ["firstname"]]

print(data) 

