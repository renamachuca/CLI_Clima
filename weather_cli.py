import requests
import argparse
import json
import os
import pickle


API_KEY = '1adac4da3358b065670693ef3171d951'  

ARCHIVO_CACHE = 'weather_cache.pkl'

TRADUCCION_CLIMA = {
    'clear sky': 'cielo despejado',
    'few clouds': 'pocas nubes',
    'scattered clouds': 'nubes dispersas',
    'broken clouds': 'nubes rotas',
    'shower rain': 'lluvia ligera',
    'rain': 'lluvia',
    'thunderstorm': 'tormenta eléctrica',
    'snow': 'nieve',
    'mist': 'niebla',
    'overcast clouds': 'nubes cubiertas'
}

def cargar_cache():
    
    if os.path.exists(ARCHIVO_CACHE):
        with open(ARCHIVO_CACHE, 'rb') as archivo_cache:
            return pickle.load(archivo_cache)
    return {}

def guardar_cache(cache):
    
    with open(ARCHIVO_CACHE, 'wb') as archivo_cache:
        pickle.dump(cache, archivo_cache)

def traducir_clima(descripcion_ingles):
    return TRADUCCION_CLIMA.get(descripcion_ingles, descripcion_ingles)

def obtener_clima(ciudad, pais, formato_salida, cache):
    clave_cache = f'{ciudad},{pais}'
    
    if clave_cache in cache:
        datos = cache[clave_cache]
        print(f"Usando caché para {ciudad}, {pais}")
    else:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={API_KEY}&units=metric'
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            cache[clave_cache] = datos
            guardar_cache(cache)
        else:
            print(f"Error: No se pudo recuperar los datos del clima para {ciudad}, {pais}")
            return
        
    temp = datos['main']['temp']
    descripcion_clima = traducir_clima(datos['weather'][0]['description'])
    
    if formato_salida == 'json':
        print(json.dumps({'ciudad': datos['name'], 'pais': datos['sys']['country'], 'temperatura': temp, 'clima': descripcion_clima}, indent=4, ensure_ascii=False))
    elif formato_salida == 'csv':
        print(f"{datos['name']},{datos['sys']['country']},{temp},{descripcion_clima}")
    else:
        print(f"Ciudad: {datos['name']}, {datos['sys']['country']}")
        print(f"Temperatura: {temp}°C")
        print(f"Clima: {descripcion_clima}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consulta la información actual del clima para una ciudad.")
    parser.add_argument('ubicaciones', type=str, nargs='+', help="Ciudades y países (e.g., 'Asuncion,PY' 'Buenos Aires,AR')")
    parser.add_argument('--formato', type=str, default='text', choices=['text', 'json', 'csv'], help="Formato de salida: text, json, csv")
    
    args = parser.parse_args()
    
    cache = cargar_cache()
    
    for ubicacion in args.ubicaciones:
        try:
            ciudad, pais = ubicacion.split(',')
            print(f"\nInformación del clima para {ciudad.strip()}, {pais.strip()}:")
            obtener_clima(ciudad.strip(), pais.strip(), args.formato, cache)
        except ValueError:
            print(f"Error: La ubicación '{ubicacion}' no está en el formato correcto. Usa 'ciudad,pais'.")
