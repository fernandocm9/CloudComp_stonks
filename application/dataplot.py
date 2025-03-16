import matplotlib
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import base64
from io import BytesIO
matplotlib.use('Agg')


def extract_data_from_file():
    print('extract_data_from_file function')
    
    try:
        metadata = open('./application/metaData.txt', "r+")
        data = open('./application/values.txt', "r+")
            
        
        print('opened files')

        metadata_list = metadata.read().split(" ")
        data_list = data.read().split("}")
        data_list[0] = data_list[0][1:]
        data_list.pop(-1)
        data_list.pop(-1)


        metadata.close()
        data.close()
        
        symbol = metadata_list[12]
        
        plot_data_points([symbol, data_list])
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
        count = 0
        date, trade_open, trade_high, trade_low, trade_close, trade_volume = [],[],[],[],[],[]
        for entry in data_list[1]:
            temp = entry.split(" ")
            if count > 0:
                temp.pop(0)
            date.append(temp[0][1:-1])
            trade_open.append(float(temp[3][1:-2]))
            trade_high.append(float(temp[6][1:-2]))
            trade_low.append(float(temp[9][1:-2]))
            trade_close.append(float(temp[12][1:-2]))
            trade_volume.append(int(temp[15][1:-2]))
            count += 1
        timeframe_high = max(trade_high)
        timeframe_low = min(trade_low)

        data = {
            'Date': date[::-1],
            'Open': trade_open[::-1],
            'High': trade_high[::-1],
            'Low': trade_low[::-1],
            'Close': trade_close[::-1],
            'Volume': trade_volume[::-1],
        }


        df = pd.DataFrame(data)
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        # Plotting the candlestick chart
        graph = BytesIO()
        mpf.plot(df, type='candle', volume=True, style='yahoo', title="Candlestick chart for " + symbol, savefig="graph.png")
    except Exception as e:
        print(f'unexpected error: {e}')
    
