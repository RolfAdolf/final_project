from dash_extensions.enrich import html, dcc


def layout(
    username: str = "Username"
):

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
                                    dcc.Upload(id='upload_to_preprocess'),
                                    html.Span(children="Select a csv-file"),
                                    dcc.Download(id="download-preprocessed"),
                                ]
                            )

                        ]
                    )

                ]
            ),

        ],
    )
    return preprocess_div
