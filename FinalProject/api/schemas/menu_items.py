from typing import Optional
from pydantic import BaseModel


class MenuItemBase(BaseModel):
    item_name: str
    item_ingredients: Optional[str] = None
    item_price: float
    item_calories: Optional[int] = None
    item_category: Optional[str] = None


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    item_name: Optional[str] = None
    item_ingredients: Optional[str] = None
    item_price: Optional[float] = None
    item_calories: Optional[int] = None
    item_category: Optional[str] = None


class MenuItem(MenuItemBase):
    menu_id: int
