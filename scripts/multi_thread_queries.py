import mysql.connector
from threading import Thread

def execute_query(query, connection_details):
    try:
        conn = mysql.connector.connect(**connection_details)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    connection_details = {
        "host": "automated-mysql-server-group3.mysql.database.azure.com",
        "user": "admin_group3",
        "password": "astha@group3",
        "database": "group3"
    }

    queries = [
        "INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity) VALUES ('Miami', '2023-01-04', 25.0, 1.0, 85.0)",
        "SELECT * FROM ClimateData WHERE temperature > 20.0",
        "UPDATE ClimateData SET humidity = 90.0 WHERE location = 'Toronto'"
    ]

    threads = []
    for query in queries:
        thread = Thread(target=execute_query, args=(query, connection_details))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
