from sqlalchemy import Column, Integer, String, DECIMAL, DATE
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    promotion_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotion_code = Column(String(50))
    expiration_date = Column(DATE)
    discount_amount = Column(DECIMAL(10, 2))
    discount_type = Column(String(20))  # "Percentage" or "Dollar_Amount"

    orders = relationship("Order", back_populates="promotion")