# -*- coding:utf-8 -*-
from flask import Flask, Response, request, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from config import config

db = SQLAlchemy()

# http://flask.pocoo.org/docs/0.10/patterns/appfactories/
def app(configs):
    app = Flask(__name__)
    app.config.from_object(config[configs])
    db.init_app(app)

    # from index import api as default_blueprint
    # app.register_blueprint(default_blueprint, url_prefix='/')

    # 首页
    from v1.controllers.index import api as index_blueprint
    app.register_blueprint(index_blueprint, url_prefix = '/v1')

    # 用户
    from v1.controllers.users import api as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix = '/v1/users')

    return app
