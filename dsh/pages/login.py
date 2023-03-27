from dash_extensions.enrich import html, dcc


logo_image_path = "assets/gaz_logo.png"

username_input_params = {
    "type": "text",
    "placeholder": "Login",
    "maxLength": "30",
    "name": "username",
    "id": "username",
    "className": "auth_inputs",
}

password_input_params = {
    "type": "password",
    "placeholder": "Password",
    "maxLength": "30",
    "name": "password",
    "id": "password",
    "className": "auth_inputs",
}

button_params = {
    "id": "sign_button",
    "type": "button",
    "className": "auth_inputs",
    "children": "Sign in",
    #"textAlign": "center",
}


def layout(with_error: bool = False):
    if with_error:
        username_input_params["style"] = {"border": "2px solid red"}
        password_input_params["style"] = {"border": "2px solid red"}

    auth_form_div = html.Div(
        id="authorization_block",
        children=[
            html.Form(
                id="authorization_form",
                children=[
                    html.Div(
                        id="logo_block",
                        children=[html.Img(src=logo_image_path, id="image_logo")],
                    ),
                    dcc.Input(**username_input_params),
                    dcc.Input(**password_input_params),
                    html.Button(**button_params),
                ],
            )
        ],
    )
    return auth_form_div
