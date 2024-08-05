import dash
from dash import dcc, html
from callbacks import update_graph

app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f9f9f9",
        "color": "#333",
        "fontFamily": "Arial, sans-serif",
        "padding": "20px",
    },
    children=[
        html.H1(
            "GitHub Repositories by Language",
            style={"textAlign": "center", "color": "#333", "paddingBottom": "20px"},
        ),
        dcc.Dropdown(
            id="language-dropdown",
            options=[
                {"label": lang.capitalize(), "value": lang}
                for lang in [
                    "python",
                    "javascript",
                    "java",
                    "ruby",
                    "php",
                    "csharp",
                    "typescript",
                ]
            ],
            value="python",
            style={
                "width": "50%",
                "margin": "auto",
                "fontSize": "16px",
                "color": "#333",
                "backgroundColor": "#fff",
            },
        ),
        dcc.Graph(id="repo-graph"),
        html.Div(
            id="repo-info",
            style={
                "marginTop": "40px",
                "padding": "20px",
                "border": "1px solid #ddd",
                "borderRadius": "5px",
                "backgroundColor": "#fff",
                "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",
                "width": "80%",
                "margin": "0 auto",
                "color": "#333",
            },
        ),
    ],
)

app.callback(
    [
        dash.Output("repo-graph", "figure"),
        dash.Output("repo-info", "children")
    ],
    [
        dash.Input("language-dropdown", "value"),
        dash.Input("repo-graph", "clickData")
    ],
)(update_graph)

if __name__ == "__main__":
    app.run_server(debug=True)
