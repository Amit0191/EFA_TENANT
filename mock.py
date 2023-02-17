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
    '''
    Returns a mock response containing a list of Tenants.

            Parameters:
                    None

            Returns:
                    (Response): A mock response containing all the Tenants available to us.
    '''
    return Response(response=TENANTS, status=200, mimetype='application/json')


def get_tenant_by_name(name: str):    
    '''
    Returns a mock response with a Tenant Name defined in the parameter name. If name doesn't match, returns 400 Response.

            Parameters:
                    name (str): Tenant name to be fetched.

            Returns:
                    (Response): A mock response containing Tenant with name specified.
    '''
    
    tenant = next((item for item in TENANTS if item["name"] == name), None)
    if tenant != None:
        return Response(response=tenant, status=201, mimetype= 'application/json')
    else:
        response_400 = f'{name} does not exist.'
        return Response(response=response_400, status=400)



