
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('attendance.db')
c = conn.cursor()

# Query to select all student IDs and timestamps from the detected_faces table
c.execute("SELECT student_id, timestamp FROM detected_faces")

# Fetch all results
results = c.fetchall()

# Print the names (student IDs) and their recognition timestamps
for row in results:
    student_id, timestamp = row
    print(f"Student ID: {student_id}, Recognition Time: {timestamp}")  # Print student ID and timestamp

# Close the database connection
conn.close()