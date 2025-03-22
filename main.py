from dash import Dash, html, dcc, Input, Output
from layout import layout
from callbacks import register_callbacks

app = Dash(__name__, suppress_callback_exceptions=True)

with open("assets/index.html", encoding="utf-8") as f:
    app.index_string = f.read()

app.layout = layout

register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
