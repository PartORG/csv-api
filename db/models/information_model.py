from sqlalchemy import Column, Integer, String
from db.local_session import Base


class ParkInfo(Base):
    """
    Basic class that represents a Table structure from database that presents Information about parks.
    """
    __tablename__ = "park_info"

    id = Column(Integer, primary_key=True, index=True)
    park_name = Column(String, nullable=False)
    timezone = Column(String, nullable=False)
    energy_type = Column(String, nullable=False)

