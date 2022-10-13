from app.tools.text import get_final_precision
import math
import pandas as pd
from app.coin_mark_analysis import coin_mark_analysis


def precision(today_price):
    results = []
    for x in today_price['price']:
        k = max(2, math.floor(-math.log10(x)) + 6)
        results.append(k)
    return results


def comparison(row):
    if row['cust_precision'] == row['precision']:
        return 'right'
    else:
        return 'wrong'


def get_actual_precision(refresh_data) -> pd.DataFrame:
    final_precision = get_final_precision()
    coin_price = coin_mark_analysis(refresh_data)
    merge = pd.merge(final_precision, coin_price, on='symbol')
    merge = merge.drop_duplicates(subset='name')
    merge.reset_index(drop=True, inplace=True)
    today_price = merge[merge["name"].str.contains(
        "Xeno Token|UNICORN Token|Stox|Wrapped Solana|Rune|Alpha Coin|STEPN|Hydro Protocol|NFTX Hashmasks Index|MIR COIN|Wormhole|HyperOne|ERC20|OMEGA FINANCE|Aavegotchi ALPHA") == False]
    today_price.reset_index(drop=True, inplace=True)

    r = precision(today_price)
    new_data = pd.DataFrame(r, columns=['precision'])
    actual_precision = pd.concat([today_price, new_data], axis=1, join='inner')
    actual_precision['compare'] = actual_precision.apply(lambda row: comparison(row), axis=1)
    return actual_precision
