from pydantic import BaseModel
from typing import Any


class BaseExecute(BaseModel):
    success: bool = True
    message: str = "Success"
    data: Any | None = None
