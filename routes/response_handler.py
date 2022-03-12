from json import dumps
from app import app

def response(data, httpCode):
    json = dumps(data, default = lambda o:o.__dict__ if hasattr(o, '__dict__') else str(o), indent = 1)
    response = app.response_class(
        response = json,
        status = httpCode,
        mimetype = 'application/json'
        )
    print(json)
    return response