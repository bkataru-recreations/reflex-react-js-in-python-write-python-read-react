# first install requests by 'pip install requests'
import requests
# we give reflex an alias of rx
import reflex as rx
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
        self.quote = data[random_number]['text']
        self.author = data[random_number]['author']

def home():
    return rx.center(
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
app.add_page(home, title="Random Quote Generator")
app.compile()
