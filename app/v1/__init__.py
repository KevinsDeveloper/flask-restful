# -*- coding:utf-8 -*-
from .. import db
from flask import jsonify, request

# 自定义错误处理
class ApiException(Exception):
    # 状态码
    status_code = 500
    # 服务器返回装状态码
    response_code = 200

    # 初始化错误信息
    def __init__(self, code = None, message = None):
        Exception.__init__(self)
        self.message = message
        if code is not None:
            self.status_code = code

    # 输出json
    def toJson(self, code = None):
        if code is not None:
            self.response_code = code

        response = dict(ret = self.status_code, msg = self.message)
        return jsonify(response), self.response_code