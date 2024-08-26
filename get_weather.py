import requests

def get_weather(location):
    api_key = "1adac4da3358b065670693ef3171d951"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

weather_data = get_weather("Buenos Aires, AR")
if weather_data:
    print(f"Temperatura: {weather_data['main']['temp']}")
else:
    print("Ubicación no encontrada o error en la solicitud.")
