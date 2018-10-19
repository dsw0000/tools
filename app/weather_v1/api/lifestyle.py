# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

from app.weather_v1.api import api_key

from requests import get
from json import loads


class Lifestyle(Resource):

    def get(self):
        try:
            location = g.args["location"]
        except KeyError:
            return {"status": -1, "message": "params error: %s" % (g.args.__str__)}, 400, None

        heweather_runtime_url = "https://api.heweather.com/s6/weather/lifestyle?"

        res = get(
            url=heweather_runtime_url,
            params={
                "location": location,
                "key": api_key,
            }
        )

        if res.status_code != 200:
            return {"status": -1, "message": "request he weather error"}, 400, None

        data = loads(res.content.decode("utf-8"))["HeWeather6"][0]

        return {"status": 0, "message": "success", "data": data}, 200, None
