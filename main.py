# main.py

from user import create_user, list_users, delete_user_by_email

def main():
    while True:
        print("\n1. Criar Usuário\n2. Listar Usuários\n3. Excluir Usuários\n4. Finalizar")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            create_user(name, email)
            print("Usuário Criado com sucesso")
    
        elif choice == '2':
            list_users()
    
        elif choice == '3':
            email = input("Digite o email do Usuário a ser removido: ")
            delete_user_by_email(email)
            print("Usuário removido!")
    
        elif choice == '4':
            break
    
        else:
            print("Opção Inválida! ")


if __name__ == "__main__":
    main()
            

    