from typing import Optional
from pydantic import BaseModel, model_validator
from .menu_items import MenuItem


class OrderDetailBase(BaseModel):
    order_quantity: int
    item_price: float


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    menu_id: int
    order_subtotal: Optional[float] = None

    # order_subtotal = item_price * order_quantity
    @model_validator(mode="after") # pydantic validator
    def compute_subtotal(self):
        self.order_subtotal = round(self.item_price * self.order_quantity, 2)
        return self


class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    menu_id: Optional[int] = None
    order_quantity: Optional[int] = None
    item_price: Optional[float] = None


class OrderDetail(OrderDetailBase):
    order_detail_id: int
    order_id: int
    order_subtotal: float
    menu_item: MenuItem = None
