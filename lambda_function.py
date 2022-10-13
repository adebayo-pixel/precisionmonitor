import datetime

from app.tools.encoding_helper import str2file,file2str

# from app.merging import merging
# from app.coin_mark_analysis import coin_mark_analysis
import os
import io
from app.controllers.send_email import send_email

from app.merging import get_actual_precision
from app.config.paths import PATH_DATA


def lambda_handler(event, context):
    start = datetime.datetime.utcnow()
    file_like_object = io.StringIO()
    refresh_cmc_data = True
    results_of_calculation = get_actual_precision(refresh_data=refresh_cmc_data)
    results_of_calculation.to_csv(file_like_object)
    #print(file_like_object.getvalue())
    base64_encoded_file=file2str(file_like_object.getvalue().encode())
    send_email(filename='price_precision.csv',file=base64_encoded_file,address='H.Yusuff@Bankhaus-Scheich.de', subject='Price precision for today')
    stop = datetime.datetime.utcnow()
    delta = stop - start
    print(f"This took {delta}")
    #print(results_of_calculation)


if __name__ == '__main__':
    lambda_handler(None, None)
