## Script to fetch Data for DCF Model 
## API Documentation "https://www.alphavantage.co/documentation/" more APIs and get an API Key from the link
import requests
import json
import pandas as pd

apikey = input("What is your API key? ")
ticker = input("What ticker? ")

# Fetch Income Statement Data
incomeStatementURL = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + apikey
requestIncomeStatementData = requests.get(incomeStatementURL)
incomeStatmentData = requestIncomeStatementData.json()
df = pd.DataFrame(incomeStatmentData['annualReports'])
df.to_csv('IncomeStatmentData.csv', index=False)

# Fetch Balance Sheet Data
balanceSheetURL = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + apikey
requestBalanceSheetData = requests.get(balanceSheetURL)
balanceSheetData = requestBalanceSheetData.json()
print(balanceSheetData)
df = pd.DataFrame(balanceSheetData['annualReports'])
df.to_csv('BalanceSheetData.csv', index=False)

# Fetch Cash Flow Statement Data 
cashFlowStatementURL = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + apikey
requestCashFlowStatement = requests.get(cashFlowStatementURL)
cashFlowStatementData = requestCashFlowStatement.json()
df = pd.DataFrame(cashFlowStatementData['annualReports'])
df.to_csv('CashFlowStatementData.csv', index=False)
