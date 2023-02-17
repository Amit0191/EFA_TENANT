from typing import Dict


def add_vrf(tenant: Dict, num: int):
    tenant['num_of_vrf'] = tenant['num_of_vrf'] + num
    return tenant

def remove_vrf(tenant: str, num: int):
    pass

