# -*- coding:utf-8 -*-
from . import *

api = Blueprint('indexBlueprint', __name__)

# 首页
@api.route('/', methods = ['GET'])
def index():
    return Json().success({'title': 'request success', 'version': '1.0.0'})