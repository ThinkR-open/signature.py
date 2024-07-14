from shiny import Inputs, Outputs, Session, module, ui, reactive
from dev import Accordion


@module.ui
def form_ui():
    accordion = Accordion.Accordion("myAccordion")

    accordion.add_item(
        "Personal information",
        ui.TagList(
            ui.input_text(
                id="firstname",
                label="First name",
                placeholder="John",
                width="100%",
            ),
            ui.input_text(
                id="lastname",
                label="Last name",
                placeholder="Doe",
                width="100%",
            ),
        ),
        expanded="true",
    )

    return ui.div(
        ui.div(
            accordion.render(),
            class_="container",
        ),
        class_="col-5",
    )


@module.server
def form_server(input: Inputs, output: Outputs, session: Session, reactive_values):
    @reactive.effect
    @reactive.event(input.firstname, input.lastname)
    def _():
        reactive_values.set(
            {"firstname": input.firstname(), "lastname": input.lastname()}
        )
