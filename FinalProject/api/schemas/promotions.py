from datetime import date
from typing import Optional, Literal
from pydantic import BaseModel


class PromotionBase(BaseModel):
    promotion_code: Optional[str] = None
    expiration_date: Optional[date] = None
    discount_amount: Optional[float] = None
    discount_type: Optional[Literal["Percentage", "Dollar_Amount"]] = None


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    promotion_code: Optional[str] = None
    expiration_date: Optional[date] = None
    discount_amount: Optional[float] = None
    discount_type: Optional[Literal["Percentage", "Dollar_Amount"]] = None


class Promotion(PromotionBase):
    promotion_id: int
