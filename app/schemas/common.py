from typing import Optional
from pydantic import BaseModel



class PageInfo(BaseModel):
  limit: int
  next: Optional[int] = None
  previous: Optional[int] = None

