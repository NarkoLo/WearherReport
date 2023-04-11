import requests

# API endpoint
url = "https://api.openweathermap.org/data/2.5/weather"

# API key
api_key = "c718d6aa5bf8fc10eb4e37078e7929dc"

# City name
city_name = input("Enter city name: ")

# API request parameters
params = {"q": city_name, "appid": api_key, "units": "metric"}

# Send API request
response = requests.get(url, params=params)

# Check API response status code
if response.status_code == 200:
    # Parse API response
    data = response.json()

    # Print weather information
    print("City name: ", data["name"])
    print("Temperature: ", data["main"]["temp"], "°C")
    print("Humidity: ", data["main"]["humidity"], "%")
    print("Weather: ", data["weather"][0]["description"])
else:
    # Print error message
    print("Error: Could not retrieve weather information.")
