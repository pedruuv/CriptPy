from cryptography.fernet import Fernet
import os

def main():
    print("Bem vindo(a) ao CriptPy!")
    
    while True:
        
        print("Escolha uma opção:")
        
        print("1- Encriptar")
        print("2- Decriptar")
        print("3- Sair\n")
        
        opcao = int(input())
        
        if opcao == 1:
            encriptar()
        elif opcao == 2:
            #ainda não tá funcionando
            chave = obter_chave()
            decriptar(chave)
        elif opcao == 3:
            print("Até logo!")
            exit()
        else:
            print("Opção inválida")

def limpar_terminal():
        input("Pressione qualquer tecla para limpar o terminal...")
        os.system('cls' if os.name == 'nt' else 'clear')

def obter_chave():
    key = input("Digite a chave: ")
    return key

def encriptar():
    key = Fernet.generate_key()
    f = Fernet(key)
    print(f)
    print(f"Essa é a sua chave: {key}. Não perca ela!!")
    
    mensagem = input("Digite a messagem que deseja criptografar: ")
    
    mensagem_bytes = mensagem.encode('utf-8')
    
    token = f.encrypt(mensagem_bytes)
    
    print(f"Texto criptografado {token}")
    
    limpar_terminal()


def decriptar(key):
    f = Fernet(key)
    token = input("Cole a mensagem criptografada:\n")
    
    mensagem_decriptada = f.decrypt(token)
    
    print(f"Mensagem decriptada: {mensagem_decriptada}")
    
    limpar_terminal()

main()


