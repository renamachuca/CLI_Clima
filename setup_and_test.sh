#!/bin/bash

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Ejecutar pruebas
echo "Ejecutando pruebas..."
pytest

# Mensaje de éxito
echo "Instalación y pruebas completadas con éxito."
