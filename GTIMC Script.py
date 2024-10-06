## Script to fetch Data for DCF Model API Key: "H1PL45YBNI1IZDJU"
import requests
import json
import pandas as pd

ticker = input("What ticker? ")

# Fetch Income Statement Data
incomeStatementURL = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=H1PL45YBNI1IZDJU'
requestIncomeStatementData = requests.get(incomeStatementURL)
incomeStatmentData = requestIncomeStatementData.json()
df = pd.DataFrame(incomeStatmentData['annualReports'])
df.to_csv('IncomeStatmentData.csv', index=False)

# Fetch Balance Sheet Data
balanceSheetURL = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=H1PL45YBNI1IZDJU'
requestBalanceSheetData = requests.get(balanceSheetURL)
balanceSheetData = requestBalanceSheetData.json()
print(balanceSheetData)
df = pd.DataFrame(balanceSheetData['annualReports'])
df.to_csv('BalanceSheetData.csv', index=False)

# Fetch Cash Flow Statement Data 
cashFlowStatementURL = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=H1PL45YBNI1IZDJU'
requestCashFlowStatement = requests.get(cashFlowStatementURL)
cashFlowStatementData = requestCashFlowStatement.json()
df = pd.DataFrame(cashFlowStatementData['annualReports'])
df.to_csv('CashFlowStatementData.csv', index=False)