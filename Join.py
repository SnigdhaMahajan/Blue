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

# Define the query to perform the natural join
query = """
SELECT cr.customer_id, aa.agent_id, cr.live_location AS "Customer Location", aa."Live Location" AS "Agent Location"
FROM customer_request cr
JOIN available_agent aa ON cr.service_request = ANY(aa."Skill set")
WHERE aa.status = 'Available';
"""

# Execute the query
cur.execute(query)

# Fetch all the results
rows = cur.fetchall()

# Print the header
print("{:<15} {:<15} {:<20} {:<20}".format("Customer ID", "Agent ID", "Customer Location", "Agent Location"))
print("-" * 70)

# Print the results
for row in rows:
    print("{:<15} {:<15} {:<20} {:<20}".format(row[0], row[1], row[2], row[3]))

# Close cursor and connection
cur.close()
conn.close()
