from pydantic import BaseModel
from typing import List


class GetRequest(BaseModel):
    name: str
    id: int


class EFABody(BaseModel):
    id: int
    name: str
    description: str
    num_of_vrf: int


class EFAList(BaseModel):
    __root__: List[EFABody]

