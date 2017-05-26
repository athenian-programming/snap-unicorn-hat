import json
import logging
import os.path
from threading import Lock

import cli_args  as cli
import requests
import unicornhat as unicorn
from cli_args import LOG_LEVEL
from cli_args import setup_cli_args
from flask import Flask
from flask import make_response
from flask import request
from utils import setup_logging

logger = logging.getLogger(__name__)

CACHE_DIR = "/tmp/js_cache"
page_cache = {}
cache_lock = Lock()
file_lock = Lock()


def fetch_file(filename):
    fqn = "{0}/{1}".format(CACHE_DIR, filename)
    if os.path.isfile(fqn):
        with open(fqn, 'r') as f:
            try:
                logger.info("Reading %s", fqn)
                return json.load(f)
            except ValueError:
                logger.error("Error reading %s", fqn)
                pass

    url = "http://snap.berkeley.edu/snapsource/{0}".format(filename)
    logger.info("Requesting %s", url)
    request = requests.get(url, stream=False)
    text = request.text
    type = request.headers["Content-Type"]
    cache = request.headers["Cache-Control"] if "Cache-Control" in request.headers.keys() else None
    val = {"text": text, "type": type, "cache": cache}

    with file_lock, open(fqn, 'w') as f:
        json.dump(val, f)
    return val


def response(val):
    resp = make_response(val, 200)
    resp.headers["Content-Type"] = "text/plain"
    return resp


if __name__ == "__main__":
    args = setup_cli_args(cli.verbose)

    setup_logging(level=args[LOG_LEVEL])

    if not os.path.exists(CACHE_DIR):
        os.mkdir(CACHE_DIR)

    flask = Flask(__name__)


    @flask.route("/snapsource/<string:filename>")
    def snapsource(filename):
        if not filename in page_cache:

            contents = fetch_file(filename)
            with cache_lock:
                if not filename in page_cache:
                    page_cache[filename] = contents

        resp = make_response(page_cache[filename]["text"], 200)

        resp.headers["Content-Type"] = page_cache[filename]["type"]
        if page_cache[filename]["cache"]:
            resp.headers["Cache-Control"] = page_cache[filename]["cache"]
        resp.headers["Access-Control-Allow-Origin"] = "*"
        resp.headers["Access-Control-Allow-Methods"] = "GET"
        return resp


    @flask.route("/unicorn/clear")
    def clear():
        unicorn.clear()
        return ""


    @flask.route("/unicorn/x")
    def x():
        return response(unicorn.get_shape()[0])


    @flask.route("/unicorn/y")
    def y():
        return response(unicorn.get_shape()[1])


    @flask.route("/unicorn/set_all")
    def set_all():
        r = request.args.get("r")
        g = request.args.get("g")
        b = request.args.get("b")
        unicorn.set_all(r=r, g=g, b=b)
        return ""


    @flask.route("/unicorn/set_pixel")
    def set_pixel():
        x = request.args.get("x")
        y = request.args.get("y")
        r = request.args.get("r")
        g = request.args.get("g")
        b = request.args.get("b")
        unicorn.set_pixel(x=x, y=y, r=r, g=g, b=b)
        return ""


    @flask.route("/unicorn/get_pixel")
    def get_pixel():
        x = request.args.get("x")
        y = request.args.get("y")
        return response(unicorn.get_pixel(x, y))


    @flask.route("/unicorn/brightness/<float:brightness>")
    def brigtness(brightness):
        unicorn.brightness(brightness)
        return ""


    flask.run(host="0.0.0.0", port=9001, threaded=True)
