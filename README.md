## Schema Model 

### customers:<br>
• customer_id (varchar)<br>
• user_name  (varchar)<br>
• gender (varchar)<br>
• date_of_birth (date)<br>
• contact_number (bigint)<br>
• email_id (varchar)<br>
• Flat|House|Building_no (varchar)<br>
• Area|Sector|Locality (varchar)<br>
• city (varchar)<br>
• state (varchar)<br>
• pincode (integer)<br>
• document_type (interger)<br>
• verification_id_number (varchar)<br>
 
 
### agents:<br>
• agent_id (varchar)<br>
• Agent Name (varchar)<br>
• gender (varchar)<br>
• Date of Birth (date)<br>
• Contact number (bigint)<br>
• Email id (varchar)<br>
• Flat|House|Building no (varchar)<br>
• Area|Sector|Locality (varchar)<br>
• city (varchar)<br>
• state (varchar)<br>
• pincode (integer)<br>
• Document Type (varchar)<br>
• Verification id number (varchar)



### customer_request:<br>
• customer_id (varchar)<br>
• service_request (varchar)<br>
• live_location (point)<br>
 
 
### available_agent:<br>
• agent_id (varchar)<br>
• Skill set (ARRAY)<br>
• status (varchar)<br>
• Live Location (point)<br>
 
 
### agent_allocation:<br>
• serial_number (integer)<br>
• agent_id (varchar)<br>
• customer_id (varchar)<br>
• status (varchar)<br>
 
