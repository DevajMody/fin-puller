from library.finlib import *
import pandas as pd
import os, shutil, csv

def listit():
  a=1


def getit(company):
  c = Company(company)
  path = "data/"
  print(c.check_ticker())
  ex = False
  try:
    os.mkdir(path+company, 0o0755)
    path = path + company + "/"

    try:
      balance_sheet = c.get_balance_sheet()
      balance_sheet.to_csv(path+"BalanceSheet.csv")
      ex = True
    except:
      balance_sheet = 0
    
    try:
      income_statement = c.get_income_statement()
      income_statement.to_csv(path+"IncomeStatement.csv")
      ex = True
    except:
      income_statement = 0
  
    try:
      historical_eps = c.get_historical_eps()
      if historical_eps.shape[0] != 0:
              historical_eps.to_csv(path+"HistoricalEPS.csv")
              ex = True
    except:
      historical_eps = 0

    try:
      historical_data = c.get_price_data()
      historical_data.to_csv(path+"HistoricalData.csv")
      ex = True
    except:
      historical_data = 0

    try:
      l = []
      beta = c.beta()
      pe = c.pe_ratio()
      l.append(["Outstanding Shares",c.outstanding_shares()])
      l.append(["Share Price",c.share_price()])
      l.append(["Market Value",c.market_value()])
      l.append(["EPS",c.earnings_per_share()])
      l.append(["PE Ratio",pe])
      l.append(["Enterprise Value",c.enterprise_value()])
      l.append(["Beta",beta])
      l.append(["Cost of Equity",c.cost_of_equity()])
      l.append(["Short Ratio",c.short_ratio()])

      if beta is not None and pe is not None:
        with open(path+'Figures.csv', 'w') as writeFile:
          writer = csv.writer(writeFile)
          writer.writerows(l)
        writeFile.close()
        ex = True
    except:
      l = 0

    try:
      data = {}
      data["year"] = ["revenue","total expenses","operating expenses","liquid assets","total debt",
                        "tax","interest","depreciation","cost of revenue","total receivables",
                        "total liabilities","total assets","total capital","total equity",
                        "capital expenditures","net income","gross profit","ebit","ebitda","quick ratio",
                        "income from continuing operations margin","net margin","return on assets",
                        "return on capital","return on equity","cash flow operations","free cash flow",
                        "gross profit margin","operating profit margin","net profit margin"]
      for year in range(2016,2020):
        data[year] = [c.revenue(year),c.total_expenses(year),c.operating_expenses(year),c.liquid_assets(year),
                      c.total_debt(year),c.tax(year),c.interest(year),c.depreciation(year),c.cost_of_revenue(year),
                      c.total_receivables(year),c.total_liabilities(year),c.total_assets(year),c.total_capital(year),
                      c.total_equity(year),c.total_equity(year),c.net_income(year),c.gross_profit(year),c.ebit(year),
                      c.ebitda(year),c.quick_ratio(year),c.income_continuing_operations_margin(year),c.net_margin(year),
                      c.return_on_assets(year),c.return_on_capital(year),c.return_on_equity(year),c.cash_flow_operations(year),
                      c.free_cash_flow(year),c.gross_profit_margin(year),c.operating_profit_margin(year),c.net_profit_margin(year)]
      if data[2016][0] is not None or data[2017][0] is not None or data[2017][4] is not None:
        d = pd.DataFrame.from_dict(data)
        d.to_csv(path+"YearWise.csv")
        ex = True

    except:
      data = 0

  
    print("\n")
    if ex is False:
      os.rmdir(path)
    
  except:
    print("Error in "+company)
