import numpy as np
import pandas as pd

d = pd.read_excel("content/PYTHON DATA CLASS L10 GROUP 06.xlsx", sheet_name="Data")
print(d)

# Read the value
d.info()
# Read value in first 5 rows in table
d.head()
# Decribe all value
d.describe(include = "all")
# Read the value we choose
d.iloc[[2]]
d.iloc[2:10, :-1]
# Group the Region
d.groupby("Region").apply(print)
# Merge table Region and Population_Age
print(d.groupby(["Region"], as_index = False)["Population ages"].mean())
# Group Region and Name with specific Population ages
print(d.groupby(['Region', 'Country Name']).agg({'Population ages':"sum"}))
# Group Region and Population growth into 1 table
print(d.groupby(["Region"], as_index = False)["Population growth"].mean())
# Group Region and Name with specific Population growth
print(d.groupby(['Region', 'Country Name']).agg({'Population growth':"sum"}))
# Group Region and Name with specific Unemployment into 1 table
print(d.groupby(["Region"], as_index = False)["Unemployment"].mean())
# Group Region and Name with specific Unemployment
print(d.groupby(['Region', 'Country Name']).agg({'Unemployment':"sum"}))
# Create table Pivot with Region
pivot1 = pd.pivot_table (d, index ='Region') # FutureWarning: pivot_table dropped a column because it failed to aggregate. This behavior is deprecated and will raise in a future version of pandas. Select only the columns that can be aggregated.
pivot1
# Create Pivot table with Region and Population ages
pivot2 = pd.pivot_table (d, index = 'Region', values='Population ages', margins=True)
pivot2
# Create Pivot table with Region and Population ages in the world
pivot3 = pd.pivot_table (d, values='Population total', index = 'Region', aggfunc=['count','sum'], margins=True)
pivot3

d.pivot_table(values='Population growth', index='Region', aggfunc=('sum', 'mean')).round(decimals=1)
d.pivot_table(values='Population ages', index='Region', aggfunc=('sum', 'mean')).round(decimals=1)
d.pivot_table(values='Unemployment', index='Region', aggfunc=('sum', 'mean')).round(decimals=1)
