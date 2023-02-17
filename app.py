from flask import request
import connexion




PASSWD = {"admin": "secret", "foo": "bar"}

def basic_auth(username, password):
    if PASSWD.get(username) == password:
        return {"sub": username}
    # optional: raise exception for custom error response
    return None


app = connexion.App(__name__, specification_dir='oapi/')
app.add_api('efa_tenant.yaml')


if __name__ == '__main__':
    app.run(port=8080)
