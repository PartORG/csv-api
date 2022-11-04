"""
FIle with set of CRUD (Create, Read, Update and Delete) operations connected with Information data Tables.
Can be easily added new functions for new endpoint set for Information data Tables.
"""

import logging

from sqlalchemy.orm import Session

from ..models.information_model import ParkInfo


logger = logging.getLogger(__name__)


def get_info_by_park(db: Session, park: str):
    """
    Return set of information filtered by park name.
    :param db:
    :param park:
    :return: List of information data
    """
    logger.debug(f"Retrieving Information for Park.")
    return db.query(ParkInfo).filter(ParkInfo.park_name == park).all()


def get_info_by_timezone(db: Session, timezone: str):
    """
    Return set of information filtered by timezone.
    :param db:
    :param timezone:
    :return: List of information data
    """
    logger.debug(f"Retrieving Information for Park.")
    return db.query(ParkInfo).filter(ParkInfo.timezone == timezone).all()


def get_info_by_energy_type(db: Session, energy_type: str):
    """
    Return set of information filtered by energy type.
    :param db:
    :param energy_type:
    :return: List of information data
    """
    logger.debug(f"Retrieving Information for Park.")
    return db.query(ParkInfo).filter(ParkInfo.energy_type == energy_type).all()


def get_info_by_park_and_timezone(db: Session, park: str, timezone: str):
    """
    Return set of information filtered by park name and timezone.
    :param db:
    :param park:
    :param timezone:
    :return: List of information data
    """
    logger.debug(f"Retrieving Information for Park.")
    return db.query(ParkInfo).filter(ParkInfo.park_name == park, ParkInfo.timezone == timezone).all()


def get_info_by_park_and_energy_type(db: Session, park: str, energy_type: str):
    """
    Return set of information filtered by park name and energy type.
    :param db:
    :param park:
    :param energy_type:
    :return: List of Information data.
    """
    logger.debug(f"Retrieving Information for Park.")
    return db.query(ParkInfo).filter(ParkInfo.park_name == park, ParkInfo.energy_type == energy_type).all()


def get_info_by_timezone_and_energy_type(db: Session, timezone: str, energy_type: str):
    """
    Return set of information filtered by timezone and energy type.
    :param db:
    :param timezone:
    :param energy_type:
    :return: List of Information data.
    """
    logger.debug(f"Retrieving Information for Park.")
    return db.query(ParkInfo).filter(ParkInfo.timezone == timezone, ParkInfo.energy_type == energy_type).all()


def get_all_info(db: Session):
    """
    Return all of information data from park_info table.
    :param db:
    :return: List of Information data.
    """
    logger.debug(f"Retrieving Information for Park.")
    return db.query(ParkInfo).all()

