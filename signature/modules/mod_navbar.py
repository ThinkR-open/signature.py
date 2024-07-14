from shiny import Inputs, Outputs, Session, module, ui


@module.ui
def navbar_ui():
    return (
        ui.tags.nav(
            ui.tags.a("Signature.py", href="/", class_="navbar-brand"),
            class_="navbar navbar-light bg-transparent",
        ),
    )


@module.server
def navbar_server(input: Inputs, output: Outputs, session: Session):
    pass
