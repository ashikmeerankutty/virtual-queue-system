from flask import jsonify, request
from functools import wraps
from config import Config



def accessManager(*roles):
    def wrapper_f(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                token = request.headers.get('Authorization')
                if token is None:
                    raise Exception('Token not found')
                if(token != Config.TOKEN):
                    raise Exception('Not authorized')
                return func(*args, **kwargs)
            except Exception as e:
                return jsonify({"status": str(e)}), 403
        return wrapper
    return wrapper_f
