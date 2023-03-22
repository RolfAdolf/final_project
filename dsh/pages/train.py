from dash import html, dcc
from dash_iconify import DashIconify


script_src = 'https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js'


def layout():
    train_main_div = html.Div(
        id="train_main_div",
        children=[
            html.Div(
                id='block',
                children=[

                    html.Div(
                        id='header',
                        children=[
                            html.Button(id='back_button', children='&#8249;'),
                            html.Div(id='title', children='Train data')
                        ]
                    ),
                    html.Button(id='import_button', children='Import data'),

                    html.Fieldset(
                        id='train_fieldset',
                        children=[

                            html.Legend('Choose model:'),
                            html.Div(
                                id='columns',
                                children=[

                                    html.Div(
                                        id='first-column',
                                        children=[

                                            html.Div(
                                                children=[
                                                    dcc.Input(type='radio', id='XGBoost', name='name'),
                                                    html.Label(htmlFor='XGBoost', children='XGBoost')
                                                ]
                                            ),
                                            html.Div(
                                                children=[
                                                    dcc.Input(type='radio', id='LSTM', name='name'),
                                                    html.Label(htmlFor='LSTM', children='LSTM')
                                                ]
                                            ),

                                        ]
                                    ),
                                    html.Div(
                                        id='second-column',
                                        children=[

                                            html.Div(
                                                children=[
                                                    dcc.Input(type='radio', id='SVM', name='name'),
                                                    html.Label(htmlFor='SVM', children='SVM')
                                                ]
                                            ),
                                            html.Div(
                                                children=[
                                                    dcc.Input(type='radio', id='LogReg', name='name'),
                                                    html.Label(htmlFor='LogReg', children='LogReg')
                                                ]
                                            ),

                                        ]
                                    )

                                ]
                            )

                        ]
                    ),

                    html.Button(
                        id='train_button',
                        children=[
                            DashIconify(
                                icon="ion:sparkles-outline",
                                width=30,
                            ),
                            html.Span('Train model')
                        ]
                    ),

                    html.Button(id='logout_button', style={'margin-top': '3%'}, children='Log out')

                ]
            ),
            html.Script(type='module', src=script_src)
        ]
    )
    return train_main_div
