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

    accordion.add_item(
        "Business information",
        ui.TagList(
            ui.input_text(
                id="job_title",
                label="Job title",
                placeholder="Data Scientist",
                width="100%",
            ),
            ui.input_text(
                id="email",
                label="Email",
                placeholder="you@thinkr.fr",
                width="100%",
            ),
            ui.input_text(
                id="phone",
                label="Phone number",
                placeholder="+33(0) xx xx xx xx",
                width="100%",
            ),
        ),
    )

    accordion.add_item(
        "Details about this application",
        ui.TagList(
            ui.p(
                "This application is a demonstration of the use of the shiny library with Python."
            ),
            ui.p(
                "You can enter your personal and professional information in the form on the left. Then you can preview the rendering of your signature on the right."
            ),
            ui.p("Then you can copy the signature to your clipboard."),
            ui.a(
                "You can explore the code of this application on GitHub.",
                href="https://github.com/ThinkR-open/signature.py/",
                target="_blank",
            ),
        ),
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
    @reactive.event(
        input.firstname, input.lastname, input.job_title, input.email, input.phone
    )
    def _():
        reactive_values.set(
            {
                "firstname": input.firstname(),
                "lastname": input.lastname(),
                "job_title": input.job_title(),
                "email": input.email(),
                "phone": input.phone(),
            }
        )
