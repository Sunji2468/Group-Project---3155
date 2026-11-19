from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    order_date = Column(DATE, nullable=False, default=date.today)
    order_tracking_number = Column(Integer, unique=True, nullable=False)
    order_status = Column(String(50), nullable=False)  # ordered, preparing, finished
    order_type = Column(String(20), nullable=False)    # pickup, delivery
    order_price = Column(DECIMAL(10, 2), nullable=False)
    promotion_id = Column(Integer, ForeignKey("promotions.promotion_id"), nullable=True)
    card_number = Column(String(4))  # last 4 digits only
    transaction_status = Column(String(50))
    payment_type = Column(String(50))

    customer = relationship("Customer", back_populates="orders")
    promotion = relationship("Promotion", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")