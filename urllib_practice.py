import urllib.request
import json
url = "https://jsonplaceholder.typicode.com/posts/1"
try:
    with urllib.request.urlopen(url) as response:
        response_body = response.read()
        response_text = response_body.decode("utf-8")
        post_data = json.loads(response_text)
        print(post_data)
except Exception as error:
    print(error)
