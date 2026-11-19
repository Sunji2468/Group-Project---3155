from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class ReviewBase(BaseModel):
    customer_id: int
    review_text: Optional[str] = None
    review_rating: int = Field(ge=1, le=5)
    review_date: Optional[date] = None


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    customer_id: Optional[int] = None
    review_text: Optional[str] = None
    review_rating: Optional[int] = Field(default=None, ge=1, le=5)
    review_date: Optional[date] = None


class Review(ReviewBase):
    review_id: int
