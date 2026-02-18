import requests


get_url = "https://jsonplaceholder.typicode.com/posts/1"
post_url = "https://jsonplaceholder.typicode.com/posts"

payloads={
    "Name" : "Sanchita",
    "Gender" : "Female",
    "Occupation" : "Student",
}

try:
    r = requests.get(get_url,timeout=5)
    print(f" Get Req Status Code:{r.raise_for_status}")

    p = requests.post(post_url,json=payloads,timeout=5)
    print(f"Post Req Status Code:{p.raise_for_status}")

    print("GET JSON:", r.json())
    print("POST JSON:", p.json())

except requests.exceptions.Timeout:
    print("Request took too long to load")

except requests.exceptions.RequestException:
    print("ERROR due to status code")







