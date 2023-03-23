from dash import html, dcc
from dash_iconify import DashIconify


script_src = 'https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js'

logout_button = {
    'id': 'logout_button',
    'style': {'margin-left': '25.5%', 'height': '6vh'},
    'children': 'Log out'
}

fieldset_style = {
    'margin-bottom': '5%'
}

train_button_style_div = {
    'padding-top': '5%',
    'margin-left': '-1%',
    'margin-bottom': '-5%'
}

if_trained_style = {'display': 'none', 'color': '#2dd61e', 'margin-bottom': '-5%'}


def layout(
    username: str
):
    train_main_div = html.Div(
        id="train_main_div",
        children=[
            html.Div(
                id='block',
                children=[

                    html.Div(
                        id='header',
                        children=[
                            html.Button(id='back_button', children='back'),
                            html.Div(id='train_title', children='Train data')
                        ]
                    ),
                    html.Div(id="preprocess_username", children=username),

                    html.Fieldset(
                        id='train_fieldset',
                        children=[

                            html.Legend('Choose model:'),
                            html.Div(
                                id='columns',
                                children=[

                                    dcc.RadioItems([
                                            {
                                                "label": html.Span(['SVM'], style={'margin-right': '20%', 'font-size': 20}),
                                                "value": "SVM",
                                            },
                                            {
                                                "label": html.Span(['XGBoost'], style={'margin-right': '15%', 'font-size': 20}),
                                                "value": "XGBoost",
                                            },
                                            {
                                                "label": html.Span(['Random forest'], style={'margin-right': '3%', 'font-size': 20}),
                                                "value": "Forest",
                                            },
                                            {
                                                "label": html.Span(['Logistic regression'], style={'margin-right': '0%', 'font-size': 20}),
                                                "value": "Log_Reg",
                                            },
                                        ],
                                        value='SVM',
                                        labelStyle={"display": "flex", "align-items": "center"},
                                        id='models_radio'
                                    )

                                ]
                            )

                        ],
                        style=fieldset_style
                    ),
                    html.Div(id='if_trained', children=html.Label('Model has trained'), style=if_trained_style),
                    html.Div(
                        id='train_button_train_div',
                        children=[
                            dcc.Upload(
                                id='train_button_train',
                                children=[

                                    html.Div([
                                        DashIconify(
                                            icon="ion:sparkles-outline",
                                            width=30,
                                        ),
                                        html.Label('Train model')
                                    ],
                                        style={'padding-top': '5%'}
                                    )

                                ],
                            ),
                            dcc.Download(id="download-preprocessed")
                        ],
                        style=train_button_style_div
                    ),

                    html.Button(**logout_button)

                ]
            ),
            html.Script(type='module', src=script_src)
        ]
    )
    return train_main_div
