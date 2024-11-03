# Encriptación de Contraseñas en Python 🔐 | 3 Formas de Cifrar y Desencriptar Textos y Passwords ✅

Tutorial de UskoKruM2010
https://youtu.be/mgDIP46LEUo?si=JKTYvxOpz6gUJi1W

usando las librerías
werkzeug 
passlib 
cryptography


### Una librería puede desencriptar la encriptación de otra librería?

No, generalmente no es posible desencriptar datos cifrados con una librería utilizando otra librería. Cada librería de criptografía utiliza sus propios algoritmos y métodos de cifrado, y los datos cifrados con un método específico solo pueden ser desencriptados con el mismo método y la misma clave.

Por ejemplo:

- Los datos cifrados con Cryptography.fernet solo pueden ser desencriptados con cryptography.fernet utilizando la misma clave.
- Los hashes generados con werkzeug.security no pueden ser desencriptados, ya que los hashes son unidireccionales.
- Los datos cifrados con passlib solo pueden ser verificados y no desencriptados, ya que también utilizan funciones hash.

Cada librería tiene su propio método específico para cifrar y verificar datos.