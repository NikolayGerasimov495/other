import psycopg2
from config import host, user, password, db_name, port

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version();'
        )

        print(f'Server version:{cursor.fetchone()}')

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #         id serial PRIMARY KEY,
    #         first_name varchar(50) NOT NULL,
    #         last_name varchar(50) NOT NULL);"""
    #     )
    #
    # print('[INFO] Table created successfully')


    # with connection.cursor() as cursor:
    #     cursor.execute(
    #     """INSERT INTO users (first_name, last_name) VALUES
    #     ('Oleg', 'barracuda');"""
    #     )
    #
    # print("[INFO] Data was succefully inserted")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #     """SELECT last_name FROM users;"""
    #     )
    #
    #     print(cursor.fetchone())

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users;"""
    #     )
    #
    #     print("[INFO] Table was deleted")


except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL', _ex)

finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection closed')
