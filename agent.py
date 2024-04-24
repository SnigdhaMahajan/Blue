import psycopg2

# Set up the connection parameters
dbname = 'airtel'
user = 'snigdhamahajan'
password = 'new_password'
host = 'localhost'  # or your host IP address
port = '5432'  # default PostgreSQL port

# Dummy data for agents
agents_data = [
    ('101', 'Agent Name 1', 'Male', '1990-05-15', 1234567890, 'agent1@example.com', '123 Main St', 'Downtown', 'New York', 'NY', 10001, 'Passport', 'ABCD123456'),
    ('102', 'Agent Name 2', 'Female', '1985-08-20', 9876543210, 'agent2@example.com', '456 Elm St', 'Suburb', 'Los Angeles', 'CA', 90001, 'Driver License', 'EFGH789012'),
    ('103', 'Agent Name 3', 'Male', '1992-11-10', 4561237890, 'agent3@example.com', '789 Oak St', 'City Center', 'Chicago', 'IL', 60601, 'Passport', 'IJKL345678'),
    ('104', 'Agent Name 4', 'Male', '1988-03-25', 7894561230, 'agent4@example.com', '999 Pine St', 'Beachside', 'Miami', 'FL', 33101, 'Social Security Card', 'MNOP567890'),
    ('105', 'Agent Name 5', 'Female', '1995-09-30', 2345678901, 'agent5@example.com', '111 Maple St', 'Suburb', 'Seattle', 'WA', 98101, 'Passport', 'QRSTUV12345')
]

# Connect to the database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

# Create a cursor object
cur = conn.cursor()

# Define the SQL statement to insert data into the agents table
insert_query = """
INSERT INTO agents (agent_id, "Agent Name", gender, "Date of Birth", "Contact number", "Email id","Flat|House|Building no","Area|Sector|Locality",city,state,pincode,"Document Type","Verification id number")
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

try:
    # Execute the insert query for each record in the dummy data
    cur.executemany(insert_query, agents_data)
    # Commit the transaction
    conn.commit()
    print("Dummy data inserted successfully.")
except Exception as e:
    # Rollback the transaction in case of error
    conn.rollback()
    print("Error:", e)

# Close cursor and connection
cur.close()
conn.close()
