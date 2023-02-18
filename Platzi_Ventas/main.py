<<<<<<< HEAD



if __name__ == '__main__':
    pass
=======
clients = 'Pablo,Ricardo,'

def create_client(client_name):
    global clients

    clients += client_name
    _add_comma()


def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients += ','


if __name__ == '__main__':
<<<<<<< HEAD
    clients += 'David'
    print(clients)
>>>>>>> 42f71ed (Update All and Start Project)
=======
    list_clients()

    create_client('David')
    
    list_clients()
>>>>>>> f57818f (Usando Funciones en Nuestro Proyecto)
