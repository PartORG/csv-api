# csv-api

A small API to work with .csv file data using Python and FastAPI.

## Overview
The `csv-api` project provides a RESTful API for interacting with CSV files. It allows you to upload, parse, and store CSV data in a database, making it easy to access and manipulate your data programmatically.

## Features

### Data Upload and Parsing
- **Upload CSV Files**: Easily upload .csv files through the API.
- **Parse CSV Data**: Utilize Pandas for parsing CSV data into structured formats.

### Database Management
- **Store Data**: Store parsed data in a SQLite database using SQLAlchemy.
- **CRUD Operations**: Perform CRUD operations on stored data via the API endpoints.

### Configuration and Environment Variables
- **Environment Variables**: Manage configuration through environment variables using `python-dotenv`.
- **Database URI**: Specify the database URI in the `.env` file for connection settings.

## How It Works

The project is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. The API routes are defined in `api/v1/route_information.py` and `api/v1/route_production.py`, which handle different types of CSV data.

### Architecture Diagram
```
csv-api/
├── api/
│   ├── collect_routes.py
│   ├── v1/
│   │   ├── route_information.py
│   │   └── route_production.py
├── config.py
├── db/
│   ├── cruds/
│   │   ├── crud_information.py
│   │   └── crud_production.py
│   ├── local_session.py
│   └── models/
│       ├── information_model.py
│       └── production_model.py
├── functional_design_1.pdf
├── local_data/
│   ├── csv_files/
│   │   ├── Bemmel.csv
│   │   ├── Netterden.csv
│   │   ├── Stadskanaal.csv
│   │   ├── Windskanaal.csv
│   │   ├── Zwartenbergseweg.csv
│   │   └── park_info.csv
│   └── local_database.db
├── main.py
├── requirements.txt
├── schemas/
│   ├── information_schemas.py
│   └── production_schemas.py
└── test_api.py
```

## Technology Stack

| Technology | Purpose |
|------------|---------|
| **FastAPI** | A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. |
| **Uvicorn** | An ASGI server implementation for serving FastAPI applications. |
| **SQLAlchemy** | A SQL toolkit and Object-Relational Mapping (ORM) system for Python. |
| **Python-dotenv** | Loads environment variables from a `.env` file into `os.environ`. |
| **Pydantic** | Data validation and settings management using Python type annotations. |
| **Pytest** | A mature full-featured Python testing tool. |
| **Requests** | HTTP for Humans. |
| **Python-multipart** | Parse multipart/form-data, including file uploads. |
| **Pandas** | An open-source data manipulation and analysis library. |

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

The project uses a `.env` file to manage configuration variables. Ensure you have the following in your `.env` file:

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

### Upload CSV Files

You can upload CSV files using the `/upload` endpoint. The request should be a multipart/form-data with the file field named `file`.

```commandline
curl -X 'POST' \
  'http://localhost:8888/upload' \
  -H 'accept: application/json' \
  -F 'file=@path/to/your/file.csv'
```

### Retrieve Data

You can retrieve data from the database using the `/data` endpoint.

```commandline
curl -X 'GET' \
  'http://localhost:8888/data' \
  -H 'accept: application/json'
```

## Project Structure

The project structure is organized as follows:

- `api/`: Contains API route definitions.
- `config.py`: Configuration settings.
- `db/`: Database-related files, including models and CRUD operations.
- `functional_design_1.pdf`: Functional design document.
- `local_data/`: Local data files and database file.
- `main.py`: Main entry point of the application.
- `requirements.txt`: List of project dependencies.
- `schemas/`: Pydantic schemas for data validation.
- `test_api.py`: Test cases.

## Development

To develop this project, follow these steps:

1. **Set up a virtual environment**:
    ```commandline
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install dependencies**:
    ```commandline
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```commandline
    python main.py
    ```

4. **Write tests**:
    Run tests using Pytest:
    ```commandline
    pytest
    ```

## Testing

The project includes unit tests in `test_api.py`. You can run these tests using Pytest:

```commandline
pytest
```

## Limitations

- The API currently supports only SQLite as the database.
- Error handling is basic and may need improvement for production use.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.