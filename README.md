# Projecto-de-Carly---sprint-7
# Introducción a la automatización de pruebas

## Descripción del proyecto
El proyecto tiene la intención de introducirnos en los principios básicos de la programación de pruebas automatizadas.

## Instalación
Para instalar y configurar el proyecto, sigue estos pasos:

1. Instala Python 3.12 desde [python.org](https://www.python.org/downloads/release/python-3120/).
2. Instala los recursos necesarios:
    ```bash
    pip install pytest - requests
    ```
Ejecuta las pruebas con el siguiente comando en la terminal:
pytest create_kit_name_kit_test.py

## Uso
El proyecto incluye varias funciones y pruebas. Aquí hay un resumen de las funciones principales:

- `post_new_client`: Función para crear un nuevo cliente.
- `post_new_client_kit`: Función para crear un nuevo kit de cliente.
- `authtoken_new_kit`: Función para autenticar un nuevo kit.
- `positive_assert`: Función para realizar aserciones positivas.
- `negative_assert_code_400`: Función para realizar aserciones negativas con código de error 400.
- `get_kit_body`: Función que cambia el contenido del cuerpo de la solicitud.

## Contribución
Actualmente, hay cuatro errores conocidos en el proyecto:

1. `test_create_kit_cero_letter_in_name_get_success_response`
2. `test_create_kit_512_letter_in_name_get_success_response`
3. `test_create_kit_caracter_x_in_name_get_success_response`
4. `test_create_kit_caracter_strangernumber_in_name_get_success_response`

Para contribuir, por favor revisa la documentación fuente en [apiDoc].

## Licencia
Este proyecto está bajo la licencia TripleTen.

## Autores
- Carly Brito

