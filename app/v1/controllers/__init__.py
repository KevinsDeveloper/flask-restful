# -*- coding:utf-8 -*-
import os
from flask import Blueprint, jsonify, request, Response, request, flash, redirect, url_for
from .. import db

# 返回JSON
class Json(object):
    # 操作正常返回
    def success(self, data, msg = "success"):
        return jsonify(dict(ret = 200, data = data, msg = msg))

    # 操作失败返回
    def msg(self, ret = 500, msg = 'error'):
        return jsonify(dict(ret = ret, msg = msg))
        
    # 服务器错误
    def error(self, ret = 500, msg = "error"):
        return jsonify(dict(ret = ret, msg = msg)), ret
