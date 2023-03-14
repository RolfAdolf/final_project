from dash import html


preprocess_button_params = {
    "type": "button",
    "id": "preprocess_button",
    "className": "buttons",
    "children": "Preprocess data",
    "n_clicks": 0,
}

train_button_params = {
    "type": "button",
    "id": "train_button",
    "className": "buttons",
    "children": "Train data",
    "n_clicks": 0,
}

predict_button_params = {
    "type": "button",
    "id": "predict_button",
    "className": "buttons",
    "children": "Predict data",
    "n_clicks": 0,
}

download_button_params = {
    "type": "button",
    "id": "download_button",
    "className": "buttons",
    "children": "Download data",
    "n_clicks": 0,
}

logout_button_params = {
    "type": "button",
    "id": "logout_button",
    "className": "buttons",
    "children": "Log out",
}


def return_office_form_div(
        username: str = "Username",
        role: str = "viewer"):
    office_form_div = html.Div(
            id="personal_office",
            children=[

                html.Div(
                    id="user_name",
                    children=username
                ),
                html.Div(
                    id="role",
                    children=role
                ),

                html.Div(
                    id="buttons_div",
                    children=[

                        html.Button(**preprocess_button_params),
                        html.Br(),
                        html.Button(**train_button_params),
                        html.Br(),
                        html.Button(**predict_button_params),
                        html.Br(),
                        html.Button(**download_button_params),

                    ]
                ),

                html.Button(**logout_button_params)

            ]
    )
    return office_form_div
