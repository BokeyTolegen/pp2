import psycopg2
config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port=5433,
    user='postgres',
    password='12345'
)

current = config.cursor()

current.execute(
    '''
    CREATE TABLE phonebook(
        id INTEGER PRIMARY KEY,
        username VARCHAR(20),
        number VARCHAR(12),
        email VARCHAR(30)
    )
    '''
)
config.commit()
current.close()
config.close()