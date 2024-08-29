import requests

import argparse

API_KEY = '1adac4da3358b065670693ef3171d951'  # Asegúrate de reemplazar esto con tu clave de API de OpenWeatherMap

def get_weather(city, country, output_format):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}&units=metric'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if output_format == 'json':
            print(data)
        elif output_format == 'csv':
            print(f"{data['name']},{data['sys']['country']},{data['main']['temp']},{data['weather'][0]['description']}")
        else:
            print(f"City: {data['name']}, {data['sys']['country']}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Weather: {data['weather'][0]['description']}")
    else:
        print(f"Error: Could not retrieve weather data for {city}, {country}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the current weather information for a city.")
    parser.add_argument('location', type=str, help="City and country (e.g., 'Asuncion,PY')")
    parser.add_argument('--format', type=str, default='text', choices=['text', 'json', 'csv'], help="Output format: text, json, csv")
    
    args = parser.parse_args()
    city, country = args.location.split(',')

    get_weather(city.strip(), country.strip(), args.format)
