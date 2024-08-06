import pytest
from signature.modules import mod_form
from shiny.ui import AccordionPanel


def test_accordion():
    panels = mod_form.accordion_panels()
    assert len(panels) == 3
    assert isinstance(panels, list)


@pytest.mark.parametrize(
    "panel_index, expected_title",
    [
        (0, "Personal information"),
        (1, "Business information"),
        (2, "Details about this application"),
    ],
)
def test_accordion_panels(panel_index, expected_title):
    panels = mod_form.accordion_panels()
    assert isinstance(panels[panel_index], AccordionPanel)
    assert panels[panel_index]._title == expected_title


@pytest.mark.parametrize(
    "panel_index, input_index, input_name",
    [
        (0, 0, "firstname"),
        (0, 1, "lastname"),
        (1, 0, "job_title"),
        (1, 1, "email"),
        (1, 2, "phone"),
    ],
)
def test_accordion_panels_content(panel_index, input_index, input_name):
    panels = mod_form.accordion_panels()
    panel = panels[panel_index]._args[0]
    assert isinstance(panel, list)
    assert (
        panel[input_index].children[1].name == "input"
    ), f"Expected input but got {panel[input_index].children[1].name}"
    assert (
        panel[input_index].children[1].attrs.get("id") == input_name
    ), f"Expected {input_name} but got {panel[input_index].children[1].attrs.get('id')}"
