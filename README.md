# csv-api

This is a small API to work with .csv file data.

## Overview
The `csv-api` project provides a RESTful API for interacting with CSV files using Python and FastAPI. It allows you to upload, parse, and store CSV data in a database, making it easy to access and manipulate your data programmatically.

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

## Usage
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

To stop the local API server, press `CTRL+C` in the terminal. You will see messages indicating that the API has stopped:

```commandline
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [63818]
INFO:     Stopping reloader process [63813]
```

For deployment, you can deploy this API on a dedicated server or use it with cloud services like AWS and Azure.