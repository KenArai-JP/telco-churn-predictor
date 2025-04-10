import pandas as pd
import mysql.connector

# Load the CSV file (update path if it's in Downloads or Desktop)
df = pd.read_csv("netflix_titles.csv", encoding="utf-8")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",       
    password="Ken4344088",   
    database="netflix_db"
)
cursor = conn.cursor()

# Insert rows into the table
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO netflix_titles (
            show_id, type, title, director, cast, country,
            date_added, release_year, rating, duration, listed_in, description
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row.fillna('').values))

conn.commit()
cursor.close()
conn.close()

print("✅ Data imported successfully!")
