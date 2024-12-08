##CVE - Create Virtual Environment - for Python

import os
import time
import subprocess
import shutil
from colorama import Fore, Style


def main():
  #mensajes de intro
  print(f"{Fore.GREEN}\nBienvenido al asistente para la creación automática de un entorno virtual para realizar proyectos de Python -by {Fore.BLUE}Paolo Troni\n {Style.RESET_ALL}")
  time.sleep(2)

  print(f"{Fore.RED}¡Atención!: {Fore.YELLOW}De momento, ese asistente esta configurado para funcionar en Linux\n{Style.RESET_ALL}")
  time.sleep(2)

  print("Requerimentos previos para el funcionamento de ese script:")
  system_requirements = ["OS Linux", "Python3", "venv"]

  for requeriment in system_requirements:
    print(f"{Fore.BLUE}- {requeriment}{Style.RESET_ALL}")
    time.sleep(0.8)

  time.sleep(2)
  print(f"Si no tienes los requerimentos, prema {Fore.BLUE}'CRTL + o' para salir y preparar el sistema adecuadamente\n.{Style.RESET_ALL}")
  time.sleep(2)
  print("Presiona 'enter (intro)' para proseguir...")
  input()


  #Creación de la carpeta del proyecto

  home_dir = os.path.expanduser("~") #obtenemos la ruta de la carpeta de usuario

  base_path = home_dir # Se establece la carpeta de usuario como ruta base

  print(f"{Fore.YELLOW}El proyecto se creará en la ruta: {Fore.BLUE}{base_path}\n {Style.RESET_ALL}")

  print("Si estás de acuerdo, digite 'S' para proseguir, o prema 'n' para insertar manualmente la ruta en donde crear el proyecto." )
  print("En caso contrario, prema 'Crtl + c' para abortar.\n")
  user_choice = input()

  while True:
    if user_choice=="S":
      print(f"{Fore.YELLOW}Proseguimos a crear el proyecto en la ruta: {Fore.BLUE}{base_path}\n {Style.RESET_ALL}")
      project_path = create_project_directory(base_path)
      break

    elif user_choice =="n":
      user_path = input(f"Inserte la ruta deseada en la que deseas crear el proyecto:")
      base_path = user_path
      print(f"Vas a crear el proyecto en la ruta: {user_path}")
      project_path = create_project_directory(base_path)
      break
    else:
      print(f"{Fore.YELLOW} ¡No has insertado un valor válido! {Style.RESET_ALL}") 
      print("Si estás de acuerdo, digite 'S' para proseguir, o prema 'n' para insertar manualmente la ruta en donde crear el proyecto." )
      print("En caso contrario, prema 'Crtl + c' para abortar.\n")
      user_choice = input()

  #creamos un entorno virtual
  print(f"Ahora vamos a proceder a crear un entorno virtual en {project_path}\n")
  try:
    create_venv(project_path)

  except Exception as e:
    manage_error(e, project_path)

  finally:
    print("\nHemos finalizado, gracias por usar ese script")

###################################################################

#Funciones del programa

#función que crea la carpeta del proyecto
def create_project_directory(base_path):
  folder_name = input("¿Como se llamará el proyeto? ")
  project_path = os.path.join(base_path, folder_name)

  if not os.path.exists(project_path):   
    os.mkdir(project_path)
    print(f"Proyecto creado en la ruta {project_path}")
  else:
    print(f"{Fore.YELLOW}¡Ya esiste una carpeta con ese nombre en esa ruta!{Style.RESET_ALL}")  
    print("Por favor, inserte un nombre valido para la carpeta para poder continuar.")
    create_project_directory(base_path)
  
  return project_path


#función que crea un entorno virtual en la carpeta del proyecto
def create_venv(path):
  create_venv = "python3 -m venv env"  
  result = subprocess.run(create_venv, shell=True, cwd=path, capture_output=True, text=True, timeout=60)

  # Imprimir el resultado del comando
  if result.returncode == 0:
    print(f"El entorno virtual ha sido creado correctamente en {path}/env")
  
  else:
    raise Exception(f"Error al crear el entorno virtual: {result.stderr}")


# Gestion de errores: expone el mensage de error y borra la carpeta del proyecto
def manage_error(e, path):
  print(f"El proceso falló: {e}")
  print("Intentando eliminar la carpeta del proyecto debido al error...\n")

  try:
    shutil.rmtree(path)
    print(f"La carpeta del proyecto {path} ha sido eliminada.")
  except Exception as cleanup_error:
      
    print(f"Error al intentar borrar la carpeta del proyecto: {cleanup_error}")  



if __name__ == "__main__":
    main()