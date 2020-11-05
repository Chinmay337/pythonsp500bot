# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:12:55 2020

@author: chinmay.bhelke
"""

import yfinance as yf
import pandas as pd

from classes import CompanyStore

def get_criteria_value(company, criteria):
    try:
        print('.')
        stockticker = yf.Ticker(company.ticker)
    #print(tesla.info['marketCap'])
        if criteria == 1:
            company.SetValue(stockticker.info['marketCap'])
        elif criteria == 2:
            company.SetValue(stockticker.info['volume'])
        elif criteria == 3:
            company.SetValue(stockticker.info['forwardEps'])
    except:
        print("x")
        company.SetValue(-1)


input_file_name = "sp500.txt"
store = CompanyStore (input_file_name)
sectors = store.get_sectors()

print("Welcome to Chinmay's S&P500 investment advice bot.")

while True:  
    user_input = input("Hello! How many companies do you wish to invest in? (max 100):")
    try:
        user_input_num = int(user_input)
        if user_input_num>0 and user_input_num<= 100:
            break
    except:
        print("Invalid number. ", end='')
    print("Please try again")

for s in sectors:
    print(s)

while True:  
    user_input = input("Which sector do you wish to invest in? (Enter number) : ")
    try:
        user_input_sector = int(user_input)
        if user_input_sector>0 and user_input_sector<= len(sectors):
            break
    except:
        print("Invalid number. ", end='')
    print("Please try again")

selected_sector = ""
for s in sectors:
    if s.idx == int(user_input_sector):
        selected_sector = s.name
        
assert selected_sector != "", "Wrong selection for sector"

print("Chosen sector: " ,selected_sector)
print('\n')

investment_strategies = ['Market Cap', 'Trading Volume','Earnings Per Share']
print("Investment strategies:")
print(1," ", investment_strategies[0])
print(2," ", investment_strategies[1])
print(3," ", investment_strategies[2])


while True:  
    user_input = input("Choose your investment strategy. (select number) :")
    try:
        user_input_criteria = int(user_input)
        if user_input_criteria>0 and user_input_criteria<= len(investment_strategies):
            break
    except:
        print("Invalid number. ", end='')
    print("Please try again")

#Find All Companies from given sector

selected_companies = store.get_companies_by_sector( selected_sector)

max_companies= min(int(user_input_num),len(selected_companies))
if max_companies == len(selected_companies):
    print("Companies:")
    for x in selected_companies[:(max_companies)]:
        print("  ", x)
else:
    #Find value of criteria for selected companies
    print("Working...")
    print("..." , end='')
    for x in selected_companies:
        get_criteria_value(x, int(user_input_criteria))
    #Sort companies by value of criteria
    sorted_companies = sorted(selected_companies,key=lambda x: x.GetValue(), reverse=True)
    print("\n")

    #Print top n companies
    print("Companies:")
    for x in sorted_companies[:(max_companies)]:
        print("   ", x)

