# Importamos librerías o módulos que contienen lo que necesitamos
# para no hacer todo de manera manual.
import random
import string


def generar_contrasena(longitud):
    """
    Genera una contraseña segura de entre 8 y 16 caracteres.
    La contraseña tendrá al menos una mayúscula, una minúscula,
    un número y un símbolo.
    """

    if longitud < 8 or longitud > 16:
        return False
    
    # Creamos una lista vacía donde se almacenarán los caracteres
    # de la contraseña.
    
    contrasena = []
    
    # Forzamos que tenga al menos una mayúscula, una minúscula,
    # un número y un símbolo.
    
    contrasena.append(random.choice(string.ascii_uppercase))
    contrasena.append(random.choice(string.ascii_lowercase))
    contrasena.append(random.choice(string.digits))
    contrasena.append(random.choice(string.punctuation))

    caracteres = string.ascii_letters + string.digits + string.punctuation

    for _ in range(longitud - 4):
        contrasena.append(random.choice(caracteres))

    random.shuffle(contrasena)

    return "".join(contrasena)

def validar_contrasena(contrasena):
    
    if len(contrasena) < 8 or len(contrasena) > 16:
        return False
    
    tiene_mayuscula = False
    tiene_minusula = False
    tiene_numero = False
    tiene_simbolo = False
    
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        
        if caracter.islower():
            tiene_minusula = True
            
        if caracter.isdigit():
            tiene_numero = True
            
        if caracter.isalnum():
            tiene_simbolo = True
            
    if not tiene_mayuscula:
        return False
    
    if not tiene_mayuscula:
        return False
    
    if not tiene_mayuscula:
        return False
    
    if not tiene_mayuscula:
        return False
    
    return True


while True:
    
    print("\nMENU")
    print("Generador de contrasenas seguras")
    print("1 - Generar contrasena")
    print("2 - Validar contrasena")
    print("3 - Salir")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        cantidad = int(input("¿Cuantas contrasenas deseas generar?: "))
        longitud = int(input("¿Que longitud tendra cada contrasena? (8 a 16 caracteres): "))

        for i in range(cantidad):
            nueva = generar_contrasena(longitud)
            print(f"Contrasena {i + 1}: {nueva}")
    
    elif opcion == "2":
        contrasena_usuario = input("Ingrese la contrasena que desea validar: ")
        
        if validar_contrasena(contrasena_usuario):
            print("La contrasena es segura")
        else:
            print("La contrasena no es segura.")
    
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opcion invaida. Intente nuevamente.")