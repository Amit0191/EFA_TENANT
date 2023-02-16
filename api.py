from connexion import NoContent
from mock import get_all_tenants, get_tenant_by_name
from validations import validate, validate_all


def index():
    
    return 'Hello'


def create_tenant(tenant):
    # id = tenant.get('id')
    return 'Successfully added Tenant', 201


def get_tenants():
    response = get_all_tenants()
    val = validate_all(response)
    return val


def get_tenant(name):
    
    response = get_tenant_by_name(name)
    val = validate(response)
    return val
