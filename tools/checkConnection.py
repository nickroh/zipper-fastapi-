# check_connection.py

import asyncio
import databases

DATABASE_URL = "postgresql://user:password@localhost/dbname"

async def check_database_connection():
    database = databases.Database(DATABASE_URL)

    try:
        await database.connect()
        print("Database connection is successful.")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    finally:
        await database.disconnect()

if __name__ == "__main__":
    asyncio.run(check_database_connection())