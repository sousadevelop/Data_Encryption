import os
from cryptography.fernet import Fernet

# Função p/ criptografar arquivos
def encriptar_arquivo(file_path, key):
    with open(file_path, "rb") as file:
        conteudo = file.read()                      # lendo arquivo
    fernet = Fernet(key)                            # Instanciando classe
    encriptar_arquivo = fernet.encrypt(conteudo)
    with open(file_path, "wb") as file:
        file.write(encriptar_arquivo)               # sobrescrevendo arquivo

# Função p/ criptografar pasta com subpastas e arquivos
def encriptar_arq_em_pastas(folder_path, key):
    for root, dirs, files in os.walk(folder_path):  # definindo pasta raiz, com subpastas e arquivos no diretório escolhido
        for file in files:
            file_path = os.path.join(root, file)
            encriptar_arquivo(file_path, key)

# Chave de criptografia
key = Fernet.generate_key()

# Caminho da pasta que você deseja criptografar os arquivos
folder_path = r"C:\Users\victt\OneDrive\Imagens\Infos"

encriptar_arq_em_pastas(folder_path, key)

with open("chave.key", "wb") as key_file:
    key_file.write(key)                             # Escrevendo chave de criptografia em arquivo



#### Infos Extras ####

## rb é para ler arquivos binários
## wb é para escrever em arquivos binários