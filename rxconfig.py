import reflex as rx

config = rx.Config(
    app_name="quote_app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
