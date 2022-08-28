import pandas as pd
import aiohttp
import asyncio
import nest_asyncio
import requests
from bs4 import BeautifulSoup as bs
import os, sys

parent_dir = os.path.abspath('..')
forex_file = parent_dir + '\data\currencies.csv'

nest_asyncio.apply()

async def getDetailExchangeRateFor(symbol: str) -> list[dict]:
        """Get all exchange for currency"""
        url = f'https://finance.yahoo.com/quote/{symbol}%3DX?p={symbol}%3DX'
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    r = await response.text()
                    soup = bs(r, "lxml")

                    currency = {}
                    currency['symbol'] = symbol
                    marketPrice = soup.find_all(attrs={"data-test": "qsp-price"})
                    currency['regularMarketPrice'] = marketPrice[0].text if len(marketPrice) > 0 else ""

                    marketChange = soup.find_all(attrs={"data-test": "qsp-price-change"})
                    currency['regularMarketChange'] = marketChange[0].text if len(marketChange) > 0 else ""

                    marketChangePercent = soup.find_all("fin-streamer", class_="Fw(500) Pstart(8px) Fz(24px)")
                    currency['regularMarketChangePercent'] = marketChangePercent[1].text if len(marketChangePercent) > 1 else ""

                    leftSummaryTable = soup.find_all(attrs={"data-test": "left-summary-table"})
                    if leftSummaryTable is None:
                        currency['previous_close'] = ''
                        currency['open'] = ''
                        currency['bid'] = ''
                    else:
                        if len(leftSummaryTable) > 0:
                            row = leftSummaryTable[0].findAll("tr")
                            currency_value = [[td for td in tr] for tr in row]
                            currency['previous_close'] = currency_value[0][1].text
                            currency['open'] = currency_value[1][1].text
                            currency['bid'] = currency_value[2][1].text

                    rightSummaryTable = soup.find_all(attrs={"data-test": "right-summary-table"})
                    if rightSummaryTable is None:
                        currency['day_range'] = ''
                        currency['year_Week_range'] = ''
                        currency['ask'] = ''
                    else:
                        if len(rightSummaryTable) > 0:
                            row = rightSummaryTable[0].findAll("tr")
                            currency_value = [[td for td in tr] for tr in row]
                            currency['day_range'] = currency_value[0][1].text
                            currency['year_Week_range'] = currency_value[1][1].text
                            currency['ask'] = currency_value[2][1].text                       

                    return currency

        except requests.exceptions.Timeout:
            print("Timeout occurred")

def getAllDetailExchangeRateFor(symbols: list[dict]) -> list[dict]:
    loop = asyncio.get_event_loop()
    coroutines = [getDetailExchangeRateFor(symbol) for symbol in symbols]
    L = asyncio.gather(*coroutines)
    results = loop.run_until_complete(L)
    return results
