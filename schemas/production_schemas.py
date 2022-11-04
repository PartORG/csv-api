from pydantic import BaseModel


class Production(BaseModel):
    """
    Basic Model for Production data Table. Usually used as a return model for API data.
    """
    datetime: str
    MW: float

    # this part converts any object to an ORM model
    class Config:
        orm_mode = True
