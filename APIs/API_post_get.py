import requests

# Base URL for the public blog database
url = "https://jsonplaceholder.typicode.com/posts"

#Creating a new blog post using POST
new_post = {
    "title": "Python Network Requests",
    "body": "Executing post and get methods is fun!",
    "userId": 42
}

post_response = requests.post(url, json=new_post)

if post_response.status_code == 201:
    print("Post successfully created on the remote database.")
    print("Server response payload:", post_response.json())
else:
    print(f"Post failed with status code: {post_response.status_code}")


#Retrieving an existing blog post using GET
#Appending /1 to the URL targets the first record in the database
get_response = requests.get(f"{url}/1")

if get_response.status_code == 200:
    fetched_data = get_response.json()
    print("Data successfully retrieved from the server.")
    print(f"Title: {fetched_data['title']}")
    print(f"Body:  {fetched_data['body']}")
else:
    print(f"Get request failed with status code: {get_response.status_code}")