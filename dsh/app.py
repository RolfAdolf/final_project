from dash import Dash, dcc, html, Output, Input, State
from dash.exceptions import PreventUpdate

import requests

from dsh.utils.background import background_div
from dsh.pages import login, office, not_found_404
from dsh.utils.authorize import authorize


app = Dash(name=__name__)

app.layout = html.Div(
    id='base_layout',
    children=[
        background_div,
        dcc.Store(id='user_json_data', storage_type='session'),
        html.Div(id='content-container'),
        html.Div(id='login_reference'),
        dcc.Location(id='url', refresh=False)
    ],
)


@app.callback(
    Output('content-container', 'children'),
    Input('url', 'pathname'),
    State('user_json_data', 'data')
)
def display_page(pathname, user_data):
    if user_data is None:
        return login.layout()
    if not (user_data.get("username", False) and user_data.get("password", False)):
        return login.layout(with_error=True)
    else:
        authorization_result = authorize(user_data["username"], user_data["password"])
        username, role = authorization_result["username"], authorization_result["role"]

    if pathname == '/' or pathname == '/office':
        return office.layout(username, role)
    if pathname == '/login':
        return login.layout()
    return not_found_404.layout


@app.callback(
    [Output('user_json_data', 'data'), Output('login_reference', 'children')],
    Input(component_id='sign_button', component_property='n_clicks'),
    State(component_id='username', component_property='value'),
    State(component_id='password', component_property='value'),
    State(component_id='user_json_data', component_property='data')
)
def auth_wrapper(n_clicks, user_login, password, user_data):
    if n_clicks == 0:
        raise PreventUpdate()
    try:
        query_result = authorize(user_login, password)

        user_data = {}
        user_data["username"] = query_result['username']
        user_data["password"] = password

        return user_data, dcc.Location(pathname='/office', id='authorized')

    except requests.exceptions.HTTPError:
        return user_data, dcc.Location(pathname='/', id='retry_authorization')





































# @app.callback(
#     Output(component_id='base', component_property='children'),
#     Input(component_id='sign_button', component_property='n_clicks'),
#     State(component_id='username', component_property='value'),
#     State(component_id='password', component_property='value'),
# )
# def auth_wrapper(n_clicks, login, password):
#     print(n_clicks, login, password)
#     if n_clicks == 0:
#         raise PreventUpdate()
#     try:
#         query_result = authorize(login, password)
#
#         global access_token
#         global username
#         global role
#
#         access_token, username, role = (
#             query_result['access_token'],
#             query_result['username'],
#             query_result['role'],
#         )
#
#         return [background_div, return_office_form_div(username, role)]
#     except requests.exceptions.HTTPError:
#         return [background_div, return_auth_form_div(with_error=True)]
#
#
# @app.callback(
#     Output(component_id='download-data', component_property='data'),
#     Input(component_id='download_button', component_property='n_clicks'),
# )
# def download_wrapper(n_clicks: int):
#     print('Download:', n_clicks)
#     if n_clicks == 0:
#         raise PreventUpdate()
#     global access_token
#     return dcc.send_data_frame(download_data(access_token), 'data.csv')
#
#
# @app.callback(
#     Output(component_id='base', component_property='children'),
#     Input(component_id='preprocess_button', component_property='n_clicks')
# )
# def preprocess_menu(n_clicks: int):
#     print('Preprocess:', n_clicks)
#     if n_clicks == 0:
#         raise PreventUpdate()
#     global username
#     return [background_div, return_preprocess_data_div(username, display=True)]
