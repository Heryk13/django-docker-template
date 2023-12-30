import dash
from dash import dcc, html
import dpd_components as dpd
from django_plotly_dash import DjangoDash
from django_plotly_dash.consumers import send_to_pipe_channel

app = DjangoDash('SimpleExample')   # replaces dash.Dash

app.layout = html.Div([
    html.Button(id='output-color'),
    dpd.Pipe(id="named_count_pipe",               # ID in callback
            value=None,                          # Initial value prior to any message
            label="named_counts",                # Label used to identify relevant messages
            channel_name="live_button_counter")
])

@app.callback(
    dash.dependencies.Output('output-color', 'children', allow_duplicate=True),
    [dash.dependencies.Input('output-color', 'n_clicks')],
    prevent_initial_call=True)
def callback_color(dropdown_value):
    if dropdown_value:
        send_to_pipe_channel(channel_name="live_button_counter",
                        label="named_counts",
                        value={"message": "Hello World"})
    return dash.no_update

@app.callback(
    dash.dependencies.Output('output-color', 'children'),
    [dash.dependencies.Input('named_count_pipe', 'value')],
    prevent_initial_call=True)
def callback_color(dropdown_value):
    if dropdown_value:
        print("faffafafafafaffa")
        return "hellow World"
    return dash.no_update