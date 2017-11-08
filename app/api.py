# -*- coding:utf-8 -*-
import os, time, hashlib
from flask import jsonify, request
from .const import const

# API请求验证
class requestParams():
    def __init__(self, request):
        self.request = request
        self.token_params = 'token'
        self.auth_params = 'auth'
        self.time_params = 'time'
        self.time_out = 60000

    def getToken(self, default = None):
        return self.request.values.get(self.token_params, default, str)

    def getTime(self, default = 0):
        return self.request.values.get(self.time_params, default, int)

    def getAuth(self, default = None):
        return self.request.values.get(self.auth_params, default, str)

    # 获取授权数据
    def getAuthId(self, default = None):
        auth = self.getAuth()
        if auth is None:
            return self.errors(500, "The auth params cannot be none")

        return auth

    # 校验请求接口
    def validate(self):
        token = self.getToken()
        if token is None:
            return self.errors(500, "The token params cannot be none")

        timemap = self.getTime()
        if timemap <= 0:
            return self.errors(500, "The time params cannot be none")

        _time = time.time()
        if _time - timemap > self.time_out:
            return self.errors(500, "request timeout")

        keys = self.request.values.keys()
        keys.sort()

        params = []
        for key in keys:
            if key == self.token_params:
                continue
            params.append(key + '=' + self.request.values.get(key, ''))
        params.append(const.API_KEY)

        md5 = hashlib.md5("&".join(params).encode('utf-8')).hexdigest().lower()
        if md5 != token:
            return self.errors(500, "The token params is error. token:" + md5)
        return None

    def errors(self, code = 500, msg = "error"):
        return jsonify(dict(ret = code, msg = msg))
