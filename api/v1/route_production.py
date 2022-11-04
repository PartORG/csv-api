"""
File has all created routes for a Production endpoint.
Here can be added more routes for Production endpoint.
For example some calculations of retrieved data - min or max MW produced in period.
"""

import logging

from typing import List, Optional
from fastapi import Depends, APIRouter, HTTPException, Query
from sqlalchemy.orm import Session
from db.cruds import crud_production
from schemas import production_schemas
from db.local_session import get_db

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    datefmt="%m-%d %H:%M",
    handlers=[logging.FileHandler("production_api.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

router = APIRouter()


# endpoint function to return all data from Production tables
@router.get("/all/", response_model=List[production_schemas.Production])
def get_all_information(park_name: str = Query(description="Provide Park Name here", example="Bemmel"),
                        db: Session = Depends(get_db)):

    logger.info(f"Retrieving all production data.")
    all_info = crud_production.get_all_prods(db, park_name)

    if all_info is None:
        logger.warning(f"No data found.")
        raise HTTPException(status_code=404, detail="Information not found.")

    logger.info(f"Successfully retrieved all information.")
    return all_info


# endpoint function to return data for provided period
@router.get("/period/", response_model=List[production_schemas.Production])
def get_all_information(park_name: str = Query(description="Provide Park Name here", example="Bemmel"),
                        start_date: Optional[str] = Query(None, description="Provide date of a start for period",
                                                          example="YYYY-MM-DD HH:MM:SS"),
                        end_date: Optional[str] = Query(None, description="Provide date of an end for period",
                                                        example="YYYY-MM-DD HH:MM:SS"),
                        db: Session = Depends(get_db)):
    all_prods = None

    # list of different conditions for period parameters
    if start_date and end_date:
        logger.info(f"Retrieving all production data.")
        all_prods = crud_production.get_prod_period(start_date, end_date, db, park_name)

    if start_date and not end_date:
        logger.info(f"Retrieving all production data.")
        all_prods = crud_production.get_prod_period_only_start(start_date, db, park_name)

    if not start_date and end_date:
        logger.info(f"Retrieving all production data.")
        all_prods = crud_production.get_prod_period_only_end(end_date, db, park_name)

    if not start_date and not end_date:
        logger.info(f"Retrieving all production data.")
        all_prods = crud_production.get_prod_period_empty(db, park_name)

    if all_prods is None or all_prods == []:
        logger.warning(f"No data found.")
        raise HTTPException(status_code=404, detail="Information not found.")

    logger.info(f"Successfully retrieved all information.")
    return all_prods
