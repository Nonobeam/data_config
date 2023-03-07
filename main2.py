import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

d = pd.read_excel("content/PYTHON DATA CLASS L10 GROUP 06.xlsx", sheet_name="Data")
print(d)

# Comlumn graph
population_growth = {"East Asia & Pacific": 0.9,
                     "Europe & Central Asia": 0.3,
                     "Latin America & Caribean": 0.9,
                     "Middle East & North Africa": 1.7,
                     "Norht America": 0.7,
                     "South Asia": 1.4,
                     "Sub-Saharan Africa": 2.4}

fig, ax = plt.subplots()

ax.barh(list(population_growth.keys()), list(population_growth.values()))
ax.set (title = "Tỷ lệ tăng trưởng dân số các vùng trên thế giới", xlabel = "Percentage (%)", ylabel="Region");

plt.savefig("Growth.png");

population_ages = {"East Asia & Pacific": 0.9,
                   "Europe & Central Asia": 16.6,
                   "Latin America & North Caribean": 10.1,
                   "Middle East & North Africa": 3.7,
                   "North America": 17.4,
                   "South Asia": 5.7,
                   "Sun-Saharan Africa": 3.4}

gid, ax = plt.subplots()

ax.barh(list(population_ages.keys()), list(population_ages.values()));
ax.set (title = "Tỷ lệ già hoá dân số các vùng trên thế giới", xlabel = "Percentage (%)", ylabel = "Region")

plt.savefig("Ages.png")

Unemployment = {"Europe Asia & Pacific": 4.7,
                "Europe & Central Asia": 5.0,
                "Latin Amecia & Caribean": 10.33,
                "Middle East & North Africa": 11.1,
                "North America": 0.8}

fig, ax = plt.subplots()

ax.barh(list(Unemployment.keys()), list(Unemployment.values()));
ax.set (title = "Tỷ lệ thất nghiệp các vùng trên thế giới", xlabel = "Percentage (%)", ylabel = "Region")

plt.savefig("Unemployment.png")

labels = 'Europe Asia & Pacific', 'Europe & Central Asia', 'Latin Amecia & Caribean', 'Middle East & North Africa', 'North America', 'South Asia', 'Sub-Saharan Africa'

axis = (1423434, 23412465, 24534571, 769675474, 235662, 5761754, 54363415)

colors = ('gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'darkblue', 'pink', 'purple')

explode = (0.1, 0, 0, 0, 0.1, 0, 0)

plt.pie(axis, explode = explode, labels =  labels, colors = colors, autopct = '%.2f%%', shadow = True, startangle = 140)
plt.axis('equal')
plt.title('Cơ cấu tổng số dân tại các vùng trên thế giới')
plt.savefig("labels.png")
plt.show()

fig, ((ex1, ex2), (ex3, ex4)) = plt.subplots(nrows=2, ncols=2, figsize = (10, 5))

ex1.barh(list(population_growth.keys()), list(population_growth.values()))
ex2.barh(list(population_ages.keys()), list(population_ages.values()))
ex3.barh(list(population_growth.keys()), list(Unemployment.values()))
ex4.pie(axis, explode=explode, labels=labels, colors=colors, autopct='%.2f%%', shadow=True,startangle=140)

