import requests
from application import app
from flask import render_template, request, jsonify

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/parse_data", methods=['POST'])
def parse_data():
    data = request.json
    symbol = data.get('symbol')
    timeframe = data.get('choice')
    options = data.get('api_response')
    
    for element in options['bestMatches']:
        if element['4. region'] == 'United States':
            symbol = element['1. symbol']
            break
    print(symbol, timeframe)

    
    # url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={symbol}&datatype=json&apikey=Y5M68XBXFU2HZ9H6'
    # url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={symbol}&datatype=json&apikey=KY71PQJ0ICH0O3EY'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{timeframe}&symbol={symbol}&datatype=json&apikey=DLYQY88QXZO200NM'
    # response = requests.get(url)
    response = requests.get(url)
    data2 = response.json()
    print(data2)
    # file_path = "output.txt"

    metaData = open('metaData.txt', "w")
    values = open('values.txt', "w")

    #metaData.write(str(data2['Meta Data']))
    #values.write(str(data2['Time Series {timeframe}']))

    metaData.close()
    values.close()
    
        
    return render_template("graph.html")
        
@app.route("/graph")
def graph(symbol, timeframe):
    return
    