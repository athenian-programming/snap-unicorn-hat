#!/usr/bin/env python

import argparse
import logging
import sys

import unicornhat as unicorn
from flask import Flask
from flask import make_response
from flask import request

LOG_LEVEL = "loglevel"

logger = logging.getLogger(__name__)
x_cache = None
y_cache = None

flask = Flask(__name__)


@flask.route("/clear")
def clear():
    unicorn.clear()
    return response()


@flask.route("/show")
def show():
    unicorn.show()
    return response()


@flask.route("/x")
def x():
    global x_cache
    if not x_cache:
        x_cache = unicorn.get_shape()[0]
    return response(x_cache)


@flask.route("/y")
def y():
    global y_cache
    if not y_cache:
        y_cache = unicorn.get_shape()[1]
    return response(y_cache)


@flask.route("/set_all")
def set_all():
    r = request.args.get("r")
    g = request.args.get("g")
    b = request.args.get("b")
    unicorn.set_all(r=int(r), g=int(g), b=int(b))
    return response()


@flask.route("/set_all_rgb/<string:rgb>")
def set_all_rgb(rgb):
    s = rgb.split("-")
    unicorn.set_all(r=int(s[0]), g=int(s[1]), b=int(s[2]))
    return response()


@flask.route("/set_pixel")
def set_pixel():
    x = request.args.get("x")
    y = request.args.get("y")
    r = request.args.get("r")
    g = request.args.get("g")
    b = request.args.get("b")
    unicorn.set_pixel(x=int(x), y=int(y), r=int(r), g=int(g), b=int(b))
    return response()


@flask.route("/set_pixel_rgb/<string:rgb>")
def set_pixel_rgb(rgb):
    x = request.args.get("x")
    y = request.args.get("y")
    s = rgb.split("-")
    unicorn.set_pixel(x=int(x), y=int(y), r=int(s[0]), g=int(s[1]), b=int(s[2]))
    return response()


@flask.route("/get_pixel")
def get_pixel():
    x = request.args.get("x")
    y = request.args.get("y")
    val = str(unicorn.get_pixel(x=int(x), y=int(y)))[1:-1]
    return response(val)


@flask.route("/rotation/<int:rotation>")
def rotation(rotation):
    unicorn.rotation(rotation)
    return response()


@flask.route("/brightness/<float:brightness>")
def brigtness(brightness):
    unicorn.brightness(brightness)
    return response("")


@flask.route("/get_brightness")
def get_brightness():
    return response(unicorn.get_brightness())


def response(val=""):
    resp = make_response(str(val), 200)
    resp.headers["Content-Type"] = "text/plain"
    resp.headers["Access-Control-Allow-Origin"] = "http://snap.berkeley.edu"
    resp.headers["Access-Control-Allow-Methods"] = "GET, POST"
    return resp


def setup_logging(filename=None,
                  filemode="a",
                  stream=sys.stderr,
                  level=logging.INFO,
                  format="%(asctime)s %(name)-10s %(funcName)-10s():%(lineno)i: %(levelname)-6s %(message)s"):
    if filename:
        logging.basicConfig(filename=filename, filemode=filemode, level=level, format=format)
    else:
        logging.basicConfig(stream=stream, level=level, format=format)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", dest=LOG_LEVEL, default=logging.INFO, action="store_const",
                        const=logging.DEBUG, help="Enable debugging info")
    args = vars(parser.parse_args())

    setup_logging(level=args[LOG_LEVEL])

    flask.run(host="0.0.0.0", port=9000)
