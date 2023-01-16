from flet import icons
from flet import MainAxisAlignment
from flet import IconButton, Container, Row, Text, TextField, UserControl


def do_nothing(event):
    pass


class Product(UserControl):
    def __init__(self, emoji, price, on_change=None):
        super().__init__()
        self.price = price
        self.emoji = emoji
        self.quantity = 0
        self.on_change = on_change or do_nothing

    def get_total(self):
        return self.price * self.quantity

    total = property(get_total)

    def add_one(self, event):
        self.quantity += 1
        self.price_field.value = str(self.quantity)
        self.on_change(event)
        self.update()

    def remove_one(self, event):
        self.quantity -= 1
        self.quantity = max(self.quantity, 0)
        self.price_field.value = str(self.quantity)
        self.on_change(event)
        self.update()

    def build(self):
        more = IconButton(icon=icons.ADD, on_click=self.add_one)
        less = IconButton(icon=icons.REMOVE, on_click=self.remove_one)
        self.price_field = TextField(value=str(self.quantity), read_only=True)

        return Row(
            [
                Text(self.emoji, size=50),
                Text(f"{self.price:.2f} €"),
                Container(width=100, content=self.price_field),
                more,
                less,
            ],
            alignment=MainAxisAlignment.CENTER,
        )
