import requests


def fetch_repository_data(language):
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars"
    headers = {"Accept": "application/vnd.github.v3+json"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json().get("items", [])
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
