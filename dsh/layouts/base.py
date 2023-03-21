from dash import html

from dsh.layouts.background import background_div
from dsh.layouts.authorization import return_auth_form_div
from dsh.layouts.personal_office import return_office_form_div
from dsh.layouts.preprocess import return_preprocess_data_div


image_path = "assets/back_image.png"

base_div = html.Div(
    id="base",
    children=[
        background_div,
        return_auth_form_div(with_error=False),
        return_office_form_div(display=False),
        return_preprocess_data_div(display=False)
    ],
)
