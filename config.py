"""
Contains all settings for running the main FastAPI app
"""
import os
from pathlib import Path


class Settings:
    """
    Class that contains all settings to run application
    """
    # Root path
    PROJECT_ROOT = Path(__file__).parent

    # Run environment variables
    HOST_NAME = 'localhost'
    PORT_NUMBER = 8888
    TESTING = True

    # FastAPI app parameters
    PROJECT_NAME = "CSV Data API"
    PROJECT_VERSION = "0.0.1"
    DESCRIPTION = "This is testing API to load data from csv files and use it for a database."

    # CSV files data
    DB_FILE = f"{PROJECT_ROOT}/local_data/local_database.db"
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_FILE}"
    DATA_CSV_FOLDER = f"{PROJECT_ROOT}/local_data/csv_files/"
    LIST_OF_FILES = os.listdir(f"{PROJECT_ROOT}/local_data/csv_files/")


# initialization of class instance
settings = Settings()
