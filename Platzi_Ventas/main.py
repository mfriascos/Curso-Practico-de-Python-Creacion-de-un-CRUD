import sys

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

    print('\n'+clients+'\n')


def _add_comma():
    global clients

    clients += ','


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input("\nWhat is the client name? ").capitalize()
        
        if client_name == 'Exit':
            client_name = None
            break;

    if not client_name:
        print('\n')
        sys.exit()

    return client_name



def _client_not_found():
    print("\nClient is not in clients list\n")


def update_client(client_name,updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name,updated_client_name)
    else:
        _client_not_found()


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name+',','')
    else:
        _client_not_found()


def search_client(client_name):
    global clients

    clients_list = clients.split(',')

    for client in clients_list: 
        if client != client_name:
            continue
        else: 
            return True


def _print_welcome():
    print('\nWELCOME TO PLATZI VENTAS\n')
    print('*'*50)
    print('\nWhat would do you like to do today?')
    print("\n[C]reate client")
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client\n')


if __name__ == '__main__':
    _print_welcome()

    command = input().upper()

    if command == 'C':
        create_client(_get_client_name())
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name,updated_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print("\nThe client is in client's list\n")
        else:
            print(f"\nThe client {client_name} isn't in client's list\n")
    else:
        print("\nInvalid command")
