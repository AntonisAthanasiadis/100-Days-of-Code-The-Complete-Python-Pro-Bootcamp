import requests

url_target = "https://jsonplaceholder.typicode.com/posts/1"

# The new data structure that will completely overwrite the original post #1
updated_payload = {
    "id": 1,
    "title": "An Updated Title",
    "body": "This text completely replaces whatever body text was here before.",
    "userId": 12
}

# Send the PUT request
put_response = requests.put(url_target, json=updated_payload)

if put_response.status_code == 200:
    print("Update successful.")
    print("New server data:", put_response.json())
else:
    print(f"PUT request failed with status: {put_response.status_code}")

# Send the DELETE request
# Note: We do not pass a 'json=' argument here because we are just destroying the target URL
delete_response = requests.delete(url_target)

if delete_response.status_code == 200:
    print("Deletion successful.")
    print("Server confirmation payload (empty):", delete_response.json())
else:
    print(f"DELETE request failed with status: {delete_response.status_code}")