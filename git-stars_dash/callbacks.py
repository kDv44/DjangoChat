import plotly.graph_objs as go
from utils import fetch_repository_data
from components import prepare_figure, prepare_repo_info


def update_graph(language, click_data):
    repos = fetch_repository_data(language)
    if not repos:
        return go.Figure(), "No repositories found for this language."

    figure = prepare_figure(language, repos)
    selected_repo = (
        repos[click_data["points"][0]["pointIndex"]] if click_data else repos[0]
    )
    repo_info = prepare_repo_info(selected_repo)

    return figure, repo_info
