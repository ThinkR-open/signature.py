from shiny.run import ShinyAppProc
from playwright.sync_api import Page, expect
from shiny.pytest import create_app_fixture

app = create_app_fixture("../../app.py")


def test_signature(page: Page, app: ShinyAppProc):
    page.goto(app.url)
    response = page.request.get(app.url)
    expect(response).to_be_ok()
    expect(page).to_have_title("signature.py")


def test_signature_dark_mode(page: Page, app: ShinyAppProc):
    page.goto(app.url)
    expect(page.locator("html")).to_have_attribute("data-bs-theme", "light")
    page.get_by_test_id("darkmode-input").click()
    expect(page.locator("html")).to_have_attribute("data-bs-theme", "dark")


def test_signature_form(page: Page, app: ShinyAppProc):
    page.goto(app.url)
    expect(page.get_by_test_id("signature-names")).to_contain_text(
        "{{firstname}} {{lastname}}"
    )
    page.get_by_label("First name").fill("Arthur")
    expect(page.get_by_test_id("signature-names")).to_contain_text(
        "Arthur {{lastname}}"
    )
    page.get_by_label("Last name").fill("Bréant")
    expect(page.get_by_test_id("signature-names")).to_contain_text("Arthur Bréant")
    page.get_by_role("button", name="Business information").click()
    page.get_by_label("Job title").fill("Secret agent")
    expect(page.get_by_test_id("signature-job")).to_contain_text("Secret agent")
    page.get_by_label("Email").fill("arthur@thinkr.fr")
    expect(page.get_by_test_id("signature-email")).to_contain_text("arthur@thinkr.fr")
    page.get_by_label("Phone number").fill("+33(0) 6 00 00 00 00")
    expect(page.get_by_test_id("signature-phone")).to_contain_text(
        "+33(0) 6 00 00 00 00"
    )
    copy_button = page.get_by_test_id("copy-button")
    copy_button.click()
    expect(copy_button).to_be_disabled()
    expect(page.locator("#shiny-notification-panel")).to_be_visible()
