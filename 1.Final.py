import matplotlib.pyplot as plt#Imports matplotlib library under the shortcut name plt
import pandas as pd#Imports pandas library under the shortcut name pd
import statistics#Imports statistics library

GasCSV = pd.read_csv('2.Short(Final).csv')#Reads the csv datapack

price = (GasCSV['Price'])#sets the price variable as everything under the 'Price' heading in the csv file
date = (GasCSV['Date'])#sets the date variable as everything under the 'Date' heading in the csv file
plt.plot(date,price)#Plots the date variable on the x axis and the y variable on the y axis of a graph
plt.xlabel('Year')#Labels the x axis 'Year'
plt.ylabel('Price')#Labels the y axis 'Price'
plt.title('Gas Prices')#Titles the graph 'Gas Prices'
plt.show()#Shows the graph