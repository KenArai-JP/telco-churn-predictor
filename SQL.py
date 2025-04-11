import pandas as pd
import mysql.connector

df = pd.read_csv("netflix_titles.csv", encoding="utf-8")

conn = mysql.connector.connect(
    host="localhost",
    user="root",       
    password="",   
    database="netflix_db"
)
cursor = conn.cursor()

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
