# Pip & VENV with Python3

## Run:

Send to the shell.

```sh
cd game 
python3 main 
```


# Create project with venv


## Crear un entorno
python3 -m venv env

##Activar un entorno virtual
source env/bin/activate

##Verificar que estemos dentro del entorno virtual
which python3

##Instalar la dependencia dentro del entorno virtual
pip3 install requests

##Verificar la instalacion
pip3 freeze

##Crear el archivo para que cualquier persona pueda desplegar el proyecto
pip freeze > requeriments.txt
