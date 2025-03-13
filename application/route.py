import requests
import application.apirequest as apirequest
import application.dataplot as dataplot
from application import app
from flask import render_template, request, jsonify

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/parse_data", methods=['POST'])
def parse_data():
    try:
        
        data = request.json
        symbol = data.get('symbol')
        timeframe = data.get('choice')
        options = data.get('api_response')
        
        print(data)
        
        for element in options['bestMatches']:
            if element['4. region'] == 'United States':
                symbol = element['1. symbol']
                break
            
        print(symbol, timeframe)
        apirequest.api_request(symbol,timeframe)
        symbol_and_data_list = dataplot.extract_data_from_file()
        dataplot.plot_data_points(symbol_and_data_list)
        return render_template("graph.html")
        
    except:
        print('failed at parsing')
        return None
    
        
        
@app.route("/graph")
def graph(symbol, timeframe):
    return
    