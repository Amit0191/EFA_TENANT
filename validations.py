from pydantic import ValidationError
import json

from pydantic_classes import EFABody, EFAList


def validate(response):
    if response.status_code == 201:
        try:
            efa_body = EFABody(**response.response)
            return json.loads(efa_body.json())
        except ValidationError as e:
            return json.loads(e.json())
    else:
        return response.response[0].decode('UTF-8')


def validate_all(response):
    if response.status_code == 200:
        try:
            efa_list = EFAList(__root__= response.response)
            return json.loads(efa_list.json())
        except ValidationError as e:
            return json.loads(e.json())
    else:
        return response.response[0].decode('UTF-8')