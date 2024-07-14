from shiny import App, Inputs, Outputs, Session, ui
from modules import mod_navbar
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

current_dir = Path(__file__).parent

env = Environment(loader=FileSystemLoader(current_dir))

app_ui = ui.page_fixed(
    ui.include_css(current_dir / "css" / "signature.css"),
    mod_navbar.navbar_ui("nav_signature"),
)


def server(input: Inputs, output: Outputs, session: Session):
    pass


app = App(app_ui, server, debug=False)
