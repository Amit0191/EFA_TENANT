from pydantic import BaseModel, validator


class GetRequest(BaseModel):
    name: str = None
    id: int = None

    @validator('name', pre=True)
    @validator('name', pre=True)
    def name_or_id(get_request, v, values) :
        if v is None and values.get('name') is None and values.get('id') is None:
            raise ValueError('Please Provide name or id')
        return v
    
        