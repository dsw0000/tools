# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.now import Now
from .api.lifestyle import Lifestyle


routes = [
    dict(resource=Now, urls=['/now'], endpoint='now'),
    dict(resource=Lifestyle, urls=['/lifestyle'], endpoint='lifestyle'),
]