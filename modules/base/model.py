from typing import Optional, Any
from pydantic import BaseModel, Field


class RepositoryResultModel(BaseModel):
    data: Optional[Any] = Field(default=None)
