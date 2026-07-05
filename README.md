# csv-api

A small API to work with .csv file data using Python and FastAPI.

## Overview
The `csv-api` project provides a RESTful API for interacting with CSV files. It allows you to upload, parse, and store CSV data in a database, making it easy to access and manipulate your data programmatically.

## Features

### Upload and Parse CSV Files
- **What it does**: Allows users to upload CSV files.
- **Why it exists**: To provide an easy way to import data into the system.
- **Why it is useful**: Enables quick data ingestion for further processing or analysis.

### Store Data in a Database
- **What it does**: Parses uploaded CSV files and stores the data in a database.
- **Why it exists**: To persistently store data for long-term use.
- **Why it is useful**: Ensures that data is not lost and can be accessed at any time.

## How It Works

The `csv-api` uses FastAPI to create a RESTful API. The main entry point is `main.py`, which sets up the application, connects to the database, and mounts the routes defined in `api/collect_routes.py`.

### Architecture Diagram
```
+-------------------+
|      main.py        |
|  - Sets up app    |
|  - Connects to DB |
|  - Mounts routes  |
+---------+---------+
          |
          v
+---------+---------+
| api/collect_routes.py |
|  - Defines API endpoints for uploading and parsing CSV files. |
+-------------------+
```

## Technology Stack

| Technology | Purpose |
|------------|---------|
| **FastAPI** | Asynchronous web framework for building APIs. |
| **Uvicorn** | ASGI server implementation for running FastAPI applications. |
| **SQLAlchemy** | SQL toolkit and Object-Relational Mapping (ORM) library. |
| **Python-dotenv** | Loads environment variables from a `.env` file into `os.environ`. |
| **Pydantic** | Data validation and settings management using Python type annotations. |
| **Pytest** | Simple and scalable testing framework for Python. |
| **Requests** | HTTP library for making requests to external APIs. |
| **Python-multipart** | Library for parsing multipart/form-data, which is used for file uploads. |
| **Pandas** | Data manipulation and analysis library. |

## Requirements

To run this project, you need the following dependencies:

- **Python**: 3.7 or higher
- **fastapi**: 0.68.1
- **uvicorn**: 0.15.0
- **sqlalchemy**: 1.4.23
- **python-dotenv**: 0.19.0
- **pydantic**: 1.8.2
- **pytest**: 6.2.5
- **requests**: 2.26.0
- **python-multipart**: 0.0.5
- **pandas**: 1.3.3

## Installation

To set up your environment, follow these steps:

```commandline
>> python3 -m venv venv
>> source venv/bin/activate
>> pip install -r requirements.txt
```

## Configuration

The project uses a `.env` file to load environment variables. Ensure you have the following variables set in your `.env` file:

```plaintext
DATABASE_URL=sqlite:///./local_database.db
```

## Quick Start

To run the API, execute the `main.py` file:

```commandline
>> python main.py
```

You will see output similar to this:

```commandline
11-04 09:10 db.local_session DEBUG    Parsing CSV with Pandas --- Bemmel.csv
11-04 09:10 db.local_session DEBUG    Successfully parsed Underdog CSV.
11-04 09:10 db.local_session INFO     Database successfully created for - Bemmel.
INFO:     Will watch for changes in these directories: ['/home/ievgen/csv-api']
INFO:     Uvicorn running on http://localhost:8888 (Press CTRL+C to quit)
INFO:     Started reloader process [63531] using StatReload
INFO:     Started server process [63537]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

To access the API documentation, navigate to `http://localhost:8888/docs` in your web browser.

## Usage

### Upload a CSV File

You can upload a CSV file using the `/upload-csv` endpoint. Here is an example of how to do it using `curl`:

```commandline
>> curl -X POST "http://localhost:8888/upload-csv" -F "file=@path/to/your/file.csv"
```

### Get CSV Data

You can retrieve data from the database using the `/get-data` endpoint. Here is an example of how to do it using `curl`:

```commandline
>> curl -X GET "http://localhost:8888/get-data"
```

## Project Structure

```
csv-api/
├── .gitignore
├── README.md
├── api/
│   ├── collect_routes.py
│   └── v1/
│       ├── route_information.py
│       └── route_production.py
├── config.py
├── db/
│   ├── cruds/
│   │   ├── crud_information.py
│   │   └── crud_production.py
│   ├── local_session.py
│   ├── models/
│   │   ├── information_model.py
│   │   └── production_model.py
│   └── schemas/
│       ├── information_schemas.py
│       └── production_schemas.py
├── functional_design_1.pdf
├── local_data/
│   ├── csv_files/
│   │   ├── Bemmel.csv
│   │   ├── Netterden.csv
│   │   ├── Stadskanaal.csv
│   │   ├── Windskanaal.csv
│   │   └── Zwartenbergseweg.csv
│   └── local_database.db
├── main.py
├── requirements.txt
└── test_api.py
```

## Development

The development workflow involves setting up a virtual environment, installing dependencies, and running the application. The project uses `pytest` for testing.

To run tests:

```commandline
>> pytest
```

## Testing

The project includes unit tests in `test_api.py`. These tests ensure that the API endpoints are working as expected.

## Limitations

- **Database Support**: Currently supports SQLite, but can be extended to support other databases.
- **File Size**: The API does not handle large file uploads efficiently. Consider implementing chunked uploads for larger files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.