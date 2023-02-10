from pydantic import BaseModel

class PostRequest(BaseModel):
    method: str
    url: str
    headers: dict
    body: dict

class GetRequest(BaseModel):
    name: str
    id: int


class EFAResponse(BaseModel):
    id: int
    name: str
    description: str
    num_of_vrf: int
    


