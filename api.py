#pip install requests
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&datatype=json&apikey=Y5M68XBXFU2HZ9H6'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&datatype=json&apikey=DLYQY88QXZO200NM'
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