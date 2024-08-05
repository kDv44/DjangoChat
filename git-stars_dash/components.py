import plotly.graph_objs as go
from dash import html


def prepare_figure(language, repos):
    repo_links = [
        f"<a href='{repo['html_url']}' target='_blank'>{repo['name']}</a>"
        for repo in repos
    ]
    stars = [repo["stargazers_count"] for repo in repos]

    return {
        "data": [
            go.Bar(
                x=repo_links,
                y=stars,
                marker=dict(
                    color="rgba(255, 127, 14, 0.8)",
                    line=dict(width=1.5, color="rgba(0, 0, 0, 0.2)"),
                ),
                opacity=0.9,
            )
        ],
        "layout": go.Layout(
            title=f"Most-Starred {language.capitalize()} Projects on GitHub",
            titlefont=dict(size=24, color="#333"),
            xaxis=dict(
                title="Repository",
                titlefont=dict(size=18, color="#333"),
                tickfont=dict(size=12, color="#333"),
                tickangle=-45,
            ),
            yaxis=dict(
                title="Stars",
                titlefont=dict(size=18, color="#333"),
                tickfont=dict(size=12, color="#333"),
            ),
            paper_bgcolor="#f9f9f9",
            plot_bgcolor="#fff",
            margin=dict(l=50, r=50, t=50, b=150),
            autosize=True,
            template="plotly_white",
        ),
    }


def prepare_repo_info(repo):
    return html.Div(
        [
            html.H3(
                "Most-Starred Repository:",
                style={"marginBottom": "10px", "color": "#333"},
            ),
            html.Div(
                [
                    html.P(
                        children=[
                            "Name: ",
                            html.A(
                                repo["name"],
                                href=repo["html_url"],
                                target="_blank",
                                style={"color": "#007bff"},
                            ),
                        ],
                        style={"fontSize": "18px", "marginBottom": "5px"},
                    ),
                    html.P(
                        f"Owner: {repo['owner']['login']}",
                        style={"fontSize": "18px", "marginBottom": "5px"},
                    ),
                    html.P(
                        f"Description: {repo.get('description', 'No description')}",
                        style={"fontSize": "18px", "marginBottom": "5px"},
                    ),
                    html.P(
                        f"Stars: {repo['stargazers_count']}",
                        style={"fontSize": "18px", "marginBottom": "5px"},
                    ),
                    html.P(
                        children=[
                            "Link: ",
                            html.A(
                                repo["html_url"],
                                href=repo["html_url"],
                                target="_blank",
                                style={"color": "#007bff"},
                            ),
                        ],
                        style={"fontSize": "18px", "marginBottom": "0px"},
                    ),
                ],
                style={"textAlign": "left"},
            ),
        ]
    )
