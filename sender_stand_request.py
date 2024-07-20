import requests
import configuration
import data


# Creacion de un nuevo usuario
def post_new_client(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

# Creacion de un nuevo kit
def post_new_client_kit(kit_user_body):
   token =  authtoken_new_kit()
   headers = {
       "Content-Type": "application/json",
       "Authorization": f"Bearer {token}"
   }
   return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                       json=kit_user_body,
                       headers=headers)

# Incluir el Authtoken
def authtoken_new_kit():
    response = post_new_client(data.user_body)
    return response.json()["authToken"]


# Función de prueba positiva
def positive_assert(kit_body):
    response = post_new_client_kit(kit_body)

    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    return response.json()

# Función de prueba negativa
def negative_assert_code_400(kit_body):
    response = post_new_client_kit(kit_body)

    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    return response.json()

def get_kit_body(name):
    return {"name": name}