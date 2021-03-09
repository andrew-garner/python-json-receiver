#!/usr/bin/env python3

import logging

from flask import Flask, json, request


app = Flask(__name__)
hello_world = [{"hello": "world"}]
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)


@app.route('/', methods=['GET'])
def get_hello_world():
    app.logger.debug(f"{request.remote_addr} {request.method} {request.path}")
    return json.dumps(hello_world)


@app.route('/', methods=['POST'])
def post_log_request_body():
    app.logger.debug(f"{request.remote_addr} {request.method} {request.path}")
    if request.is_json:
        app.logger.debug(f"Received JSON: {json.dumps(request.get_json())}")
        return json.dumps({request.get_json()})
    
    app.logger.debug(f"Received data: {request.values}")
    return json.dumps({"request":"POST"})


if __name__ == '__main__':
    app.run()
