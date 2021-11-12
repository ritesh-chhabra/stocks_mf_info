from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ShowStock(BaseModel):
    name: str
    price: float
    time: str
    # time: Optional[str] = str(datetime.now())