from pydantic import BaseModel


class GetRequest(BaseModel):
    name: str
    id: int


class EFABody(BaseModel):
    id: int
    name: str
    description: str
    num_of_vrf: int



