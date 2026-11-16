import requests
url = "https://jsonplaceholder.typicode.com/posts/999999"
try:
    response = requests.get(url)
    response.raise_for_status()
    post_data = response.json()
    print(post_data["title"])
except requests.exceptions.RequestException as error:
    print(error)
