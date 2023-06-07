import requests

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

def display_weather(weather_data):
    # Extract necessary information from the weather data
    city = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]

    # Display the weather information
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")

# Main program
def main():
    api_key = "86b9514f188e888b256c05721c5d59d8"
    city = input("Enter the city name: ")
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
