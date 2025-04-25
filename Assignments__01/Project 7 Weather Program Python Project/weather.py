import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # temperature Celsius mein chahiye
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] != 200:
        print("City not found! Please check the name.")
        return

    # Weather info extract karte hain
    temp = data["main"]["temp"]
    weather_desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Description: {weather_desc}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "YOUR_API_KEY_HERE"  # Yahan apni API key daalo
    get_weather(city_name, api_key)
