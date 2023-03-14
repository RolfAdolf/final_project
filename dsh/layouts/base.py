from dash import html

from dsh.layouts.background import background_div
from dsh.layouts.authorization import return_auth_form_div


image_path = "assets/back_image.png"

base_div = html.Div(
    id="base",
    children=[
        background_div,
        return_auth_form_div(with_error=False)
    ]
)
