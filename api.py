'''
    A module specified by connexion to implement endpoints according to OpenApi3 specs. 
        Functions:
            create_tenant():
                Deals with the endpoint /create_tenant. Takes as an argument Tenant dictionary and returns a successful response if Tenant is created.
                    Parameters:
                            tenant (Dict): Dict of Tenant fields like name, num_of_vrf, description, etc.

                    Returns:
                            (Response): A successful response if tenant is created successfully.

            get_tenants():
                Deals with the endpoint /tenants. Returns a list of all Tenants available.
                    Parameters:
                            tenant (Dict): Dict of Tenant fields like name, num_of_vrf, description, etc.

                    Returns:
                            (Response): A successful response if tenant is created successfully.

            get_tenant(name):
                Deals with the endpoint /tenant/name. Returns a Tenant with tenant name = name.
                    Parameters:
                            name (str): String reflecting Tenant Name to be returned.

                    Returns:
                            (Response): Requested Tenant is returned if name matches If not, a 'Tenant Name doesnt exist is returned'.
'''

from mock import get_all_tenants, get_tenant_by_name
from validations import validate, validate_all, validate_create
from operations import add_vrf

from typing import List, Dict


def index() -> str:
    
    return 'Hello'


def create_tenant(tenant: dict) -> str:

    add_vrf = add_vrf(tenant, 50)
    val = validate_create(tenant)
    return val


def get_tenants() -> List:
    
    response = get_all_tenants()
    val = validate_all(response)
    print(type(val))
    return val


def get_tenant(name: str) -> Dict:
    
    response = get_tenant_by_name(name)
    val = validate(response)
    print(type(val))
    return val
