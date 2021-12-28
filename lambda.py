# import urllib library
from urllib.request import urlopen
import pandas as pd
# import json
import json
# store the URL in url a

s3 = boto3.client('s3')

def lambda_handler(event, context):
	bucket ='aws-simplified-transactions420'
	
	url = 'https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json'
    response = urlopen(url)
    data_json = json.loads(response.read())

    df = pd.DataFrame(data_json)
    
    fileName = 'data' + '.csv'

	uploadByteStream = bytes(df.to_csv(data.csv, sep='\t', encoding='utf-8'))

	s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)

	print('Put Complete')