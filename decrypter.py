# decrypter.py
import os # Biblioteca do Sistema Operacional
import pyaes # Biblioteca de Criptografia
# Abertura de Arquivo Criptografado
file_name = 'teste.txt.ransomwaretroll'
file = open(file_name, 'rb') # 'rb' é Leitura
file_data = file.read()
file.close()
# Setting da Chave de Descriptografia
key = b'testeransomwares' # Chave de Criptografia
aes = pyaes.AESModeOfOperationCTR(key) # Aplicação da Criptografia
decrypt_data = aes.decrypt(file_data) # Aplicação da Descriptografia
# Remoção do Arquivo Criptografado
os.remove(file_name)
# Criação de Arquivo Descriptografado
new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()