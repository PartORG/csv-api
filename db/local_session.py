"""
THis file can be used for developing other ways to generate database Sessions.
For example for PostgreSQL or MongoDB databases.
Corresponding data should be added to config.py file and .env file too.
"""

import logging
import os
import pandas

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings


engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

logger = logging.getLogger(__name__)


def create_database():
    """
    Function that creates a new SQLite database from the set of CSV
    data files.
    :return: None
    """
    logger.info("Creating new park_info database from Underdog CSV file.")

    if os.path.exists(settings.DB_FILE):
        # Remove any old DB files for having a new database each run of API.
        os.remove(settings.DB_FILE)

    Base.metadata.create_all(bind=engine)

    for file in settings.LIST_OF_FILES:
        df = _get_dataframe_for_db(file)

        try:
            with engine.begin() as connection:
                df.to_sql(file.split('.')[0], con=connection, index=False, if_exists="append")
        except SQLAlchemyError as e:
            logger.error("The database creation failed!")
            raise
        else:
            logger.info(f"Database successfully created for - {file.split('.')[0]}.")


def _get_dataframe_for_db(file_name):
    """
    Read the CSV file, parses it to a
    Pandas dataframe, and returns a dataframe

    :return: Pandas DataFrame
    """
    logger.debug(f"Parsing CSV with Pandas --- {file_name}")
    file_path = f"{settings.DATA_CSV_FOLDER}{file_name}"

    df = pandas.read_csv(file_path)

    logger.debug("Successfully parsed Underdog CSV.")
    return df


def get_db():
    """
    Function used to get a SQLAlchemy Session

    :return: SQLAlchemy Session
    """
    logger.debug("Getting db session.")

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# TODO: as get_db() function is same, then to generate a session
#  for a new database will need only to change config.py data to use a new database.
