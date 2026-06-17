import requests

url = "https://api.sunrise-sunset.org/json"
params = {
    #Hardcoded coordinates for Thessaloniki
    "lat": 40.6436,
    "lng": 22.9309,
    "formatted": 0
}

try:
    response = requests.get(url, params=params)
    data = response.json()
    print(f"Raw JSON: {data}")

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    print("Today's Times for Thessaloniki:")
    print(f"Sunrise: {sunrise}")
    print(f"Sunset:  {sunset}")

except Exception as e:
    print(f"Error fetching data: {e}")