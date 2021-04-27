import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import csv
import numpy as np
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

