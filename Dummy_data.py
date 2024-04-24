import psycopg2

# Set up the connection parameters
dbname = 'airtel'
user = 'snigdhamahajan'
password = 'new_password'
host = 'localhost'  # or your host IP address
port = '5432'  # default PostgreSQL port

# Connect to the database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

# Create a cursor object
cur = conn.cursor()

# Define the dummy data for customer_request
# Dummy data for customer_request with live_location
# Dummy data for customer_request with live_location
customer_request_data = [
    ('1', 'Network', '(40.7128, -74.0060)'),
    ('2', 'Data', '(34.0522, -118.2437)'),
    ('3', 'sim', '(41.8781, -87.6298)'),
]

# Dummy data for available_agent with live_location
available_agent_data = [
    ('101', ['Data','sim','broadband'], 'Available', '(37.7749, -122.4194)'),
    ('102', ['Data','Network','broadband'], 'Available', '(34.0522, -118.2437)'),
    ('103', ['Network'], 'Unavailable', '(41.8781, -87.6298)')  # This agent is unavailable
]


# Define the queries to insert data into customer_request and available_agent tables
customer_request_query = """
INSERT INTO customer_request (customer_id, service_request, live_location)
VALUES (%s, %s, %s);
"""

available_agent_query = """
INSERT INTO available_agent (agent_id, "Skill set", status, "Live Location")
VALUES (%s, %s, %s, %s);
"""

try:
    # Insert dummy data into customer_request table
    cur.executemany(customer_request_query, customer_request_data)

    # Insert dummy data into available_agent table
    cur.executemany(available_agent_query, available_agent_data)

    # Commit the transaction
    conn.commit()
    print("Dummy data inserted successfully.")

    # Now perform the natural join and print the results
    # Define the query to perform the natural join
    # Execute the query

    # Fetch all the results
    rows = cur.fetchall()

    # Print the header
    print("{:<15} {:<15} {:<20} {:<20}".format("Customer ID", "Agent ID", "Customer Location", "Agent Location"))
    print("-" * 70)

    # Print the results
    for row in rows:
        print("{:<15} {:<15} {:<20} {:<20}".format(row[0], row[1], row[2], row[3]))

except psycopg2.Error as e:
    # Rollback the transaction in case of error
    conn.rollback()
    print("Error:", e)

# Close cursor and connection
cur.close()
conn.close()
