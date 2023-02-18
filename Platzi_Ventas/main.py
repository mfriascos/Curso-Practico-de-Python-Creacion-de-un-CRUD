clients = 'Pablo,Ricardo,'

def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else: 
        print("\nClient already in the client's list\n")


def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients += ','

def _print_welcome():
    print('\nWELCOME TO PLATZI VENTAS\n')
    print('*'*50)
    print('\nWhat would do you like to do today?')
    print("\n[C]reate client")
    print('[D]elete client\n')

if __name__ == '__main__':
    _print_welcome()

    command = input()

    if command == 'C' or command == 'c':
        client_name = input("\nWhat is the client name? ")
        create_client(client_name)
        list_clients()
    elif command == 'D' or command == 'd':
        pass
    else:
        print("\nInvalid command")
