# first install requests by 'pip install requests'
import requests
# we give reflex an alias of rx
import reflex as rx
from rxconfig import config
# in order to get some random quotes
import random

class QuoteState(rx.State):
    """The app state."""

    quote: str = ""
    author: str = ""

    def get_quote(self):
        """Get a random quote."""
        response = requests.get("https://api.quotable.kurokeita.dev/api/quotes")
        data = response.json()["data"]
        random_number: int = random.randint(0, 10)
        elem = data[random_number]
        
        self.quote = elem['content']
        self.author = elem['author']['name']

def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Random Quote Generator"),
            rx.button("Get Quote", on_click=QuoteState.get_quote),
            rx.text(QuoteState.quote),
            rx.text(QuoteState.author),
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
    )

app = rx.App()
app.add_page(index, title="Random Quote Generator")
