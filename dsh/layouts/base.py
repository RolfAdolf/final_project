from dash import html

from dsh.layouts.background import background_div
from dsh.layouts.authorization import auth_form_div


image_path = "assets/back_image.png"


base_div = html.Div(
    id="base",
    children=[
        background_div,
        auth_form_div
    ]
)
