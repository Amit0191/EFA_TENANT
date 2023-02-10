import responses
from pydantic_classes import EFAResponse
from flask import Response
import json

@responses.activate
def mock_efa_response():
    response = responses.add(
        responses.GET,
        url='http://gotenant-service:8083/v1/tenant/tenant',
        json={
                "id": 1,
                "name": "Tenant-A",
                "description": "Tenant-A's Description",
                "num_of_vrf": 20,
        },
        status=200)
    return response





def mock_response_get_tenants():
    tenants= {
    "id": 1,
    "name": "Tenant-A",
    "description": "Tenant-A's Description",
    "num_of_vrf": 20,
    }
    response = Response(response=tenants, status=200, mimetype='application/json')

    response_status = response._status
    response_dict = response.response
    return response_dict






def get_efa_response():

    response = mock_efa_response()
    return json.loads(response.body)



def get_efa_response_pydantic():
    response = mock_efa_response()
    json_data = json.loads(response.body)
    efa_response = EFAResponse(**json_data)
    return efa_response
