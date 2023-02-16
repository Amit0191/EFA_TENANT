from connexion import NoContent
from mock import get_all_tenants, get_tenant_by_name
from validations import validate

# from mock_responses import mock_response_get_tenants


def index():
    
    return 'Hello'


def create_tenant(tenant):

    return 'Successfully added Tenant', 201


def get_tenants():

    return 'Hello Get Tenant'


def get_tenant(name):
    
    response = get_tenant_by_name(name)
    val = validate(response)
    return val
