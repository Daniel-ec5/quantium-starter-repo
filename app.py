import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = dash.Dash(__name__)
dates=[]
sales=[]
regions=[]
with open('sorted_data.csv', 'r') as file:
    c=0
    for line in file:
        if c==0:
            c+=1
            continue
        sale,date, region = line.strip().split(',')
        if date < '2021-01-15':
            continue
        else:
            if date in dates:
                sales[len(sales)-1] += float(sale)
                continue
            else:
                dates.append(date)
                sales.append(float(sale))
        regions.append(region)
df=pd.DataFrame({
    'Date': pd.date_range(start='2021-01-15', periods=len(dates), freq='D'),
    'Sales': sales
})
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Sales'],
        mode='lines+markers',
        name='Sales'
    )
) 
app.layout = html.Div([
    html.H1("Pink Morsel Sales after 2021-01-15"),
    dcc.Graph(
        id='line-chart',
        figure=fig
    )
])
if __name__ == '__main__':
    app.run(debug=True)