from shiny import App, Inputs, Outputs, Session, ui
from modules import mod_navbar

app_ui = ui.page_fixed(
    mod_navbar.navbar_ui("nav_signature"),
)


def server(input: Inputs, output: Outputs, session: Session):
    pass


app = App(app_ui, server, debug=False)
