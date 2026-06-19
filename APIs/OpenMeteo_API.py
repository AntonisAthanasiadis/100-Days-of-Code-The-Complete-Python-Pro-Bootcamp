import requests

ENDPOINT = "https://api.open-meteo.com/v1/forecast"
#If API key is needed, add it to weather_params (for OpenWeatherMap for example)
#Set the parameters for Thessaloniki, Greece
weather_params = {
    "latitude": 40.6436,
    "longitude": 22.9309,
    "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature"],
    "timezone": "auto"
}

try:
    #Make the API request
    response = requests.get(ENDPOINT, params=weather_params)
    response.raise_for_status()  #Raises an error for bad HTTP status codes

    # Parse the JSON response
    data = response.json()

    #Extract and print the current weather data
    current = data["current"]
    units = data["current_units"]

    print(f"Current Weather in Thessaloniki:")
    print(f"Temperature: {current['temperature_2m']}{units['temperature_2m']}")
    print(f"Feels Like:  {current['apparent_temperature']}{units['apparent_temperature']}")
    print(f"Humidity:    {current['relative_humidity_2m']}{units['relative_humidity_2m']}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the weather: {e}")