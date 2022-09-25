from typing import Union
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: Union[str, None] = None
