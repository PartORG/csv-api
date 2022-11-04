"""
File with all the tables connected with Information retrieval.
For now there is only table with Information data.
But this folder can be populated with new database Tables.
"""
from pydantic import BaseModel


class Information(BaseModel):
    """
    Basic Model for Park Information Table. Usually used as a return model for API data.
    """
    park_name: str
    timezone: str
    energy_type: str

    # this part converts any object to an ORM model
    class Config:
        orm_mode = True

