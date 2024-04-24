import psycopg2

# Set up the connection parameters
dbname = 'airtel'
user = 'snigdhamahajan'
password = 'new_password'
host = 'localhost'  # or your host IP address
port = '5432'  # default PostgreSQL port

try:
    # Connect to the database
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    print("Connected to database.")

    # Create a cursor
    cur = conn.cursor()

    # Define the delete query
    delete_query = """
    DELETE FROM available_agent WHERE agent_id > '0';  
    """

    # Execute the query
    cur.execute(delete_query)
    print("Records deleted successfully.")

    # Commit the transaction
    conn.commit()

except psycopg2.Error as e:
    print("Unable to connect to the database:", e)

finally:
    # Close the cursor and connection
    cur.close()
    conn.close()
