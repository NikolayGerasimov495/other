import psycopg2


conn = psycopg2.connect(database='1111',
                        user='postgres',
                        password='postgres',
                        host='127.0.0.1',
                        port='5433')
print('Done!')

conn.close()
