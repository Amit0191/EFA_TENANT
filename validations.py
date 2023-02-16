from pydantic import ValidationError
import json

from pydantic_classes import EFABody


def validate(response):
    if response.status_code == 201:
        try:
            print('I am in')
            efaBody = EFABody(**response.response)
            return json.loads(efaBody.json())
        except ValidationError as e:
            return json.loads(e.json())
    else:
        return response.response[0].decode('UTF-8')


