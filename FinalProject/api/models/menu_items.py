from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    menu_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item_name = Column(String(100), nullable=False)
    item_ingredients = Column(String(500))
    item_price = Column(DECIMAL(10, 2), nullable=False)
    item_calories = Column(Integer)
    item_category = Column(String(50))

    order_details = relationship("OrderDetail", back_populates="menu_item")