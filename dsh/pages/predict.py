from dash import html, dcc
from dash_iconify import DashIconify


if_trained_style = {'display': 'none', 'color': '#2dd61e', 'margin-bottom': '-5%'}

script_src = 'https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js'

logout_button = {
    'id': 'logout_button',
    'style': {'margin-left': '27%', 'height': '6vh'},
    'children': 'Log out'
}


predict_button_style_div = {
    'padding-top': '5%',
    'margin-left': '1%',
    'margin-bottom': '-5%'
}

predict_header_style = {
    'margin-left': '16%'
}


def layout(
    username: str
):
    predict_main_div = html.Div(
        id="predict_main_div",
        children=[
            html.Div(
                id='predict_block',
                children=[

                    html.Div(
                        id='header',
                        children=[
                            html.Button(id='back_button', children='back'),
                            html.Div(id='train_title', children='Predict', style=predict_header_style)
                        ]
                    ),
                    html.Div(id="preprocess_username", children=username),

                    html.Div(
                        id='predict_button_predict_div',
                        children=[
                            dcc.Upload(
                                id='predict_button_predict',
                                children=[

                                    html.Div([
                                        DashIconify(
                                            icon="ion:sparkles-outline",
                                            width=30,
                                        ),
                                        html.Label('Get predictions')
                                    ],
                                        style={'padding-top': '5%'}
                                    )

                                ],
                            ),
                            dcc.Download(id="download-predictions")
                        ],
                        style=predict_button_style_div
                    ),

                    html.Button(**logout_button)

                ]
            ),
            html.Script(type='module', src=script_src)
        ]
    )
    return predict_main_div
