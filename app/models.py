from sqlalchemy import Column, Integer, String

from .database import Base


class DataIntegration(Base):
    __tablename__ = "data_integration"

    id = Column(Integer, primary_key=True, index=True)
    id_board = Column(String, nullable=True)
    id_list = Column(String, nullable=True)
    list_labels = Column(String, nullable=True)
    list_users = Column(String, nullable=True)
