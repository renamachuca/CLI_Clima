#!/bin/bash

# Instalación de dependencias
echo "Instalando dependencias..."

# Verificar si pip está instalado
if ! command -v pip3 &> /dev/null
then
    echo "pip3 no encontrado. Por favor, instálalo y vuelve a intentarlo."
    exit 1
fi

# Instalar dependencias desde requirements.txt
if [ -f requirements.txt ]; then
    pip3 install -r requirements.txt
else
    echo "requirements.txt no encontrado. Crea este archivo para especificar las dependencias."
fi

echo "Dependencias instaladas."
