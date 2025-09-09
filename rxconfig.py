import reflex as rx

config = rx.Config(
    app_name="reflex_react_js_in_python_write_python_read_react",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)