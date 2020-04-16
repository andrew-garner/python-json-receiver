#!/usr/bin/env python3

from flask import Flask, json, request

hello_world = [{"hello": "world"}]

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_hello_world():
    return json.dumps(hello_world)


@app.route('/', methods=['POST'])
def post_log_request_body():
    if request.is_json:
        return json.dumps(request.get_json())


if __name__ == '__main__':
    app.run()
