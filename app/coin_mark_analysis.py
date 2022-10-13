from app.coinmarkapi import get_coinmarketcap_api_data
import pandas as pd
import json
from pandas.io.json import json_normalize



def coin_mark_analysis(refresh_data) -> pd.DataFrame:
    df_coinmarketcap = get_coinmarketcap_api_data(refresh=refresh_data)
    # list_of_quotes = df_coinmarketcap['quote'].tolist()
    # df_list_of_quotes = pd.DataFrame(list_of_quotes)

    first_quote = pd.DataFrame(df_coinmarketcap["quote"].tolist())
    print(first_quote)
    #second_quote = pd.DataFrame([json.loads(item) for item in first_quote.tolist()])
    second_quote = first_quote["EUR"].apply(pd.Series)
    coin_market_data = df_coinmarketcap[['name', 'symbol']]
    coin_price = pd.concat([coin_market_data, second_quote[['price']]], axis=1, join='inner')
    return coin_price
