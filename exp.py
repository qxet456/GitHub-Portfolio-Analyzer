import requests


def get_info():
    while True:
        username = input("Type username: ")
        url = f"https://api.github.com/users/{username}"
        repo_url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)
        response2 = requests.get(repo_url)
        if response.status_code == 200 and response2.status_code == 200:
            print("----------------------------")
            print("Valid User")
            data = response.json()
            data2 = response2.json()
            print("----------------------------")
            print("Github Profile")
            print("----------------------------")
            print(f"Username: {data['login']}")
            print(f"Name: {data['name']}")
            print(f"Bio: {data['bio']}")
            print(f"Followers: {data['followers']}")
            print(f"Following: {data['following']}")
            print(f"Public Repositories: {data['public_repos']}")
            print(f"Created on: {data['created_at']}")
            print(f"Url: {data['html_url']}")
            print("----------------------------")
            print("Repositories")
            print("---------------------------")
            print(type(data))
            print(type(data2))
        else:
            print("Invalid User")


get_info()
