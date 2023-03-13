import requests
from dash import Dash, Input, Output, State

from dsh.layouts.base import base_div
from dsh.callbacks.authorization import authorize

app = Dash(__name__)

app.layout = base_div


@app.callback(
    Output(component_id="base", component_property="children"),
    Input(component_id="sign_button", component_property="n_clicks"),
    State(component_id="username", component_property="value"),
    State(component_id="password", component_property="value")
)
def auth_wrapper(n_clicks, username, password):
    if n_clicks == 0:
        return base_div.children
    try:
        request = authorize(username, password)
        request.raise_for_status()
        return request.text
    except requests.exceptions.HTTPError as err:
        print(SystemExit(err))
