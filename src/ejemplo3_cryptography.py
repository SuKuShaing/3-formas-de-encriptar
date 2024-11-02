from cryptography.fernet import Fernet

texto = "x?1_P-1M.4!eM"

key = Fernet.generate_key() # Genera una clave en formato de secuencia de bytes:
object_cifrado = Fernet(key) # Objeto cifrado
texto_encriptado = object_cifrado.encrypt(str.encode(texto)) # Encriptamos mediante la llave
print("texto_encriptado", texto_encriptado)

texto_desencriptado_bytes = object_cifrado.decrypt(texto_encriptado)
print("texto_desencriptado_bytes", texto_desencriptado_bytes)
texto_desencriptado = texto_desencriptado_bytes.decode()
print("texto_desencriptado", texto_desencriptado)
print(type(texto_desencriptado))