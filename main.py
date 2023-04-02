from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
import datetime
import openpyxl

def supstart():
    url = "https://www.boerse.de/insider-trades/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    id(soup)
    requesttxt(url)


def requesttxt(url):
    page = requests.get(url)

def id(soup):
    results = soup.find(id="emsPowerViewContent")
    xx =(results.prettify())
    stocks(results)

def stocks(res):
    data_list = []
    company_list = []
    insider_list= []
    transaction_list = []
    relationship_list = []
    amount_list = []
    Insiderstocks = res.find('table', class_='table')
    rows = Insiderstocks.find_all('tr')
    for row in rows:
        try:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            data_list.append(cols[0])
            company_list.append(cols[1])
            insider_list.append(cols[2])
            transaction_list.append(cols[3])
            relationship_list.append(cols[4])
            amount_list.append(cols[5])
            if len(amount_list) == 96:
                remfirst(data_list, company_list, insider_list, transaction_list, relationship_list, amount_list)
        except IndexError:
            pass


def remfirst(data_list, company_list, insider_list, transaction_list, relationship_list, amount_list):
    del data_list[0], company_list[0], insider_list[0], transaction_list[0], relationship_list[0], amount_list[0]
    topd(data_list, company_list, insider_list, transaction_list, relationship_list, amount_list)
    print(data_list)
    print(company_list)
    print(insider_list)
    print(transaction_list)
    print(relationship_list)
    print(amount_list)


def topd(data_list, company_list, insider_list, transaction_list, relationship_list, amount_list):
    now = datetime.datetime.now()
    columns = ["Datum", "Unternehmen","Meldepflichtiger", "Art", "Stellung", "Volumen"]
    df = pd.DataFrame(list(zip(data_list, company_list, insider_list, transaction_list, relationship_list, amount_list)), columns=columns)
    df.to_excel(f'Stocks{now.strftime("%A")}.xlsx', sheet_name="Insider")
    print(df)

def clusterbuy():
    pass
















supstart()

