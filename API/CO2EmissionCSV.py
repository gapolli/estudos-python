import requests
import csv
import matplotlib.pyplot as plt

req = requests.get("https://pkgstore.datahub.io/core/co2-fossil-global/global_csv/"
                   + "data/09015539c2fc32bb3c4afead7df461b5/global_csv.csv")
data = csv.reader(req.text.strip().split('\n'))

for obj in data:
    if obj[0] != 'Year':
        year = int(obj[0])
        total = int(obj[1])
        gas = int(obj[2])
        liquid = int(obj[3])
        solid = int(obj[4])
        cement = int(obj[5])
        flaring = int(obj[6])
        plt.plot(year, cement, color='blue', linestyle='dashed', linewidth=1, marker='o',
                 markerfacecolor='blue', markersize=2)
        plt.plot(year, flaring, color='green', linestyle='dashed', linewidth=1, marker='o',
                 markerfacecolor='green', markersize=2)
        plt.plot(year, gas, color='yellow', linestyle='dashed', linewidth=1, marker='o',
                 markerfacecolor='yellow', markersize=2)
        plt.plot(year, liquid, color='magenta', linestyle='dashed', linewidth=1, marker='o',
                 markerfacecolor='magenta', markersize=2)
        plt.plot(year, solid, color='cyan', linestyle='dashed', linewidth=1, marker='o',
                 markerfacecolor='cyan', markersize=2)
        plt.plot(year, total, color='red', linestyle='dashed', linewidth=1, marker='o',
                 markerfacecolor='red', markersize=2)
plt.xlim(1751, 2010)
plt.ylim(0, 9200)
plt.xlabel('Year')
plt.ylabel('Total (million metric tons of C)')
plt.title('Global CO2 Emissions from Fossil Fuels since 1751')
plt.plot([], color='blue', label='Cement production')
plt.plot([], color='green', label='Gas flaring')
plt.plot([], color='yellow', label='Gas fuel consumption')
plt.plot([], color='magenta', label='Liquid fuel consumption')
plt.plot([], color='cyan', label='Solid fuel consumption')
plt.plot([], color='red', label='Total emissions')
plt.legend()
plt.show()

