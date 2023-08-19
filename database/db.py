import psycopg2

def get_database_connection():
    # Conectar a la base de datos
    conn = psycopg2.connect(
        dbname='postgres',
        user='fl0user',
        password='r5thMngSxWj6',
        host='ep-solitary-meadow-48135541.us-east-2.aws.neon.tech',
        port='5432'
    )
    return conn

def fetch_all_data():
    conn = get_database_connection()
    cursor = conn.cursor()
    # Realizar una consulta
    cursor.execute('SELECT * FROM usuarios')
    rows = cursor.fetchall()
    # Cerrar conexión
    conn.close()
    return  [{"nombre": row[1], "edad": row[2], "plan": row[3], "documento": row[4]} for row in rows]

def insert_data(nombre, edad, plan, documento):
    conn = get_database_connection()
    cursor = conn.cursor()
    
    # Sentencia SQL para insertar datos
    query = "INSERT INTO usuarios (nombre, edad, plan, documento) VALUES (%s, %s, %s, %s)"
    values = (nombre, edad, plan, documento)

    cursor.execute(query, values)
    conn.commit()  # Es importante hacer commit para que los cambios se guarden

    # Cerrar conexión
    conn.close()