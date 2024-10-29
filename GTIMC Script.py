## Script to fetch Data for DCF Model 
## API Documentation "https://www.alphavantage.co/documentation/" more APIs and get an API Key from the link
import requests
import pandas as pd
from datetime import datetime
import xlsxwriter

# Get the current date and time
currentDateTime = datetime.now()
formatted_date = currentDateTime.strftime('%Y-%m-%d') 


apikey = input("What is your API key? ")
ticker = input("What ticker? ")


### Fetch Income Statement Data
incomeStatementURL = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=' + ticker + '&apikey=' + apikey
requestIncomeStatementData = requests.get(incomeStatementURL)
incomeStatementData = requestIncomeStatementData.json()
incomeStatementdf = pd.DataFrame(incomeStatementData['annualReports'])
incomeStatementdfLastFive = incomeStatementdf[0:4]

# Clean Up of Income Statement Data from Pandas Dataframe, hence forth variable names "IS" means Income Statement
ISYear = incomeStatementdfLastFive['fiscalDateEnding']
ISCurrency = incomeStatementdfLastFive['reportedCurrency']

ISRevenue = incomeStatementdfLastFive['totalRevenue']
ISRevenueGrowth = incomeStatementdfLastFive[]

ISCostOfRevenue = incomeStatementdfLastFive['costOfRevenue']
ISCOGSPercentOfRevenue = incomeStatementdfLastFive[]
ISGrossProfit = incomeStatementdfLastFive['grossProfit']
ISGrossProfitRatio = incomeStatementdfLastFive[]

ISRDExpenses = incomeStatementdfLastFive['researchAndDevelopment']
ISRDToRevenue = incomeStatementdfLastFive[]
ISSellingGAExpenses = incomeStatementdfLastFive['sellingGeneralAndAdministrative']
ISSalesGAExpenses = incomeStatementdfLastFive[]
ISSellAndMarkExpenses = incomeStatementdfLastFive[]
ISMarketingExpenseToRevenue = incomeStatementdfLastFive[]
ISOtherExpenses = incomeStatementdfLastFive[]
ISOperatingExpenses = incomeStatementdfLastFive['operatingExpenses']

ISCostAndExpenses = incomeStatementdfLastFive[]
ISEarningsBITDA = incomeStatementdfLastFive['ebitda']
ISEBITDARatio = incomeStatementdfLastFive[]
ISInterestExpense = incomeStatementdfLastFive['interestExpense']
ISInterestExpensePercentOfLTDebt = incomeStatementdfLastFive[]
ISDepreciationAndAmmort = incomeStatementdfLastFive['depreciationAndAmortization']
ISOperatingIncome = incomeStatementdfLastFive['operatingIncome']
ISOperatingIncomeRatio = incomeStatementdfLastFive

ISTotalOtherIncomeExpensesNet = incomeStatementdfLastFive[]
ISIncomeBeforeTax = incomeStatementdfLastFive['incomeBeforeTax']
ISIncomeBeforeTaxRatio = incomeStatementdfLastFive[]
ISIncomeTaxExpense = incomeStatementdfLastFive['incomeTaxExpense']
ISNetIncome = incomeStatementdfLastFive['netIncome']

ISEarningsPS = incomeStatementdfLastFive[]

### Fetch Balance Sheet Data
balanceSheetURL = 'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=' + ticker + '&apikey=' + apikey
requestBalanceSheetData = requests.get(balanceSheetURL)
balanceSheetData = requestBalanceSheetData.json()
balanceSheetdf = pd.DataFrame(balanceSheetData['annualReports'])
balanceSheetdfLastFive = balanceSheetdf[0:4]

# Clean Up of Balance Sheet Data from Pandas Dataframe, hence forth variable names "BS" means Balance Sheet
BSYear = balanceSheetdfLastFive['fiscalDateEnding']
BSCurrency = balanceSheetdfLastFive['reportedCurrency']

# Assets
BSCashAndCashEqs = balanceSheetdfLastFive['cashAndCashEquivalentsAtCarryingValue']
BSShortTermInvestments = balanceSheetdfLastFive['shortTermInvestments']
BSCashAndShortTermInvestments = balanceSheetdfLastFive['cashAndShortTermInvestments']
BSNetReceivables = balanceSheetdfLastFive['currentNetReceivables'] # ?
BSNetReceivablesPercentOfRevenue = balanceSheetdfLastFive[]
BSInventory = balanceSheetdfLastFive['inventory']
BSInventoryPercentOfRevenue = balanceSheetdfLastFive[]
BSOtherCurrentAssets = balanceSheetdfLastFive['otherCurrentAssets']
BSTotalCurrentAssets = balanceSheetdfLastFive['totalCurrentAssets']

BSPropertyPlantEquipmentNet = balanceSheetdfLastFive['propertyPlantEquipment']
BSGoodwill = balanceSheetdfLastFive['goodwill']
BSIntangibleAssets = balanceSheetdfLastFive['intangibleAssetsExcludingGoodwill']
BSGoodwillAndIntangibleAssets = balanceSheetdfLastFive['intangibleAssets']
BSLongTermInvestments = balanceSheetdfLastFive['longTermInvestments']
BSTaxAssets = balanceSheetdfLastFive[]
BSOtherNonCurrentAssets = balanceSheetdfLastFive['otherNonCurrentAssets']
BSTotalNonCurrentAssets = balanceSheetdfLastFive['totalNonCurrentAssets']

