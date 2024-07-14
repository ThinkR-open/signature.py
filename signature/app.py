from shiny import App, Inputs, Outputs, Session, ui, reactive
from modules import mod_navbar, mod_form, mod_preview
from pathlib import Path

current_dir = Path(__file__).parent

app_ui = ui.page_fixed(
    ui.include_css(current_dir / "css" / "signature.css"),
    mod_navbar.navbar_ui("nav_signature"),
    ui.div(
        ui.div(
            mod_form.form_ui("form_signature"),
            mod_preview.preview_ui("preview_signature"),
            class_="row gx-5",
        ),
        class_="container",
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    reactive_values = reactive.Value({"firstname", "lastname"})

    mod_form.form_server("form_signature", reactive_values=reactive_values)
    mod_preview.preview_server(
        "preview_signature", current_dir=current_dir, reactive_values=reactive_values
    )


app = App(app_ui, server, debug=False)
