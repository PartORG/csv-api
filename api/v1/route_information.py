"""
File has all created routes for an Information endpoint.
Here can be added more routes for Information endpoint..
"""

import logging

from typing import List, Optional
from fastapi import Depends, APIRouter, HTTPException, Query
from sqlalchemy.orm import Session
from db.cruds import crud_information
from schemas import information_schemas
from db.local_session import get_db

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    datefmt="%m-%d %H:%M",
    handlers=[logging.FileHandler("information_api.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

router = APIRouter()


# endpoint function to retrieve data from Information table
@router.get("/", response_model=List[information_schemas.Information])
def get_all_information(park: Optional[str] = Query(None, description="Provide Park Name here", example="Bemmel"),
                        timezone: Optional[str] = Query(None,
                                                description="Provide Timezone of an interesting set of parks here",
                                                example="Europe/Amsterdam"),
                        energy_type: Optional[str] = Query(None,
                                               description="Provide energy type to provide information for",
                                               example="Solar or Wind"),
                        db: Session = Depends(get_db)):
    all_info = None

    # set of different conditions for data filtering
    if park and not timezone and not energy_type:
        logger.info(f"Retrieving all information data.")
        all_info = crud_information.get_info_by_park(db, park)

    if not park and timezone and not energy_type:
        logger.info(f"Retrieving all information data.")
        all_info = crud_information.get_info_by_timezone(db, timezone)

    if not park and not timezone and energy_type:
        logger.info(f"Retrieving all information data.")
        all_info = crud_information.get_info_by_energy_type(db, energy_type)

    if park and timezone and not energy_type:
        logger.info(f"Retrieving all information data.")
        all_info = crud_information.get_info_by_park_and_timezone(db, park, timezone)

    if park and not timezone and energy_type:
        logger.info(f"Retrieving all information data.")
        all_info = crud_information.get_info_by_park_and_energy_type(db, park, energy_type)

    if not park and timezone and energy_type:
        logger.info(f"Retrieving all information data.")
        all_info = crud_information.get_info_by_timezone_and_energy_type(db, timezone, energy_type)

    if not park and not timezone and not energy_type:
        logger.info(f"Retrieving all information data.")
        all_info = crud_information.get_all_info(db)

    all_info = all_info if isinstance(all_info, list) else [all_info]

    if all_info is None or all_info == []:
        logger.warning(f"No data found.")
        raise HTTPException(status_code=404, detail="Information not found.")

    logger.info(f"Successfully retrieved all information.")
    logger.info(all_info)
    return all_info
