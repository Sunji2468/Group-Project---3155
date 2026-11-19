from typing import Optional
from pydantic import BaseModel


class ResourceManagementBase(BaseModel):
    resource_name: str
    resource_amount: float
    resource_unit: str


class ResourceManagementCreate(ResourceManagementBase):
    pass


class ResourceManagementUpdate(BaseModel):
    resource_name: Optional[str] = None
    resource_amount: Optional[float] = None
    resource_unit: Optional[str] = None


class ResourceManagement(ResourceManagementBase):
    resource_id: int