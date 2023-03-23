# from dash import Dash, dcc, html, Output, Input, State
from dash_extensions.enrich import DashProxy, dcc, html, Output, Input, State, MultiplexerTransform
from dash.exceptions import PreventUpdate

import requests
from typing import Dict, Optional

from dsh.utils.background import background_div
from dsh.pages import login, office, not_found_404, preprocess, train, predict
from dsh.utils.authorize import authorize
from dsh.utils.download_data import download_data
from dsh.utils.preprocess_data import preprocess_data
from dsh.utils.train_model import train_model_request
from dsh.utils.predict import get_predict_data


# app = Dash(name=__name__)

app = DashProxy(name=__name__, transforms=[MultiplexerTransform()])

app.layout = html.Div(
    id='base_layout',
    children=[
        background_div,
        dcc.Store(id='user_json_data', storage_type='session'),
        html.Div(id='content-container'),
        html.Div(id='login_reference'),
        html.Div(id='logout_reference'),
        html.Div(id='preprocess_reference'),
        html.Div(id='train_reference'),
        html.Div(id='predict_reference'),
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
    if not (user_data.get('username', False) and user_data.get('password', False)):
        return login.layout()
    else:
        try:
            authorization_result = authorize(user_data["username"], user_data["password"])
            username, role = authorization_result["username"], authorization_result["role"]
        except requests.exceptions.HTTPError:
            return login.layout(with_error=True)

    if pathname == '/' or pathname == '/office':
        return office.layout(username, role)
    if pathname == '/login':
        return login.layout()
    if pathname == '/preprocess':
        return preprocess.layout(username)
    if pathname == '/train':
        return train.layout(username=username)
    if pathname == '/predict':
        return predict.layout(username=username)
    return not_found_404.layout


@app.callback(
    [Output('user_json_data', 'data'), Output('login_reference', 'children')],
    Input(component_id='sign_button', component_property='n_clicks'),
    State(component_id='username', component_property='value'),
    State(component_id='password', component_property='value'),
    State(component_id='user_json_data', component_property='data')
)
def auth_wrapper(n_clicks, user_login, password, user_data):
    if n_clicks is None:
        raise PreventUpdate()
    try:
        query_result = authorize(user_login, password)

        return {'username': query_result['username'], 'password': password}, \
                dcc.Location(pathname='/office', id='authorized')

    except requests.exceptions.HTTPError:
        return {}, dcc.Location(pathname='/login', id='retry_authorization')


@app.callback(
    Output(component_id='download-data', component_property='data'),
    Input(component_id='download_button', component_property='n_clicks'),
    State(component_id='user_json_data', component_property='data')
)
def download_wrapper(n_clicks: int, user_data):
    if n_clicks is None:
        raise PreventUpdate()
    if user_data is None:
        return dcc.Location(pathname='/login', id="can't download")
    if not (user_data.get("username", False) and user_data.get("password", False)):
        return dcc.Location(pathname='/login', id="can't download")
    try:
        user_login, password = user_data["username"], user_data["password"]
        access_token = authorize(user_login, password)["access_token"]

        return dcc.send_data_frame(download_data(access_token), 'data.csv')

    except requests.exceptions.HTTPError:
        try:
            access_token = authorize(user_login, password)["access_token"]
            return dcc.send_data_frame(download_data(access_token), 'data.csv')
        except requests.exceptions.HTTPError:
            return dcc.Location(pathname='/', id='retry_authorization')


@app.callback(
    [Output('user_json_data', 'data'), Output('logout_reference', 'children')],
    Input(component_id='logout_button', component_property='n_clicks'),
    State(component_id='user_json_data', component_property='data')
)
def log_out(n_clicks: int, user_data: Dict):
    if n_clicks is None:
        raise PreventUpdate()
    return {}, dcc.Location(pathname='/login', id='log_out')


@app.callback(
    Output('preprocess_reference', 'children'),
    Input('preprocess_button', 'n_clicks')
)
def go_preprocess(n_clicks: int):
    if n_clicks is None:
        raise PreventUpdate()
    return dcc.Location(pathname='/preprocess', id='go_preprocess')


@app.callback(
    Output('preprocess_reference', 'children'),
    Input('back_button', 'n_clicks')
)
def back_from_preprocess(n_clicks: int):
    if n_clicks is None:
        raise PreventUpdate()
    return dcc.Location(pathname='/', id='return_from_preprocess')


@app.callback(
    Output(component_id='download-preprocessed', component_property='data'),
    Input('upload_to_preprocess', 'contents'),
    State('upload_to_preprocess', 'filename'),
    State(component_id='user_json_data', component_property='data')
)
def download_preprocessed_data(file: Optional[str], filename: str, user_data: Dict):
    print("FILE PREPROCESS")
    print(type(file))
    print(user_data)
    if file is None:
        raise PreventUpdate()
    try:
        preprocessed_data = preprocess_data(file, filename, user_data['username'], user_data['password'])
        return dcc.send_data_frame(preprocessed_data, 'preprocessed_data.csv')
    except requests.exceptions.HTTPError:
        return dcc.Location(pathname='/office', id='retry_authorization')


@app.callback(
    Output('train_reference', 'children'),
    Input('train_button', 'n_clicks')
)
def back_from_preprocess(n_clicks: int):
    if n_clicks is None:
        raise PreventUpdate()
    return dcc.Location(pathname='/train', id='go_train')


@app.callback(
    Output(component_id='if_trained', component_property='style'),
    Input(component_id='train_button_train', component_property='contents'),
    State(component_id='train_button_train', component_property='filename'),
    State(component_id='models_radio', component_property='value'),
    State(component_id='user_json_data', component_property='data')
)
def train_model_menu(file: str, filename: str, model_type: str, user_data: Dict):
    if file is None:
        raise PreventUpdate()
    try:
        train_model_request(file, filename, model_type, user_data['username'], user_data['password'])
    except requests.exceptions.HTTPError:
        return dcc.Location(pathname='/login', id='authorization_problems')
    style = dict(train.if_trained_style)
    style['display'] = 'block'
    return style


@app.callback(
    Output('predict_reference', 'children'),
    Input('predict_button', 'n_clicks')
)
def back_from_preprocess(n_clicks: int):
    if n_clicks is None:
        raise PreventUpdate()
    return dcc.Location(pathname='/predict', id='go_predict')


@app.callback(
    Output('download-predictions', 'data'),
    Input('predict_button_predict', 'contents'),
    State('predict_button_predict', 'filename'),
    State('user_json_data', 'data')
)
def get_predict(file: str, filename: str, user_data: Dict):
    if file is None:
        raise PreventUpdate()
    try:
        return dcc.send_data_frame(
            get_predict_data(file, filename, user_data['username'], user_data['password']),
            'predictions.csv'
        )
    except requests.exceptions.HTTPError:
        return dcc.Location(pathname='/login', id='authorization_problems')
