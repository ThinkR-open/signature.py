from shiny import Inputs, Outputs, Session, module, ui, reactive


def accordion_panels():
    return [
        ui.accordion_panel(
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
        ),
        ui.accordion_panel(
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
        ),
        ui.accordion_panel(
            "Details about this application",
            ui.TagList(
                ui.p(
                    "This application is a demonstration of the use of the shiny library with Python."
                ),
                ui.p(
                    "You can enter your personal and professional information in the form on the left. Then you can preview the rendering of your signature on the right."
                ),
                ui.p("Then you can copy the signature to your clipboard."),
                ui.p("You love this application and you would like to reuse it?"),
                ui.p("Discover how to do it on the GitHub repository."),
                ui.a(
                    "Explore the code of this application on GitHub.",
                    href="https://github.com/ThinkR-open/signature.py/",
                    target="_blank",
                ),
            ),
        ),
    ]


@module.ui
def form_ui():
    return ui.div(
        ui.div(
            ui.accordion(*accordion_panels(), id="myAccordion", multiple=False),
            class_="row",
        ),
        class_="col-lg-5 col-md-12 p-3",
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
