import matplotlib.pyplot as plt
import pandas as pd
import statistics

GasCSV = pd.read_csv('Gas Prices(Short)Years.csv')

price = (GasCSV['Price'])
date = (GasCSV['Date'])
print(price)
plt.plot(date,price)
plt.xlabel('date')
plt.ylabel('price')
plt.title('Gas Prices')
plt.show()

