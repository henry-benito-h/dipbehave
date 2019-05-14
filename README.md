# DipBehave

_DipBehave es un proyecto de automatizacion para pruebas de aceptacion_sobre el REST API de una aplicacion._
_Aplica el tipo de framework BDD(Behavior Driven Development) en el lenguaje python._

## Comenzando 🚀

_Estas instrucciones permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

El codigo actual esta implementado en un repositorio en github. Para poder clonar el proyecto se debe ejecutar el siguiente comando:

```git clone https://github.com/henry-benito-h/dipbehave.git```

EL codigo estable se encuentra en el branch 'develop'. Ejecutar el siguiente commando para moverse al branch mencionado.

```git branch develop```


### Pre-requisitos 📋

_Las siguientes requerimientos son necesarios para la ejecucion del proyecto._

- **Python 3.7.2**
Es posible obtener el instalador de python en su [pagina oficial](https://www.python.org/downloads/) de acuerdo a la plataforma sobre la que se esta trabajando.

- Pip
EL gestor de paquetes de python, desde python 3 el gestor ya viene instalado por defecto, sin embargo puede ejecutar el 
siguiente comando para instalarlo:

    ```
    python -m pip install -U pip setuptools
    ```
- La siguiente lista de paquetes tambien se encuentran disponibles en el archivo 'requirements.txt'

  - behave>=1.2.6
  - compare>=0.2b0
  - coverage>=4.5.3
  - oauthlib>=3.0.1
  - pytest>=4.4.1
  - pytest-cov>=2.7.1
  - pytest-html>=1.20.0
  - requests>=2.21.0
  - requests-oauthlib>=1.2.0

  para la instalacion de requerimientos se ejecuta el siguiente comando:
    ```
    pip install -r requirements.txt
    ```

Mas alla de estas herramientas, es necesario cambiar los datos de configuracion en el archivo "config.yaml" de acuerdo a
 la aplicacion que seleccione para ejecutar las pruebas.

    root:
      host: https://www.pivotaltracker.com
      root_path: /services/v5/
      authorization_type: bearer
      default_role: admin
      headers:
        accept: application/json
        Content-Type: application/json
      roles:
        admin:
          username: <username>
          password: <password>
          headers:
            X-TrackerToken: <token>


### Instalación 🔧

_El siguiente es un ejemplo de como abrir el proyecto en el IDE Pycharm en la version Porfesional(Esto debido a que el 
plugin para trabajar con Gherkin ya viene instalado en esta version)._

 1. Abrir el IDE Pycharm
 2. Seleccionar la opcion "Abrir proyecto"
 3. Seleccionar la carpeta del proyecto "dipbehave"
 4. Esperar la carga de modulos y paquetes
 5. Abrir la carpeta "features"
 6. Abrir el menu contextual sobre algun archivo con extension "feature"
 7. Seleccione la opcion "Run '...feature''"


_Mediante linea terminal, el siguiente comando permite ejecutar los escenarios mediante behave._

```
hasta finalizar
```

para la ejecuacion de un escenario que usa tags se puede anadir el parametro "--tag" de la siguiente manera:
```
angular2
```


## Ejecutando las pruebas ⚙

La ejecucion de pruebas unitarias se la realiza con el siguiente commando:

```
pytest test_authorization.py --html=report.html --cov=../utils .
```

Finalmente para la poder ejecutar los escenarios con 'coverage' el siguiente comando sera ejecutado:

```
coverage run --source='.' --omit 'unittests/*' --branch -m behave
```

para generar el reporte se ejecuta:

```
coverage report -m
```


### Analice las pruebas end-to-end 🔩

_Las pruebas de conexion son necesarias para evitar resultados de ejecucion, como los falsos posistivos. Mediante el
 siguiente escenario de ejemplo podemos probar la disponibilidad del servicio para un endpoint en especifico._

```gherkin
@Smoke
Feature: API Availability
  As an admin
  I want to get a response from api service.
  So I should get 200 OK response


  Scenario: Test service availability for project
    And I have the next endpoint "projects"
    When I do an api GET request
    Then I should have 200 as status code
```

## Construido con 🛠

* [Python](https://www.python.org) - Lenguaje de programacion
* [Behave](https://behave.readthedocs.io) - El framework para automatizacion

## Contribuyendo 🖇

Las contribuciones se realizan con un Merge Request. Todo mejora es gratamente recibida.

## Autores ✒
* **Henry Benito** - *Trabajo Inicial* - (https://github.com/henry-benito-h)


También puedes mirar la lista de todos los [contribuyentes](https://github.com/henry-benito-h/dipbehave/contributors) quíenes han participado en este proyecto. 

## Expresiones de Gratitud 🎁

* Quiero agradecer a mi familia por el incondicional soporte.



---
⌨ con ❤ por [Henry](https://github.com/henry-benito-h) 😊