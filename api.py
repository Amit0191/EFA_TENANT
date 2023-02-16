from connexion import NoContent
from mock import get_all_tenants, get_tenant_by_name
from validations import validate

# from mock_responses import mock_response_get_tenants


def index():
    
    return 'Hello'
    # return mock_response_get_tenants()



def create_tenant(tenant):
    # id = tenant.get('id')
    # Pass the tenant object to Pydantic for validation.

    return 'Successfully added Tenant', 201


def get_tenants():

    return 'Hello Get Tenant'

    # return mock_response_get_tenants()


def get_tenant(name):
    
    response = get_tenant_by_name(name)
    val = validate(response)
    return val
    # if name in TENANTS:
    #     return TENANTS[name]
    # else:
    #     NoContent, 404