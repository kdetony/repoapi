"""
Programa flask que implementa el endpoint devops.
"""

import ssl
from functools import wraps

from flask import Flask, request, abort


app = Flask(__name__)
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('server.crt', 'server.key')


# The actual decorator function
def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        with open('api.key', 'r') as apikey:
            key = apikey.read().replace('\n', '')
        if request.headers.has_key('x-api-key') and request.headers['x-api-key'] == key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function


@app.route('/devops/', methods=['POST'])
#@require_appkey
def put_user():
    return {"message": "Hello Juan Perez your message will be send"}


@app.route('/')
def hello_world():
    return 'Hola Mundo Prueba'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, debug=True, ssl_context=context)

