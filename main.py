from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

# this a normal get using fastapi

# @app.get("/")
# async def root():
#     return {"message" : "Hello world!"}

#-------------------------------------------------

# this is a get using "parameters" o "variables" in the path

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"itemId" : item_id}

#--------------------------------------------------

#this is now a example using types in the parameters on the path

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"itemId" : item_id}


#--------------------------------------------------

# you cannot redefine a path operation, always be used the first one since the path matches first

# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morty"]


# @app.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]

#----------------------------------------------------

# Using predefined values with enums class

# class ModelName(str, Enum):
#     rick = "Rick"
#     morty = "Morty"
#     archer = "Archer"

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.rick:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
#     # Se puede acceder al nombre del enum usando operador == o usando 'is'

#     # if model_name is ModelName.morty:

#     if model_name.value == "Morty":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

#------------------------------------------------------------------------------


# using a path like a path parameter

# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}

#-------------------------------------------------------------------------------

# Using a path like a parameter and read de content in the file of the path 

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    # Define la base del directorio donde se buscarán los archivos
    base_path = "files"
    
    # Obtiene el directorio de trabajo actual del servidor
    current_directory = os.getcwd()

    # Reemplaza las barras invertidas por barras normales en la ruta (útil para sistemas Windows)
    modified_directory = current_directory.replace('\\', '/')
    
    # Combina el base_path con file_path y elimina una barra inicial si está presente
    # Esto asegura que file_path se trate como ruta relativa
    _path = os.path.join(base_path, file_path).lstrip('/')

    # Combina el directorio modificado con _path para obtener la ruta completa del archivo
    full_path = os.path.join(modified_directory, _path)

    # Verifica si el archivo existe en la ruta completa
    if not os.path.exists(full_path):
        # Si el archivo no existe, devuelve un error 404
        raise HTTPException(status_code=404, detail="File not found")

    # Intenta abrir y leer el archivo
    try:
        with open(full_path, "r") as file:
            # Devuelve el contenido del archivo en la respuesta
            return {"file_content": file.read()}
    except Exception as e:
        # Si hay algún error al leer el archivo, devuelve un error 500
        raise HTTPException(status_code=500, detail=str(e))
