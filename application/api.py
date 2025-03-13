#pip install requests
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
timeframe = 'DAILY'
ticker = "TSLA"
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={ticker}&datatype=json&apikey=Y5M68XBXFU2HZ9H6'
#url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={ticker}&datatype=json&apikey=KY71PQJ0ICH0O3EY'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={ticker}&datatype=json&apikey=DLYQY88QXZO200NM'
response = requests.get(url)
data = response.json()
# file_path = "output.txt"

metaData = open('metaData.txt', "w")
values = open('values.txt', "w")

metaData.write(str(data['Meta Data']))
values.write(str(data['Time Series (Daily)']))

metaData.close()
values.close()

# print(data['Meta Data'])
# print(data['Time Series (Daily)'])