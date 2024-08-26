#!/bin/bash

echo "Ejecutando pruebas..."

# Verificar si pytest está instalado
if ! command -v pytest &> /dev/null
then
    echo "pytest no encontrado. Por favor, instálalo y vuelve a intentarlo."
    exit 1
fi

# Ejecutar las pruebas
pytest tests/

echo "Pruebas completadas."
