"""
Main file that runs FastAPI application
"""

import uvicorn

from fastapi import FastAPI
from config import settings
from api.collect_routes import api_router
from db.local_session import create_database


def include_router(app):
    """
    Collects all api routes.
    :param app:
    :return:
    """
    app.include_router(api_router)


def start_application():
    """
    Starts main application, creates local database from .csv files.
    Needed configuration parameters are loaded from config.py file as a settings object.
    :return:app
    """
    app = FastAPI(title=settings.PROJECT_NAME, description=settings.DESCRIPTION, version=settings.PROJECT_VERSION)
    include_router(app)
    create_database()
    return app


# Generate main app
app = start_application()

if __name__ == "__main__":
    # Run main app on uvicorn server with provided HOST and PORT
    uvicorn.run("main:app", host=settings.HOST_NAME, port=settings.PORT_NUMBER, reload=settings.TESTING)
