import pandas as pd


def get_final_precision() -> pd.DataFrame:
    """
    This function gets ....
    :return: Dataframe containin ...♠
    """
    df = pd.read_csv('outbound_price_channel.csv')
    #print(df)
    opc_df = df['opc_name'].str.split('-', expand=True)
    precision = pd.concat([opc_df[1], df['cust_precision']], axis=1, join='inner')

    precision = precision[precision[1].str.contains("none|vinni|outbound") == False]
    precision = precision.drop_duplicates(subset=1)
    precision.reset_index(drop=True, inplace=True)
    precision.columns = ['curr_exchanges', 'cust_precision']
    precision_new = precision['curr_exchanges'].str[:-3]
    precision_new = pd.DataFrame(precision_new).reset_index()
    precision_new.columns = ['curr', 'curr_exchanges']
    final_precision_in_my_function = pd.concat([precision_new['curr_exchanges'], precision['cust_precision']], axis=1,
                                               join='inner')
    final_precision_in_my_function.rename(columns={'curr_exchanges': 'symbol'}, inplace=True)
    return final_precision_in_my_function
