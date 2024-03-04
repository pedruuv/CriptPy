from cryptography.fernet import Fernet
import os

def main():
    print("Bem vindo(a) ao CriptPy!")
    
    while True:
        
        print("Escolha uma opção:")
        
        print("1- Encriptar")
        print("2- Decriptar")
        print("3- Sair")
        print("4- Gerar chave\n")
        
        opcao = int(input())
        
        if opcao == 1:
            key = get_key()
            input_file = input("Digite o nome do arquivo que deseja encriptar(Ex: arquivo.txt) ")
            output_file = input("Digite o nome do arquivo que deseja salvar(Ex: arquivo_encriptado.txt): ")
            encriptar(input_file, output_file)
        elif opcao == 2:
            #ainda não tá funcionando
            key = get_key()
            input_file = input("Digite o nome do arquivo que deseja decriptar(Ex: arquivo_encriptado.txt) ")
            output_file = input("Digite o nome do arquivo que deseja salvar(Ex: arquivo_decriptado.txt): ")
            decriptar(key, input_file, output_file)
        elif opcao == 3:
            print("Até logo!")
            exit()
        elif opcao == 4:
            gen_key()
        else:
            print("Opção inválida")

def limpar_terminal():
        input("Pressione qualquer tecla para limpar o terminal...")
        os.system('cls' if os.name == 'nt' else 'clear')

def obter_chave():
    key = input("Digite a chave: ")
    return key

def gen_key():
    key = Fernet.generate_key()
    
    with open('mykey.key', 'wb') as mykey:
        mykey.write(key)
    limpar_terminal()

def get_key():
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
    return key

def encriptar(input_file, output_file):
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
    fernet = Fernet(key)
    
    with open(input_file, 'rb') as f:
        data = f.read()
        encrypted_data = fernet.encrypt(data)
    
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)
    
    limpar_terminal()


def decriptar(key, input_file, output_file):
    fernet = Fernet(key)
    with open(input_file, 'rb') as f:
        data = f.read()
        decrypted_data = fernet.decrypt(data)
        
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)
    
    limpar_terminal()

main()


