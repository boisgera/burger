from flet import app, icons
from flet import MainAxisAlignment
from flet import (
    Card,
    Column,
    Container,
    Divider,
    FilledButton,
    Markdown,
    Row,
)

from product import Product


def main(page):
    page.title = "I Can Has Cheezburger?"
    page.window_width = 400
    page.window_height = 430

    total_markdown = Markdown("**Total:** 0.0 €")

    def on_change(event):
        total = sum([p.total for p in products])
        total_markdown.value = f"**Total:** {total:.2f} €"
        page.update()

    products = [
        Product("🍔", 5.95, on_change=on_change),
        Product("🍟", 3.60, on_change=on_change),
        Product("🥗", 8.30, on_change=on_change),
        Product("🥤", 2.60, on_change=on_change),
    ]

    page.add(
        Column(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                *products,
                Divider(),
                Row(
                    [
                        Card(Container(total_markdown, padding=10)),
                        FilledButton(text="Buy", icon=icons.PAYMENT),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
        )
    )


app(target=main)

