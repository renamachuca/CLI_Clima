import requests
import argparse

API_KEY = '1adac4da3358b065670693ef3171d951'  # Reemplaza con tu clave de API de OpenWeatherMap

def obtener_clima(ciudad, pais, formato_salida):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={API_KEY}&units=metric'
    
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        temp = datos['main']['temp']
        descripcion_clima = datos['weather'][0]['description']
        
        if formato_salida == 'json':
            print({'city': datos['name'], 'country': datos['sys']['country'], 'temperature': temp, 'weather': descripcion_clima})
        elif formato_salida == 'csv':
            print(f"{datos['name']},{datos['sys']['country']},{temp},{descripcion_clima}")
        else:
            print(f"Ciudad: {datos['name']}, {datos['sys']['country']}")
            print(f"Temperatura: {temp}°C")
            print(f"Clima: {descripcion_clima}")
    else:
        print(f"Error: No se pudo obtener información del clima para {ciudad}, {pais}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obtén la información actual del clima para una ciudad.")
    parser.add_argument('ubicaciones', type=str, nargs='+', help="Ciudades y países (ej., 'Asuncion,PY' 'Buenos Aires,AR')")
    parser.add_argument('--format', type=str, default='text', choices=['text', 'json', 'csv'], help="Formato de salida: text, json, csv")
    
    args = parser.parse_args()
    
    for ubicacion in args.ubicaciones:
        ciudad, pais = ubicacion.split(',')
        print(f"\nInformación del clima para {ciudad.strip()}, {pais.strip()}:")
        obtener_clima(ciudad.strip(), pais.strip(), args.format)
