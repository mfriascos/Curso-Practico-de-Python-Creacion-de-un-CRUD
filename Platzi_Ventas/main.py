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


def _get_client_name():
    return input("\nWhat is the client name? ")

def update_client(client_name,updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name+',',updated_client_name+',')
    else:
        print("Client is not in clients list")
        list_clients()

def _print_welcome():
    print('\nWELCOME TO PLATZI VENTAS\n')
    print('*'*50)
    print('\nWhat would do you like to do today?')
    print("\n[C]reate client")
    print('[U]pdate client')
    print('[D]elete client\n')

if __name__ == '__main__':
    _print_welcome()

    command = input().upper()

    if command == 'C':
        create_client(_get_client_name())
        list_clients()
    elif command == 'D':
        pass
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name,updated_client_name)
        list_clients()
    else:
        print("\nInvalid command")
