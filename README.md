# CHR test practico


## Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.


### Pre-requisitos 📋

Para empezar tenemos que tener un entorno virtual de Python instalado. Si no tienes uno puedes instalar virtualenv abrienda la consola y ejecutando los siguientes codigos:

```shell
pip install virtualenv
```
Luego tienes que crear una carpeta del entorno, en este caso lo llamaremos venv.

```
virtualenv venv
```
Para activar el entorno tienes que ejecutar el siguiente comando en el directorio actual si estas en windows:

```
.\venv\Scripts\activate
```
tambien es necesario que instales las siguientes versiones:

**Python 3.10.9**

Por ultimo tienes que tener **PostgreSQL** instalado y tienes que tener en el PATH el chromedriver.
### Creando la base de datos
Tienes que crear una base de datos en PostgreSQL con las siguientes caracteristicas:

Nombre de la base de datos: **taskdb**
usuario: **postgres**
password: **admin**
puerto: **5432**

### Instalación 🔧
Versiones a utilizar:
**Django 4.2.2**
**requests 2.31.0**
**psycopg2 2.9.6**
**selenium 4.10.0**

Primero tenemos que instalar Django:
```
pip install django==4.2.2
```
Luego instalamos **requests** , **psycopg2** y **selenium 4.10.0** :
```
pip install requests==2.31.0
pip install psycopg2==2.9.6
pip install selenium==4.10.0
```
Despues tenemos que hacer las migraciones para crear la tabla en la BDD :
```
python manage.py makemigrations
python manage.py migrate
```

## Despliegue 📦

Para iniciar la aplicación tienes que iniciar Django:
```
python manage.py runserver
```
### Tarea 1

La principal función del de esta app es que puedes guardar una jurisprudencia en la base de datos al ingresar el nombre en el buscador. Luego, se muestran por pantalla todas las jurisprudencia de la base de datos local.

### Tarea 2

Las pruebas hechas con selenium se utilizan para probar los filtros de la página solicitada obteniendo los resultados entregados por este.

Para iniciar las pruebas se tiene que ejecutar el siguiente código en consola:
```
python manage.py test
```
