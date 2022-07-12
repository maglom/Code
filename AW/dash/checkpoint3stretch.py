import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_excel(r'C:\Users\magnu\Documents\Code\AW\dash\GDP.xlsx')

app = dash.Dash(__name__)

header = html.H1('Checkpoint 3 Dashboard!')

radio_items = dcc.RadioItems(options=[{'label': 'USA', 'value': 0}, {'label': 'Sweden', 'value': 11}, {'label': 'Norway', 'value': 21}], value=0, id='myradio')

my_plot = dcc.Graph(id='plot1')

@app.callback(
    dash.dependencies.Output('plot1', 'figure'),
        dash.dependencies.Input('myradio', 'value'))
def update_plot1(radio_value):
    x_values = df['Country'].loc[radio_value:radio_value+10]
    y_values = df['GDP  (nominal, 2017)'].loc[radio_value:radio_value+10]
    fun_fig = px.bar(x=x_values, y=y_values)
    return(fun_fig)

app.layout = html.Div([header, radio_items, my_plot])

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)

df.tail
