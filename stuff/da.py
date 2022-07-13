import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

header = html.H1('Checkpoint 3 Dashboard!')

numb_slider = dcc.Slider(min=0, max=20, step=1, value=10, id='myslider')

radio_items = dcc.RadioItems(['0', '1','2', '3', '4'], id='myradio')

my_plot = dcc.Graph(id='plot1')

@app.callback(
    dash.dependencies.Output('plot1', 'figure'),
    [
        dash.dependencies.Input('myradio', 'value'),
        dash.dependencies.Input('myslider', 'value')])
def update_plot1(radio_value, slider_value):
    x_values = [0,1,2,3,4]
    y_values = [5,3,2,7,12]
    if radio_value:
        y_values[int(radio_value)] = slider_value
    fun_fig = px.line(x=x_values, y=y_values)
    return(fun_fig)

app.layout = html.Div([header, radio_items, numb_slider, my_plot])

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)