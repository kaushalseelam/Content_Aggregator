from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import  BaseModel
from enum import Enum


class link_(BaseModel):
    name:str
    url:str

