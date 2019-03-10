# -*- coding: utf-8 -*-
"""
clients = 'Edwin, Alejandro,'


if __name__ == '__main__':
    clients += 'Juan'
    print(clients)
"""
# en este bloque incorpore la variable dentro de la funcion

"""
clients = 'Edwin, Alejandro,'


def create_clients(clients_name):
    global clients

    clients += clients_name
    _add_comma()


def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients += ','


if __name__ == '__main__':
    list_clients()
    create_clients('Andrea')
    list_clients()


# pendiente por hacer un fork para subir a git
"""

# clase 12 add nue clients and valid already clients_name
"""
clients = 'Edwin, Alejandro, '


def create_clients(clients_name):
    global clients

    if clients_name not in clients:
        clients += clients_name
        _add_comma
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate cliente')
    print('[D]elete cliente')


if __name__ == '__main__':
    _print_welcome()

    command = input()

    if command == 'C':
        clients_name = input('What is the client name?')
        create_clients(clients_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Invalid command')
"""

# clase 15 update of clients pendiente to up githib
# -*- coding: utf-8 -*-

# cambiando el main.py
"""
clients = 'Edwin, Alejandro, '


def create_clients(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients
    print(clients)


def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_name + ',')
    else:
        print('Client is not in client\'s list')


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate cliente')
    print('[U]pdate client')
    print('[D]elete cliente')


def _get_client_name():
    return input('What is the client name? ')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_clients(client_name)
        list_clients()
    elif command == 'D':
        pass
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name ')
        update_client(client_name, update_client_name)
        list_clients()

    else:
        print('Invalid command')
"""

# clase 16 integrando el delete
# pendiente subir a github

# -*- coding: utf-8 -*-

# vamos a agregar la funcion delete a nuestro script
# crud   [c]reated , [r]read or retreive, [u]ptade, [d]elete
"""
clients = 'Edwin, Alejandro, '


def create_clients(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients
    print(clients)


def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_name + ',')
    else:
        print('Client is not in client\'s list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client is not in clients list')


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate cliente')
    print('[U]pdate client')
    print('[D]elete cliente')


def _get_client_name():
    return input('What is the client name? ')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_clients(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name ')
        update_client(client_name, update_client_name)
        list_clients()

    else:
        print('Invalid command')
"""

# clase 18 incorporamos la funcion de search
# con la funcion for loops en clients_list = clients.split(',')
# vamos a incorporar esta funcion en platzi_ventas
# vamos a usar un for loop para buscar a un cliente
# dentro de nuestra lista de clients
# las comas nos permiten generar un separador

clients = 'Edwin, Alejandro, '


def create_clients(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients
    print(clients)


def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_name + ',')
    else:
        print('Client is not in client\'s list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client is not in clients list')


def search_client(client_name):
    clients_list = clients.split(',')

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]ead client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_name():
    return input('What is the client name? ')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_clients(client_name)
        list_clients()
    elif command == 'R':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name ')
        update_client(client_name, update_client_name)
        list_clients()

    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')

# revizar el 19_subclass_main.py  
