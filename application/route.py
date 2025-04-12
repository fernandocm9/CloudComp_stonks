import requests
import os
import application.apirequest as apirequest
import application.dataplot as dataplot
from application import app
from flask import render_template, request, jsonify, send_file, abort


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
        
        # print(data)
        
        for element in options['bestMatches']:
            if element['4. region'] == 'United States':
                symbol = element['1. symbol']
                break
            
        print(symbol, timeframe)
        apirequest.api_request(symbol,timeframe)
        print('api_request done')
        # symbol_and_data_list = dataplot.extract_data_from_file()
        dataplot.extract_data_from_file()
        print('extract_data_from_file done')
        #dataplot.plot_data_points(symbol)
        return render_template("graph.html", symbol=symbol)
        #return send_file(chart_buffer, mimetype='image/png')
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"error": str(e)}), 500
    
        
'''
@app.route("/graph")
def graph(symbol, timeframe):
    return
'''
@app.route("/chart")
def chart():
    chart_path = os.path.join(os.path.dirname(__file__), 'graph.png')
    if os.path.exists(chart_path):
        return send_file(chart_path, mimetype='image/png')
    else:
        abort(404)
    