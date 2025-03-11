from application import app
from flask import render_template, request, jsonify

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/parse_data", methods=['POST'])
def parse_data():
    data = request.json
    symbol = data.get('symbol')
    timefame = data.get('choice')
    options = data.get('api_response')
    
    for element in options['bestMatches']:
        if element['4. region'] == 'United States':
            symbol = element['1. symbol']
            break
    print(symbol, timefame)
        
    return render_template("graph.html")
        
@app.route("/graph")
def graph(symbol, timeframe):
    return
    