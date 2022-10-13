import pandas as pd
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from app.config.paths import PATH_CMC_PRICE_DATA
from app.config.passwords import coinmarketcap_headers


def get_coinmarketcap_api_data(refresh: bool = False) -> pd.DataFrame:
    """

    :param refresh: [bool] if True: get data from API, if False: get data from local
    :return:
    """

    if refresh:
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '1',
            'limit': '5000',
            'convert': 'Eur',
            'market_cap_max': '100000000000000000',
            'circulating_supply_min': '0',
            'circulating_supply_max': '100000000000000000',
            'percent_change_24h_min': '-100',
            'percent_change_24h_max': '100',
            'sort': 'market_cap',
            'sort_dir': 'desc',
            'cryptocurrency_type': 'all',
        }

        session = Session()
        session.headers.update(coinmarketcap_headers)

        try:
            response = session.get(url, params=parameters)
            data = pd.DataFrame(response.json()['data'])
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            data = pd.DataFrame()
        # data.to_csv(PATH_CMC_PRICE_DATA)
        return data
    else:
        data = pd.read_csv(PATH_CMC_PRICE_DATA)
        return data
