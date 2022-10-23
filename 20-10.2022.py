import pandas as pd
# covid_data = pd.read_csv('archive/us.csv', index_col="date")
covid_data = pd.read_csv('archive/us.csv')

data_filter = ((covid_data['cases'] >=1) & (covid_data['deaths'] > 50))


print(covid_data.loc[data_filter, ['cases']])

# print(covid_data[data_filter])