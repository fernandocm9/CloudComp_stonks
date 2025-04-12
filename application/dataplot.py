import matplotlib
import json
import re
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import base64
from io import BytesIO
import ast
import os

matplotlib.use('Agg')  # Use non-GUI backend

'''
def extract_data_from_file():
    print('extract_data_from_file function')

    try:
        with open('./application/metaData.txt', "r+") as metadata, open('./application/values.txt', "r+") as data:
            print('opened files')

            metadata_list = metadata.read().split(" ")
            raw_data = data.read()

        # Use regex to extract the first complete dictionary (greedy match from first { to last })
        match = re.search(r"\{.*\}", raw_data, re.DOTALL)
        if not match:
            raise ValueError("No dictionary structure found in values.txt")

        raw_dict_str = match.group(0)

        # Convert Python-style single quotes to JSON-style double quotes safely
        json_compatible = raw_dict_str.replace("'", '"')
        print(json_compatible[:500])

        # Fix keys like "1. open" by ensuring they stay quoted
        json_compatible = re.sub(r'(\d+)\. (\w+)', r'\1. \2', json_compatible)

        # Now parse it
        data_dict = json.loads(json_compatible)

        symbol = metadata_list[12] if len(metadata_list) > 12 else "UNKNOWN"

        plot_data_points([symbol, data_dict])

    except FileNotFoundError:
        print('Error: file not found')
    except PermissionError:
        print('Error: permission error')
    except Exception as e:
        print(f'unexpected error: {e}')


def plot_data_points(data_list):
    print('plot_data_points function')

    try:
        symbol = data_list[0]
        raw_data = data_list[1]

        date, trade_open, trade_high, trade_low, trade_close, trade_volume = [], [], [], [], [], []

        for date_str, values in raw_data.items():
            date.append(date_str)
            trade_open.append(float(values["1. open"]))
            trade_high.append(float(values["2. high"]))
            trade_low.append(float(values["3. low"]))
            trade_close.append(float(values["4. close"]))
            trade_volume.append(int(values["5. volume"]))

        # Construct DataFrame
        df = pd.DataFrame({
            'Date': date[::-1],
            'Open': trade_open[::-1],
            'High': trade_high[::-1],
            'Low': trade_low[::-1],
            'Close': trade_close[::-1],
            'Volume': trade_volume[::-1],
        })

        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        # Plot and save the candlestick chart
        mpf.plot(df, type='candle', volume=True, style='yahoo',
                 title=f"Candlestick chart for {symbol}",
                 savefig='graph.png')
        print("Chart saved as graph.png")

    except Exception as e:
        print(f'unexpected error: {e}')
'''


def extract_data_from_file():
    print('extract_data_from_file function')
    
    try:
        metadata = open('./application/metaData.txt', "r")
        data = open('./application/values.txt', "r+")
            
        
        print('opened files')

        metadata_list = metadata.read().split(" ")
        data_list = data.read().split("}")
        data_list[0] = data_list[0][1:]
        print(len(data_list))
        data_list.pop(-1)
        data_list.pop(-1)


        metadata.close()
        data.close()
        
        symbol = metadata_list[12]

        data_list[0] = data_list[0] + "}"
        for i in range(1, len(data_list)):
            data_list[i] = data_list[i][2:]
            data_list[i] = data_list[i] + "}"

        # Fix the invalid syntax by wrapping each entry in curly braces
        for i in range(len(data_list)):
            data_list[i] = data_list[i].replace("'", '"')  # Replace single quotes with double quotes
            data_list[i] = "{" + data_list[i] + "}"  # Wrap each entry in curly braces
            
        plot_data_points(symbol, data_list)
    except FileNotFoundError:
        print('Error: file not found')
    except PermissionError:
        print('Error: permission error')
    except Exception as e:
        print(f'unexpected error: {e}')
    
    

def plot_data_points(ticker, data_list):
    print('plot_data_points function')
    try:
        symbol = ticker
        date, trade_open, trade_high, trade_low, trade_close, trade_volume = [],[],[],[],[],[]
        for entry in data_list[1:]:
            try:
                data_dict = ast.literal_eval(entry)
                for data, values in data_dict.items():
                    try:
                        pd.to_datetime(data)  # Check if the date is valid
                        date.append(data)
                        trade_open.append(float(values['1. open']))
                        trade_high.append(float(values['2. high']))
                        trade_low.append(float(values['3. low']))
                        trade_close.append(float(values['4. close']))
                        trade_volume.append(int(values['5. volume']))
                    except Exception as e:
                        continue
            except Exception as e:
                continue
        #timeframe_high = max(trade_high)
        #timeframe_low = min(trade_low)

        dataframe = {
            'Date': date[::-1],
            'Open': trade_open[::-1],
            'High': trade_high[::-1],
            'Low': trade_low[::-1],
            'Close': trade_close[::-1],
            'Volume': trade_volume[::-1]
        }


        df = pd.DataFrame(dataframe)
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        print('Trying to plot dataset')

        # Plotting the candlestick chart
        chart_path = os.path.join(os.path.dirname(__file__), 'graph.png')
        fig,_ =mpf.plot(df, type='candle', volume=True, style='yahoo', title="Candlestick chart for " + symbol,returnfig=True)
        fig.savefig(chart_path)
        print("Chart saved as graph.png")
        return chart_path
    except Exception as e:
        print(f'unexpected error: {e}')
    
