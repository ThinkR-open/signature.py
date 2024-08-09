from shiny import Inputs, Outputs, Session, module, ui, render, reactive
from faicons import icon_svg
from jinja2 import Environment, FileSystemLoader
import asyncio


@module.ui
def preview_ui():
    return (
        ui.div(
            ui.div(
                ui.div(
                    ui.div(
                        ui.div(
                            ui.div(class_="close"),
                            ui.div(class_="minimize"),
                            ui.div(class_="zoom"),
                            class_="buttons",
                        ),
                        class_="card-header bg-ligth",
                    ),
                    ui.div(
                        ui.div(
                            ui.p("Hello the team!"),
                            ui.p("You can edit your signature from this interface."),
                            ui.p(
                                "Then you'll just have to insert it as your signature."
                            ),
                            ui.HTML("Thank you &#128513"),
                            id="intro",
                        ),
                        ui.div(
                            ui.output_ui("render_template"),
                            id="signature",
                        ),
                        class_="card-body row gy-4",
                    ),
                    ui.div(
                        ui.input_task_button(
                            id="copy",
                            label="Copy to clipboard",
                            icon=icon_svg("copy"),
                            width="100%",
                            class_="btn-info btn-md",
                            label_busy="Copied!",
                            icon_busy=icon_svg("check"),
                            data_clipboard_target="#signature",
                            data_testid="copy-button",
                        ),
                        class_="card-footer bg-transparent border-top-0",
                    ),
                ),
                class_="card",
            ),
            class_="col-lg-7 col-md-12 p-3",
        ),
    )


@module.server
def preview_server(
    input: Inputs, output: Outputs, session: Session, current_dir, reactive_values
):
    env = Environment(loader=FileSystemLoader(current_dir))
    template = env.get_template("template/template.html")

    @render.text
    def render_template() -> str:
        print(reactive_values())

        first_name = reactive_values().get("firstname")
        last_name = reactive_values().get("lastname")
        job_title = reactive_values().get("job_title")
        email = reactive_values().get("email")
        email_url = reactive_values().get("email_url")
        phone = reactive_values().get("phone")
        phone_url = reactive_values().get("phone_url")

        rendered_template = template.render(
            firstname="{{firstname}}" if first_name == "" else first_name,
            lastname="{{lastname}}" if last_name == "" else last_name,
            job_title="{{job_title}}" if job_title == "" else job_title,
            email="{{email}}" if email == "" else email,
            phone="{{phone}}" if phone == "" else phone,
            email_url="{{email_url}}" if email_url == "" else email_url,
            phone_url="{{phone_url}}" if phone_url == "" else phone_url,
        )
        return rendered_template

    @reactive.effect
    @reactive.event(input.copy)
    async def _() -> None:
        await asyncio.sleep(0.75)
        ui.notification_show(
            "Paste the signature in your email client",
            id="copy",
            type="default",
            duration=5,
        )
