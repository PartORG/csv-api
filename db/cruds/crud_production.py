"""
FIle with set of CRUD (Create, Read, Update and Delete) operations connected with Production data Tables.
Can be easily added new functions for new endpoint set for Production data Tables.
"""

import logging
import sys

from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..models.production_model import Bemmel, Netterden, Stadskanaal, Windskanaal, Zwartenbergseweg


logger = logging.getLogger(__name__)


def get_all_prods(db: Session, table: str):
    """
    Get ALL data from specific production table.
    Returns a very big set of data. Was added here for example.
    :param db:
    :param table:
    :return: list of all data from table
    """

    # check that provided Park name exists in production models
    try:
        prod_table = getattr(sys.modules[__name__], table)
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Park {table} not found in database.")

    logger.debug(f"Retrieving Information for {table}.")
    return db.query(prod_table).order_by(prod_table.id.desc()).all()


def get_prod_period_empty(db: Session, table: str):
    """
    Get data from Park table for empty period - will return last 10 data entries.
    :param db:
    :param table:
    :return: List of 10 last data entries
    """
    try:
        prod_table = getattr(sys.modules[__name__], table)
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Park {table} not found in database.")

    logger.debug(f"Retrieving Information for {table}.")
    return db.query(prod_table).order_by(prod_table.datetime.desc()).limit(10).all()


def get_prod_period_only_start(start: str, db: Session, table: str):
    """
    Return data from provided park for provided period - only start date, end date is the end of the table data.
    :param start:
    :param db:
    :param table:
    :return: List of data entries.
    """
    try:
        prod_table = getattr(sys.modules[__name__], table)
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Park {table} not found in database.")

    logger.debug(f"Retrieving Information for {table}.")
    return db.query(prod_table).order_by(prod_table.datetime.desc()).filter(prod_table.datetime >= start).all()


def get_prod_period_only_end(end: str, db: Session, table: str):
    """
    Return data from provided park for provided period - only end date, start date is the first entry of the table data.
    :param end:
    :param db:
    :param table:
    :return: List of data entries.
    """
    try:
        prod_table = getattr(sys.modules[__name__], table)
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Park {table} not found in database.")

    logger.debug(f"Retrieving Information for {table}.")
    return db.query(prod_table).order_by(prod_table.datetime.desc()).filter(prod_table.datetime <= end).all()


def get_prod_period(start: str, end: str, db: Session, table: str):
    """
    Return data from provided park for provided period.
    :param end:
    :param db:
    :param table:
    :return: List of data entries.
    """
    try:
        prod_table = getattr(sys.modules[__name__], table)
    except AttributeError:
        raise HTTPException(status_code=404, detail=f"Park {table} not found in database.")

    logger.debug(f"Retrieving Information for {table}.")
    return db.query(prod_table).order_by(prod_table.datetime.desc())\
        .filter(prod_table.datetime >= start, prod_table.datetime <= end).all()
