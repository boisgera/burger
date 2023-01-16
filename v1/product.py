from flet import icons
from flet import MainAxisAlignment
from flet import IconButton, Container, Row, Text, TextField, UserControl


class Product(UserControl):
    def __init__(self, emoji, price):
        super().__init__()
        self.price = price
        self.emoji = emoji

    def build(self):
        return Row(
            [
                Text(self.emoji, size=50),
                Text(f"{self.price:.2f} €"),
                Container(width=100, content=TextField(value="0")),
                IconButton(icon=icons.ADD),
                IconButton(icon=icons.REMOVE),
            ],
            alignment=MainAxisAlignment.CENTER,
        )
