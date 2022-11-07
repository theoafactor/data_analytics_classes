import pandas 

pandas.set_option("display.max_rows", 50)

data = pandas.read_csv("pds/students.csv")

print(data)

print("-------------")


print(data.loc[[0,2], ['gender','email']])




    






# print(data['gender'])

# print(data['firstname'])