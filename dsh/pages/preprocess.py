from dash_extensions.enrich import html, dcc


def return_preprocess_data_div(
    username: str = "Username", display: bool = True
):

    preprocess_style = {"display": "block" if display else "none"}

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
                                    dcc.Upload(),
                                    html.Span(children="Select a csv-file")
                                ]
                            )

                        ]
                    )

                ]
            ),

        ],
        style=preprocess_style,
    )
    return preprocess_div
