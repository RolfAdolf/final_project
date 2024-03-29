from dash_extensions.enrich import html, dcc


preprocess_button_params = {
    "type": "button",
    "id": "preprocess_button",
    "className": "buttons",
    "children": "Preprocess data",
}

train_button_params = {
    "type": "button",
    "id": "train_button",
    "className": "buttons",
    "children": "Train data",
}

predict_button_params = {
    "type": "button",
    "id": "predict_button",
    "className": "buttons",
    "children": "Predict data",
}

download_button_params = {
    "type": "button",
    "id": "download_button",
    "className": "buttons",
    "children": "Download data",
}

logout_button_params = {
    "type": "button",
    "id": "logout_button",
    "className": "buttons",
    "children": "Log out",
}


def layout(username: str, role: str):
    office_form_div = html.Div(
        id="personal_office",
        children=[
            html.Div(id="user_name", children=username),
            html.Div(id="role", children=role),
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
                    dcc.Download(id="download-data"),
                ],
            ),
            html.Button(**logout_button_params),
        ],
    )
    return office_form_div
