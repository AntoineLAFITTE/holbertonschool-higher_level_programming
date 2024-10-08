import requests
import csv

# All needed 2 functions : - one for fecthing and printing posts.(if code 200)
#                          - one to fetch and save posts.(if code sucess 200)

def fetch_and_print_posts():
    # Fetch data from the JSONPlaceholder API
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Print the status code of the response
    # status_code will return after calling requests.get("url")
    # status_code is an attribute of the Response object response(instance).
    print(f"Status Code: {response.status_code}")

    # Check if request was successfuly done
    if response.status_code == 200:
        # Parse the response into JSON
        # .json() method from Response class use it bro it converts the body
        # of the response(data returned by the server) into a Python Object
        # (Dictionary or list) if content is in JSON format how wonderfull.
        posts = response.json()

        # Print the titles of all posts (python loops are so sexy btw)
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    # Fetch data from the JSONPlaceholder API
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Check if request was successful
    if response.status_code == 200:
        # Parse the response into JSON
        posts = response.json()

        # Structure the data into a list of dictionaries
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Save the data to a CSV file
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data)
