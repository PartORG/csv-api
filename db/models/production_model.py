"""
File with all the tables with Production data.
"""

from sqlalchemy import Column, Integer, String, Float
from db.local_session import Base


class Defaul(Base):
    """
    Basic Class to be inherited from, as all Production tables use the same set of column names.
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(String, nullable=False)
    MW = Column(Float, nullable=False)


class Bemmel(Defaul):
    __tablename__ = "Bemmel"


class Netterden(Defaul):
    __tablename__ = "Netterden"


class Stadskanaal(Defaul):
    __tablename__ = "Stadskanaal"


class Windskanaal(Defaul):
    __tablename__ = "Windskanaal"


class Zwartenbergseweg(Defaul):
    __tablename__ = "Zwartenbergseweg"


# TODO: used __abstract__ for a main class and different __tablename__ for each child.