BSOtherAssets = balanceSheetdfLastFive[]
BSTotalAssets = balanceSheetdfLastFive['totalAssets']

# Liabilities
BSAccountPayables = balanceSheetdfLastFive['currentAccountsPayable']
BSAPPercentOfCOGS = balanceSheetdfLastFive[]
BSShortTermDebt = balanceSheetdfLastFive['shortTermDebt']
BSTaxPayables = balanceSheetdfLastFive[]
BSDeferredRevenue = balanceSheetdfLastFive['deferredRevenue']
BSDeferredRevenuePercentOfRevenue = balanceSheetdfLastFive[]
BSOtherCurrentLiabilities = balanceSheetdfLastFive['otherCurrentLiabilities']
BSTotalCurrentLiabilities = balanceSheetdfLastFive['totalCurrentLiabilities']

BSLongTermDebt = balanceSheetdfLastFive['longTermDebt']
BSDeferredRevenueNonCurrent = balanceSheetdfLastFive[]
BSDRNCPercentOfRevenue = balanceSheetdfLastFive[]
BSDeferredTaxLiabilitiesNonCurrent = balanceSheetdfLastFive[]
BSOtherNonCurrentLiabilities = balanceSheetdfLastFive['otherNonCurrentLiabilities']
BSTotalNonCurrentLiabilities = balanceSheetdfLastFive['totalNonCurrentLiabilities']

BSOtherLiabilities = balanceSheetdfLastFive[]
BSTotalLiabilities = balanceSheetdfLastFive['totalLiabilities']

# Stockholders Equity
BSCommonStock = balanceSheetdfLastFive['commonStock']
BSRetainedEarnings = balanceSheetdfLastFive['retainedEarnings']
BSAccumulatedOtherCompIncomeLoss = balanceSheetdfLastFive[]
BSOtherTotalStockholdersEquity = balanceSheetdfLastFive[]
BSTotalStockholdersEquity = balanceSheetdfLastFive['totalShareholderEquity']

BSTotalLiabilitiesAndStockholdersEquity = balanceSheetdfLastFive[]

### Fetch Cash Flow Statement Data 
cashFlowStatementURL = 'https://www.alphavantage.co/query?function=CASH_FLOW&symbol=' + ticker + '&apikey=' + apikey
requestCashFlowStatement = requests.get(cashFlowStatementURL)
cashFlowStatementData = requestCashFlowStatement.json()
cashFlowStatementdf = pd.DataFrame(cashFlowStatementData['annualReports'])
cashFlowStatementdfLastFive = cashFlowStatementdf[0:4]

# Clean Up of Cash Flow Statement Data from Pandas Dataframe, hence forth variable names "CFS" means Cash Flow Statement
CFSYear = cashFlowStatementdfLastFive['fiscalDateEnding']
CFSCurrency = cashFlowStatementdfLastFive['reportedCurrency']

# Operating Activities
CFSNetIncome = cashFlowStatementdfLastFive['netIncome']
CFSDepreciationAndAmortization = cashFlowStatementdfLastFive[]
CFSDAndAPercentOfRevenue = cashFlowStatementdfLastFive[]
CFSDeferredIncomeTax = cashFlowStatementdfLastFive[]
CFSStockBasecCompensation = cashFlowStatementdfLastFive[]
CFSChangeInWorkingCapital = cashFlowStatementdfLastFive[]
CFSAccountsReceivables = cashFlowStatementdfLastFive[]
CFSInventory = cashFlowStatementdfLastFive[]
CFSAccountsPayables = cashFlowStatementdfLastFive[]
CFSOtherWorkingCapital = cashFlowStatementdfLastFive[]
CFSOtherNonCashItems = cashFlowStatementdfLastFive[]
CFSNetCashProvidedByOperatingActivities = cashFlowStatementdfLastFive[]

# Investing Activities
CFSInvestmentsInPropPlantAndEquip = cashFlowStatementdfLastFive[]
CFSAcquisitionsNet = cashFlowStatementdfLastFive[]
CFSPurchasesOfInvestments = cashFlowStatementdfLastFive[]
CFSSalesMaturitiesOfInvestments = cashFlowStatementdfLastFive[]
CFSOtherInvestingActivities = cashFlowStatementdfLastFive[]
CFSNetCashUsedForInvestingActivities = cashFlowStatementdfLastFive[]

# Finanacing Activities
CFSDebtRepayment = cashFlowStatementdfLastFive[]
CFSCommonStockIssued = cashFlowStatementdfLastFive[]
CFSCommonStockRepurchased = cashFlowStatementdfLastFive[]
CFSDividendsPaid = cashFlowStatementdfLastFive[]
CFSOtherFinancingActivities = cashFlowStatementdfLastFive[]
CFSNetCashUsedProvidedByFinancingActivities = cashFlowStatementdfLastFive

CFSEffectOfForexChangesOnCash = cashFlowStatementdfLastFive[]
CFSNetChangeInCash = cashFlowStatementdfLastFive[]

## Write the variables to the DCF Model Excel Sheet
fileName = "DCFModel_" + ticker + ".xlsx"
workbook = xlsxwriter.Workbook(fileName)
worksheet = workbook.add_worksheet('Sheet1')

for i, (year, currency) in enumerate(zip(incomeStatementdfLastFive['fiscalDateEnding'], incomeStatementdfLastFive['reportedCurrency'])):
    worksheet.write(i+1, 1, year)
    worksheet.write(i+1, 1, currency)
workbook.close()
