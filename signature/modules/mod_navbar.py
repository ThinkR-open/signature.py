from shiny import Inputs, Outputs, Session, module, ui


@module.ui
def navbar_ui():
    return (
        ui.tags.nav(
            ui.div(
                ui.tags.a("Signature.py", href="/", class_="navbar-brand"),
                ui.input_dark_mode(
                    data_testid="darkmode-input",
                ),
                class_="container-fluid",
            ),
            class_="navbar navbar-light bg-transparent",
        ),
    )


@module.server
def navbar_server(input: Inputs, output: Outputs, session: Session):
    pass
