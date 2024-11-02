from werkzeug.security import generate_password_hash, check_password_hash

# generate_password_hash # Genera un valor cifrado
# check_password_hash # Verifica un valor cifrado

# texto_encriptado_1 = generate_password_hash("texto a encriptar", method="método de encriptacion (opcional)", salt_length=16 ("opcional, debe ser un número entero"))
# El "salt" es un valor aleatorio que se añade a la contraseña antes de aplicar la función hash para asegurar que incluso contraseñas idénticas no produzcan el mismo hash. Esto ayuda a proteger contra ataques de diccionario y ataques de fuerza bruta.

texto = "x?1_P-1M.4!eM"
texto_encriptado_1 = generate_password_hash(texto)
# texto_encriptado_2 = generate_password_hash(texto, 'sha256')
# texto_encriptado_3 = generate_password_hash(texto, 'sha256', 30)
texto_encriptado_4 = generate_password_hash(texto, 'pbkdf2:sha256')
texto_encriptado_5 = generate_password_hash(texto, 'pbkdf2:sha256', 30)
texto_encriptado_6 = generate_password_hash(texto, 'pbkdf2:sha256:30', 30)

print(texto_encriptado_1)
# print(texto_encriptado_2)
# print(texto_encriptado_3)
print(texto_encriptado_4)
print(texto_encriptado_5)
print(texto_encriptado_6)

# check_password_hash # compara la contraseña ingresada con la que se guardó en la base de datos
print(check_password_hash(texto_encriptado_1, texto)) # True
print(check_password_hash(texto_encriptado_4, texto))
print(check_password_hash(texto_encriptado_5, texto))
print(check_password_hash(texto_encriptado_6, texto))