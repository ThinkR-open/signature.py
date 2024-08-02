import pytest
from signature.modules import mod_form
from shiny.ui import AccordionPanel


def test_accordion():
    panels = mod_form.accordion_panels()
    assert len(panels) == 3
    assert isinstance(panels, list)


@pytest.mark.parametrize(
    "index, expected_title",
    [
        (0, "Personal information"),
        (1, "Business information"),
        (2, "Details about this application"),
    ],
)
def test_accordion_panels(index, expected_title):
    panels = mod_form.accordion_panels()
    assert isinstance(panels[index], AccordionPanel)
    assert panels[index]._title == expected_title
