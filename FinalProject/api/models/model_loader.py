from . import (
    customers,
    promotions,
    orders,
    menu_items,
    order_details,
    reviews,
    resource_management,
)

from ..dependencies.database import engine


def index():
    customers.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
    resource_management.Base.metadata.create_all(engine)