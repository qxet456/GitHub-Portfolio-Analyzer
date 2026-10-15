import requests


def get_info():
    while True:
        print("-" * 20)
        print("OPTIONS")
        print("-" * 20)
        print("A. CONTINUE")
        print("B. EXIT")
        print("-" * 20)
        ask_choice = input("Type your choice: ")
        if ask_choice == "A" or ask_choice == "a":
            print("-" * 20)
            username = input("Type username: ")
            url = f"https://api.github.com/users/{username}"
            repo_url = f"https://api.github.com/users/{username}/repos"
            response = requests.get(url)
            response2 = requests.get(repo_url)
            if response.status_code == 200 and response2.status_code == 200:
                print("-" * 20)
                print("Valid User")
                data = response.json()
                data2 = response2.json()
                print("-" * 20)
                print("Github Profile")
                print("-" * 20)
                print(f"Username: {data['login']}")
                print(f"Name: {data['name']}")
                print(f"Bio: {data['bio']}")
                print(f"Followers: {data['followers']}")
                print(f"Following: {data['following']}")
                print(f"Public Repositories: {data['public_repos']}")
                print(f"Created on: {data['created_at']}")
                print(f"Url: {data['html_url']}")
                print("-" * 20)
                print("Repositories")
                print("-" * 20)
                for i in data2:
                    print(f"Name: {data2[0]['name']}")
                    print(type(i))
                    i += 1  
            else:
                print("Invalid User")
        elif ask_choice == "B" or ask_choice == "b":
            break
        else:
            print(ask_choice, "is not an OPTION")
get_info()