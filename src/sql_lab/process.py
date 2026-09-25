import logging
import os

import pandas as pd
import mysql.connector

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",

)

logger = logging.getLogger(__name__)

DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBNAME = os.getenv("DBNAME")

def read_data(filename):
    """Read a CSV file into a pandas DataFrame."""
    logger.info("Reading data from %s", filename)
    data = pd.read_csv(filename)
    logger.info("Read %d rows", len(data))
    return data

def clean_data(data):
    """Remove rows containing missing values from the DataFrame."""
    cleaned = data.dropna()
    logger.info("Rows before cleaning: %d", len(data))
    logger.info("Rows after cleaning: %d", len(cleaned))
    return cleaned

def load_data(data, table):
    """Create the MySQL table and load the cleaned data."""
    logger.info("Connecting to the database")
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host = DBHOST,
            user = DBUSER,
            password = DBPASS,
            database = DBNAME,
        )

        cursor = connection.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS mock (
            id BIGINT,
            `group` VARCHAR(255),
            age BIGINT,
            city VARCHAR(255),
            salary DOUBLE,
            active VARCHAR(255)
        )
        """

        cursor.execute(create_table_query)

        insert_query = """
        INSERT INTO mock (
            id,
            `group`,
            age,
            city,
            salary,
            active
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        for _, row in data.iterrows():
            cursor.execute(
                insert_query,
                (
                    row["id"],
                    row["group"],
                    row["age"],
                    row["city"],
                    row["salary"],
                    row["active"],
                ),
            )

        connection.commit()

        logger.info(
            "Successfully loaded %d rows into %s",
            len(data),
            table,
        )

    except mysql.connector.Error as error:
        logger.error("Database error: %s", error)
        raise

    finally:
        if cursor is not None:
                cursor.close()

        if connection is not None:
                connection.close()


def main():
    """Run the complete data processing pipeline."""
    data = read_data("MOCK_DATA.csv")
    cleaned_data = clean_data(data)
    load_data(cleaned_data, "mock")
              
if __name__ == "__main__":
    main()