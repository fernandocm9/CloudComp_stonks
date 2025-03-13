#pip install requests
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={ticker}&datatype=json&apikey=Y5M68XBXFU2HZ9H6'
# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={ticker}&datatype=json&apikey=KY71PQJ0ICH0O3EY'
# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={ticker}&datatype=json&apikey=DLYQY88QXZO200NM'


def api_request(symbol,timeframe):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={symbol}&datatype=json&apikey=DLYQY88QXZO200NM'
    # response = requests.get(url)
    response = requests.get(url)
    data2 = response.json()
    print(data2)
    
    if timeframe == 'DAILY':
        timeframe = 'Daily'
    elif timeframe == 'WEEKLY':
        timeframe = 'Weekly'
    elif timeframe == 'MONTHLY':
        timeframe = 'Monthly'
        
    print(timeframe)
    # file_path = "output.txt"

    metaData = open('./application/metaData.txt', "w")
    values = open('./application/values.txt', "w")

    metaData.write(str(data2['Meta Data']))
    values.write(str(data2[f'Time Series ({timeframe})']))

    metaData.close()
    values.close()
    return 