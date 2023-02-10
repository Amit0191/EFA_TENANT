from flask import render_template
from efa_response import mock_response_get_tenants


def index():
    
    return mock_response_get_tenants()
    # return render_template('index.html')


def create_tenant():
    
    return render_template('create_tenant.html')


def get_tenant():
    return mock_response_get_tenants()
    # return render_template('get_tenant.html')
