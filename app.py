from flask import request
import connexion


app = connexion.App(__name__, specification_dir='oapi/')
app.add_api('efa_tenant2.yaml')


if __name__ == '__main__':
    app.run(port=8080)
