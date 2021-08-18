from rest_framework.response import Response


def response(status=None, message=None, data=None):
    res = {}

    if status:
        res['code'] = status

    if message:
        res['message'] = message

    if data:
        res['data'] = data

    return Response(res, status)
