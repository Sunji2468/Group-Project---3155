from sqlalchemy import Column, ForeignKey, Integer, String, DATE, CheckConstraint
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = (
        CheckConstraint("review_rating BETWEEN 1 AND 5", name="ck_reviews_rating_range"),
    )

    review_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    review_text = Column(String(500))
    review_rating = Column(Integer)
    review_date = Column(DATE)

    customer = relationship("Customer", back_populates="reviews")