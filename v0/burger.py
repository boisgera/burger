from flet import app, icons
from flet import MainAxisAlignment
from flet import (
    Card,
    Column,
    Container,
    Divider,
    FilledButton,
    IconButton,
    Markdown,
    Row,
    Text,
    TextField,
)
from product import Product


def main(page):
    page.title = "I Can Has Cheezburger?"
    page.window_width = 400
    page.window_height = 430
    page.add(
        Column(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                Row(
                    [
                        Text("🍔", size=50),
                        Text("5.95 €"),
                        Container(width=100, content=TextField(value="0")),
                        IconButton(icon=icons.ADD),
                        IconButton(icon=icons.REMOVE),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [
                        Text("🍟", size=50),
                        Text("3.60 €"),
                        Container(width=100, content=TextField(value="0")),
                        IconButton(icon=icons.ADD),
                        IconButton(icon=icons.REMOVE),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [
                        Text("🥗", size=50),
                        Text("8.30 €"),
                        Container(width=100, content=TextField(value="0")),
                        IconButton(icon=icons.ADD),
                        IconButton(icon=icons.REMOVE),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [
                        Text("🥤", size=50),
                        Text("2.60 €"),
                        Container(width=100, content=TextField(value="0")),
                        IconButton(icon=icons.ADD),
                        IconButton(icon=icons.REMOVE),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Divider(),
                Row(
                    [
                        Card(Container(Markdown("**TOTAL:** 0.00 €"), padding=10)),
                        FilledButton(text="Buy", icon=icons.PAYMENT),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
        )
    )


app(target=main)

