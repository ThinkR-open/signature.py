from shiny import App, Inputs, Outputs, Session, ui, reactive
from modules import mod_navbar, mod_form, mod_preview
from pathlib import Path

current_dir = Path(__file__).parent

app_ui = ui.page_fixed(
    ui.head_content(
        ui.tags.title("signature.py"),
        ui.tags.script(
            src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.5.10/clipboard.min.js",
        ),
        ui.tags.script(
            src="https://www.googletagmanager.com/gtag/js?id=G-SPE51YQFS7",
            async_=True,
        ),
        ui.tags.link(
            rel="icon",
            href="favicon.svg",
        ),
        ui.tags.script(
            """
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());

            gtag('config', 'G-SPE51YQFS7');
            """,
        ),
    ),
    ui.include_css(current_dir / "css" / "signature.css"),
    ui.include_js(current_dir / "js" / "signature.js"),
    mod_navbar.navbar_ui("nav_signature"),
    ui.div(
        ui.div(
            mod_form.form_ui("form_signature"),
            mod_preview.preview_ui("preview_signature"),
            class_="row",
        ),
        class_="container",
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    reactive_values = reactive.Value(
        {
            "firstname",
            "lastname",
            "jobtitle",
            "email",
            "email_url",
            "phone",
            "phone_url",
        }
    )

    mod_form.form_server("form_signature", reactive_values=reactive_values)
    mod_preview.preview_server(
        "preview_signature", current_dir=current_dir, reactive_values=reactive_values
    )


app = App(app_ui, server, static_assets=current_dir / "assets", debug=False)
