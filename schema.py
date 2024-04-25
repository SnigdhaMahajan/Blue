import psycopg2

# Set up the connection parameters
dbname = 'airtel'
user = 'usr_name'
password = 'Password'
host = 'localhost'  # or your host IP address
port = '5432'  # default PostgreSQL port

# Connect to the database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

# Create a cursor object
cur = conn.cursor()

# Define the query to retrieve table names
table_query = """
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public' AND table_type = 'BASE TABLE';
"""

# Execute the query to retrieve table names
cur.execute(table_query)

# Fetch all the table names
tables = cur.fetchall()

# Iterate over the tables
for table in tables:
    table_name = table[0]
    print(f"Table: {table_name}")
    print("-" * 40)

    # Define the query to retrieve column names and data types
    column_query = f"""
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_name = '{table_name}';
    """

    # Execute the query to retrieve column names and data types
    cur.execute(column_query)

    # Fetch all the column names and data types
    columns = cur.fetchall()

    # Print the column names and data types
    for column in columns:
        column_name, data_type = column
        print(f"{column_name}: {data_type}")

    print("\n")

# Close cursor and connection
cur.close()
conn.close()
