from db_settings import store_passwords, find_users, find_password 


def menu():
    print('-' * 30)
    print(('-' * 13) + 'Menu' + ('-' * 13))
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('4. Change a master password')
    print('Type "quit" to exit.')
    print('-' * 30)
    return input('Your choice: ')


def create():
   print()
   site = input('Please proivide the name of the site or app you want to generate a password for: ')
   passw = input('Please provide a simple password for this site: ')
   user_email = input('Please provide a user email for this app or site: ')
   username = input('Please provide a username for this app or site (optional): ')
   if username == None:
       username = ''
   store_passwords(passw, user_email, username, site)


def find():
   site = input('Please proivide the name of the site or app you want to find the password to: ')
   find_password(site)


def find_accounts():
   user_email = input('Please proivide the email that you want to find accounts for: ') 
   find_users(user_email)
