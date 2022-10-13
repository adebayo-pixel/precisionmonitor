import os


current_file = os.path.dirname(__file__)
PATH_APP = os.path.join(current_file, '..')
PATH_DATA = os.path.join(PATH_APP, 'data')
PATH_CMC_PRICE_DATA = os.path.join(PATH_DATA, 'cmc_prices.csv')
