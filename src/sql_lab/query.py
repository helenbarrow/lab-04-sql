import os
import logging

import mysql.connector

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_connection():
    """Create and return a connection to the MySQL database."""
    return mysql.connector.connect(
        host = os.environ["DBHOST"],
        user = os.environ["DBUSER"],
        password = os.environ["DBPASS"],
        database = os.environ["DBNAME"],
    )

def get_data_by_group(value):
    """Return all rows from mock where the group column equals value."""
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT *
            FROM mock
            WHERE `group` = %s
        
        """

        cursor.execute(query, (value,))
        rows = cursor.fetchall()

        logging.info("REtrieved %d rows for group '%s'", len(rows), value)

        return rows

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
        return []

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()

def plot_counts(groupby):
    """Count rows for each distinct value of the specified column."""
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = f"""
            SELECT `{groupby}`, COUNT(*)
            FROM mock
            GROUP BY `{groupby}`
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        logging.info("Retrieved counts grouped by '%s'", groupby)

        return rows

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
        return[]

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()

def main():
    """Run example queries against the mock table."""

    group_results = get_data_by_group("The Avengers")

    print("Rows in selected group:")
    for row in group_results:
        print(row)

    count_results = plot_counts("group")

    print("\nCounts by group:")
    for row in count_results:
        print(row)

if __name__ == "__main__":
    main()