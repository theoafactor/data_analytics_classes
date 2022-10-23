import pandas 

pandas.set_option("display.max_rows", 50)

data = pandas.read_csv("pds/students.csv")



print(data['gender'].value_counts())

# print(data['firstname'])