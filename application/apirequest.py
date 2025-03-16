#pip install requests
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key


def api_request(symbol,timeframe):
    print('api_request function')
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={symbol}&datatype=json&apikey=Y5M68XBXFU2HZ9H6'
    # url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={symbol}&datatype=json&apikey=KY71PQJ0ICH0O3EY'
    # url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={symbol}&datatype=json&apikey=DLYQY88QXZO200NM'
    # response = requests.get(url)
    response = requests.get(url)
    data2 = response.json()
    #print(data2)
    
    if timeframe == 'DAILY':
        timeframe = 'Daily'
    elif timeframe == 'WEEKLY':
        timeframe = 'Weekly'
    elif timeframe == 'MONTHLY':
        timeframe = 'Monthly'
        
    print(timeframe)

    metaData = open('./application/metaData.txt', "r+")
    values = open('./application/values.txt', "r+")

    metaData.write(str(data2['Meta Data']))
    if timeframe == 'Daily':
        values.write(str(data2['Time Series (Daily)']))
    else:
        values.write(str(data2[f'{timeframe} Time Series']))
    

    metaData.close()
    values.close()
    print('created and wrote to files')
    return 