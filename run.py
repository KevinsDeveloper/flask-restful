#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, jsonify, request, Response, request, flash, redirect, url_for
from app import app

app = app('development')

@app.errorhandler(404)
def error_404(error):
    response = dict(ret = 404, msg = "Not Found")
    return jsonify(response), 404

# @app.errorhandler(Exception)
# def error_500(error):
#     response = dict(ret = 500, msg = "Server Error")
#     return jsonify(response), 500

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 8000, debug = True)
