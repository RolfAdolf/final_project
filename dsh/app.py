import requests
from dash import Dash, Input, Output, State

from copy import copy

from dsh.layouts.base import base_div
from dsh.layouts.background import background_div
from dsh.layouts.authorization import return_auth_form_div
from dsh.layouts.personal_office import return_office_form_div, download_button_params
from dsh.callbacks.authorization import authorize
from dsh.callbacks.personal_office import download_data


app = Dash(__name__)

app.layout = base_div

access_token = ""
username = ""
role = ""

@app.callback(
    Output(component_id="base", component_property="children"),
    Input(component_id="sign_button", component_property="n_clicks"),
    State(component_id="username", component_property="value"),
    State(component_id="password", component_property="value")
)
def auth_wrapper(n_clicks, login, password):
    if n_clicks == 0:
        return base_div.children
    try:

        query_result = authorize(login, password)

        global access_token
        global username
        global role

        access_token, username, role = query_result["access_token"], query_result["username"], query_result["role"]

        return [background_div, return_office_form_div(username, role)]
    except requests.exceptions.HTTPError as err:
        return [background_div, return_auth_form_div(with_error=True)]


@app.callback(
    Output(component_id="download_button", component_property="style"),
    Input(component_id="download_button", component_property="n_clicks")
)
def download_wrapper(n_clicks: int):
    if n_clicks == 0:
        return
    global access_token
    download_data(access_token)
    download_button_params["color"] = "#fff"
    return download_button_params
