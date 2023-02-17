'''
    A module to validate Mock responses by using Pydantic library. 
        Functions:
            validate(Response):
                Validates Responses based on Pydantic class EFABody. 
                    Parameters:
                            response (Response): Takes in Mock Response as parameter.

                    Returns:
                            (Response): If validated successfuly, a json response is returned containing a Tenant.

            validate_all():
                Validates Responses(List of Tenants) based on Pydantic class EFAList. 
                    Parameters:
                            tenant (Dict): Dict of Tenant fields like name, num_of_vrf, description, etc.

                    Returns:
                            (Response): If validated successfuly, a json response is returned containing all tenants.

            validate_create(name):
                Accepts a request and validates it against EFABody.
                    Parameters:
                            request (Request): String reflecting Tenant Name to be returned.

                    Returns:
                            (Response): Response tenant created successfully is returned if succeded.
'''


from pydantic import ValidationError
from typing import List, Dict
import json

from pydantic_classes import EFABody, EFAList


def validate(response) -> Dict:
    if response.status_code == 201:
        try:
            efa_body = EFABody(**response.response)
            return json.loads(efa_body.json())
        except ValidationError as e:
            return json.loads(e.json())
    else:
        return response.response[0].decode('UTF-8')


def validate_all(response) -> List:
    if response.status_code == 200:
        try:
            efa_list = EFAList(__root__= response.response)
            return json.loads(efa_list.json())
        except ValidationError as e:
            return json.loads(e.json())
    else:
        return response.response[0].decode('UTF-8')
    

def validate_create(request, num: int) -> str:

    try:
        efa_body = EFABody(**request)
        efa_body.num_of_vrf = efa_body.num_of_vrf - num
        return f'Scuccesfully created Tenant with Tenant name {efa_body.name}, {efa_body.num_of_vrf}'
    except ValidationError as e:
        return json.loads(e.json())

