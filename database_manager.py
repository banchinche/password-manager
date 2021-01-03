import psycopg2

def store_passwords(password, user_email, username, link):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO passwords (password, email, username, link) VALUES (%s, %s, %s, %s)"""
        record_to_insert = (password, user_email, username, link)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)

def connect():
    try:
        connection = psycopg2.connect(user='andrew', password='andrew', database='passwords')
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)

def find_password(link):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT password FROM passwords WHERE link = '""" + link + "'"
        cursor.execute(postgres_select_query, link)
        connection.commit()
        result = cursor.fetchone()
        print('Password is: ' )
        print(result[0])
    
    except (Exception, psycopg2.Error) as error:
        print(error)
def find_users(user_email):
    data = ('Password: ', 'Email: ', 'Username: ', 'Link: ') 
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM passwords WHERE email = '""" + user_email + "'"
        cursor.execute(postgres_select_query, user_email)
        connection.commit()
        result = cursor.fetchall()
        print('\nInfo:')
        for row in result:
            for i in range(0, len(row)):
                print(data[i] + row[i])
        print('-'*30)
    except (Exception, psycopg2.Error) as error:
        print(error)
