#!/usr/bin/env python3

import logging
import pprint

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
    app.logger.debug(f"Content length: {request.content_length}")
    app.logger.debug(f"Content type: {request.content_type}")
    app.logger.debug(f"All headers: {request.headers}")
    data = request.get_data()
    app.logger.debug(f"Request Data: {pprint.pprint(data)}")
    
    if request.is_json:
        app.logger.debug(f"Received JSON: {pprint.pprint(json.dumps(request.get_json()))}")
        return json.dumps({request.get_json()})
    
    json_data = request.get_json(force=True, silent=True, cache=True)
    app.logger.debug(f"Received JSON: {pprint.pprint(json.dumps(json_data))}")
    
    return json.dumps({"request":"POST"})


if __name__ == '__main__':
    app.run()
