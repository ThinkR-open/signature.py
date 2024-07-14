from shiny import App, Inputs, Outputs, Session, ui


app_ui = ui.page_fixed(
    ui.h1("Signature.py"),
)


def server(input: Inputs, output: Outputs, session: Session):
    pass


app = App(app_ui, server, debug=False)
