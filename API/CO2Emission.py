import requests
import matplotlib.pyplot as plt

req = requests.get("https://pkgstore.datahub.io/core/co2-fossil-global/global_json/data/"
                   + "cf26bfc62988eb44a387fdf653e3f01a/global_json.json")
data = req.json()

for obj in data:
    plt.plot(obj['Year'], obj['Cement'], color='blue', linestyle='dashed', linewidth=1, marker='o',
             markerfacecolor='blue', markersize=2)
    plt.plot(obj['Year'], obj['Gas Flaring'], color='green', linestyle='dashed', linewidth=1, marker='o',
             markerfacecolor='green', markersize=2)
    plt.plot(obj['Year'], obj['Gas Fuel'], color='yellow', linestyle='dashed', linewidth=1, marker='o',
             markerfacecolor='yellow', markersize=2)
    plt.plot(obj['Year'], obj['Liquid Fuel'], color='magenta', linestyle='dashed', linewidth=1, marker='o',
             markerfacecolor='magenta', markersize=2)
    plt.plot(obj['Year'], obj['Solid Fuel'], color='cyan', linestyle='dashed', linewidth=1, marker='o',
             markerfacecolor='cyan', markersize=2)
    plt.plot(obj['Year'], obj['Total'], color='red', linestyle='dashed', linewidth=1, marker='o',
             markerfacecolor='red', markersize=2)
plt.xlim(1751,2010)
plt.ylim(0,9200)
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
