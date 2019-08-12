from rest_framework import response

import logging


def render_response(result=None):
    res = {
        'msg': "succeed",
        'status': 0,
        'result': result,
    }
    print(res)
    return response.Response(res)


def render_exceptions(msg=None, status=1):
    res = {
        'msg': msg,
        'status': status,
    }
    print(res)
    return response.Response(res)
