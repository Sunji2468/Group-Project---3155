from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    order_detail_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    menu_id = Column(Integer, ForeignKey("menu_items.menu_id"))
    order_quantity = Column(Integer, nullable=False)
    item_price = Column(DECIMAL(10, 2), nullable=False)
    order_subtotal = Column(DECIMAL(10, 2), nullable=False)  # item_price * order_quantity

    order = relationship("Order", back_populates="order_details")
    menu_item = relationship("MenuItem", back_populates="order_details")