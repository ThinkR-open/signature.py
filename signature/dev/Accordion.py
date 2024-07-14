from shiny import ui


class Accordion:
    """
    Accordion component.
    """

    def __init__(self, id):
        self.id = id
        self.items = []

    def add_item(self, title, content, expanded="false"):
        item_id = f"{self.id}-{len(self.items)}"
        self.items.append((item_id, title, content, expanded))

    def render(self):
        accordion_items = []
        for item_id, title, content, expanded in self.items:
            accordion_items.append(
                ui.div(
                    ui.h2(
                        ui.tags.button(
                            title,
                            class_=f"accordion-button {'collapsed' if expanded == 'false' else ''}",
                            type="button",
                            data_bs_toggle="collapse",
                            data_bs_target=f"#{item_id}",
                            aria_expanded=expanded,
                            aria_controls=item_id,
                        ),
                        class_="accordion-header",
                        id=f"heading-{item_id}",
                    ),
                    ui.div(
                        ui.div(ui.HTML(content), class_="accordion-body"),
                        id=item_id,
                        class_=f"accordion-collapse collapse {'show' if expanded == 'true' else ''}",
                        aria_labelledby=f"heading-{item_id}",
                        data_bs_parent=f"#{self.id}",
                    ),
                    class_="accordion-item",
                )
            )
        return ui.div(*accordion_items, class_="accordion", id=self.id)
