import pandas as pd 

data_set = {
    "firstname": ["Ade", "Mike", "Mary"],
    "lastname": ["Joseph", "Andrew", "James"],
    "gender": ["male", "male", "female"],
    "age": [12, 13, 14]
}



data = pd.DataFrame(data_set)

print(data)


print(data.iloc[ [0,1], [0,2]])
