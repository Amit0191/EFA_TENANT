from flask import Response



# Mock response body data.
TENANTS= [{
"id": '1',
"name": "tenant-a",
"description": "Tenant-A's Description",
"num_of_vrf": 20
},
{
"id": 2,
"name": "tenant-b",
"description": "Tenant-B's Description",
"num_of_vrf": 30
},
{
"id": 3,
"name": "tenant-c",
"description": "Tenant-C's Description",
"num_of_vrf": 40
}]


def get_all_tenants():
    return Response(response=TENANTS, status=200, mimetype='application/json')


def get_tenant_by_name(name):
    tenant = next((item for item in TENANTS if item["name"] == name), None)
    if tenant != None:
        return Response(response=tenant, status=201, mimetype= 'application/json')
    else:
        response_400 = f'{name} does not exist.'
        return Response(response=response_400, status=400)


def create_tenant(tenant_name):
    response_201 = f'Successfully created {tenant_name}.' 
    return Response(response=response_201, status=201)


def pydantic_error_response():
    response_400 = 'Field_Name is not valid.'
    return Response(response=response_400, status=400)

