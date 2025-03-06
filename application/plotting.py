import matplotlib.pyplot as plt
import base64
from io import BytesIO
import mplfinance as mpf
import pandas as pd

data = {
    'Date': ['2025-03-01', '2025-03-02', '2025-03-03', '2025-03-04'],
    'Open': [150, 155, 160, 158],
    'High': [162, 165, 163, 160],
    'Low': [148, 153, 155, 152],
    'Close': [155, 160, 158, 155],
    'Volume': [100, 120, 90, 110]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
tempfile = BytesIO()
mpf.plot(df, type='candle', volume=True, style='yahoo', title='Sample Candlestick Chart',savefig=dict(fname=tempfile, format='png'))



# Encode graph into temporary png file
encoded = base64.b64encode(tempfile.getvalue()).decode('utf-8')
image = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)

# Put it into html 
html =f"""<!DOCTYPE html> 
<html>
<head>
</head>
<body>
    {image}
</body>
</html>
"""
with open('.\\application\\templates\\index.html','w') as f:
    f.write(html)