import requests

url = "http://api.open-notify.org/iss-now.json"

try:
    response = requests.get(url)
    data = response.json()
    print(data)

    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]

    print(f"\nThe ISS is currently at:")
    print(f"Latitude:  {latitude}")
    print(f"Longitude: {longitude}")

except Exception as e:
    print(f"Could not connect: {e}")