import os
from cryptography.fernet import Fernet

# Função p/ criptografar arquivos
def decriptar_arquivo(file_path, key):
    with open(file_path, "rb") as file:
        conteudo = file.read()                      # lendo arquivo
    fernet = Fernet(key)                            # Instanciando classe
    decriptar_arquivo = fernet.decrypt(conteudo)
    with open(file_path, "wb") as file:
        file.write(decriptar_arquivo)               # sobrescrevendo arquivo

# Função p/ criptografar pasta com subpastas e arquivos
def decriptar_arq_em_pastas(folder_path, key):
    for root, dirs, files in os.walk(folder_path):  # definindo pasta raiz, com subpastas e arquivos no diretório escolhido
        for file in files:
            file_path = os.path.join(root, file)
            decriptar_arquivo(file_path, key)

with open("chave.key", "rb") as key_file:
    key = key_file.read()                           # Lendo chave de decryptação

# Caminho da pasta que você deseja criptografar os arquivos
folder_path = r"C:\Users\profile/documents/Infos"

decriptar_arq_em_pastas(folder_path, key)           # Usando o caminho da pasta que deve ser decryptada e a chave
