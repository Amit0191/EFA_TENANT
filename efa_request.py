from pydantic_classes import GetRequest


URL = f'http://gotenant-service:8083/v1/tenant/tenant'



model = GetRequest(name = 'Tenant-A', id = '1A')


def request_url_with_query_parameters(model: GetRequest):
    model_dict = model.dict()
    query = '&'.join(f'{k}={v}' for k,v in model_dict.items())
    return f'{URL}?{query}'

print(request_url_with_query_parameters(model))

# Can also do 
# data = model.json()
# response = requests.post(url, json=data)