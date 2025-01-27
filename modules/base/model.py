from typing import Optional, Any
from pydantic import BaseModel, Field


class RepositoryResultModel(BaseModel):
    data: Optional[Any] = Field(default=None)


class ServiceResultModel(BaseModel):
    success: bool = Field(default=False)
    data: Optional[Any] = Field(default=None)
    message: Optional[str] = Field(default="Success")
    error_msg: Optional[str] = Field(default="Something went wrong. Please try again.")
