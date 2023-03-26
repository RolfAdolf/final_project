from dash_extensions.enrich import html, dcc

style_graph = {
    "display": "none",
    "height": "30vh",
    "width": "15vw",
    "margin-left": "25%",
    "margin-top": "-30%",
}

logout_button = {
    "id": "logout_button",
    "style": {"margin-left": "25%", "height": "6vh"},
    "children": "Log out",
}


def layout(username: str = "Username"):
    preprocess_div = html.Div(
        id="preprocess_div",
        children=[
            html.Button(id="back_button", children="back"),
            html.Div(id="preprocess_title", children="Preprocess data"),
            html.Div(id="preprocess_username", children=username),
            html.Div(
                id="preprocess_upload",
                children=[
                    html.Form(
                        children=[
                            html.Label(
                                className="input-file",
                                children=[
                                    dcc.Upload(id="upload_to_preprocess"),
                                    html.Span(children="Select a csv-file"),
                                    dcc.Download(id="download-preprocessed"),
                                ],
                            )
                        ]
                    )
                ],
            ),
            dcc.Graph(id="preprocess_graph", figure={}, style=style_graph),
            html.Button(**logout_button),
        ],
    )
    return preprocess_div
