from os import stat
from menu import menu, create, find, find_accounts
from master import init_master, decrypt_master, encrypt_master


if stat('master_password.txt').st_size == 0:
    init_master()

master = decrypt_master().decode('utf-8')

passw = input('Please provide the master password to start using password manager: ')

if passw == master:
    print('You\'re in. Master password is correct.')
    choice = menu()
    while choice != 'quit':
        if choice == '1':
            create()
        if choice == '2':
            find_accounts()
        if choice == '3':
            find()
        if choice == '4':
            encrypt_master(input('Enter new master password:'))
            break
        else:
            choice = menu()
    exit()
else:
    print(decrypt_master())
    print(master)
    with open('master_password.txt', 'r') as f:
        print(f.read())
    print('Incorrect master password.')
    exit() 
