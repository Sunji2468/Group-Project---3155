from datetime import date
from typing import Optional, Literal
from pydantic import BaseModel
from .order_details import OrderDetail


class OrderBase(BaseModel):
    customer_id: Optional[int] = None
    order_tracking_number: int
    order_status: Literal["ordered", "preparing", "finished"]
    order_type: Literal["pickup", "delivery"]
    order_price: float
    promotion_id: Optional[int] = None
    card_number: Optional[str] = None  # last 4 digits only
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None


class OrderCreate(OrderBase):
    order_date: Optional[date] = None


class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    order_date: Optional[date] = None
    order_tracking_number: Optional[int] = None
    order_status: Optional[Literal["ordered", "preparing", "finished"]] = None
    order_type: Optional[Literal["pickup", "delivery"]] = None
    order_price: Optional[float] = None
    promotion_id: Optional[int] = None
    card_number: Optional[str] = None
    transaction_status: Optional[str] = None
    payment_type: Optional[str] = None


class Order(OrderBase):
    order_id: int
    order_date: Optional[date] = None
    order_details: list[OrderDetail] = None
