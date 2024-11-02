from passlib.context import CryptContext

# CryptContext # es un contexto para hacer encriptación

contexto = CryptContext(
    schemes = ["pbkdf2_sha256"], # algoritmo o métodos de encriptación
    default = "pbkdf2_sha256", # algoritmo por defecto que va a usar
    pbkdf2_sha256__default_rounds = 30000 # iteraciones a realizar para reducir la posibilidad de crackeo
)

texto = "x?1_P-1M.4!eM"

texto_encriptado = contexto.hash(texto)
print(texto_encriptado)
print(contexto.verify(texto, texto_encriptado)) # True