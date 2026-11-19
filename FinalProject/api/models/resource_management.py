from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base


class ResourceManagement(Base):
    __tablename__ = "resource_management"

    resource_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    resource_name = Column(String(100), nullable=False)
    resource_amount = Column(DECIMAL(10, 2), nullable=False)
    resource_unit = Column(String(20), nullable=False)