# csv-api
This is a small API to work with .csv file data.

## Installation
To prepare an environment to run this API, you need to set up a virtual environment with Python > 3.7 and use the `requirements.txt` file to install all dependencies. Execute the following commands in your project folder:

```commandline
>> python3 -m venv venv
>> source venv/bin/activate
>> pip install -r requirements.txt
```

## Usage
After setting up your local virtual environment, simply execute the `main.py` file with Python in the terminal. You will see output similar to this:

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