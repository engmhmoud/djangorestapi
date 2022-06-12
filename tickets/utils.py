from rest_framework.response import Response as RestResponse
from rest_framework import status


def get_or_throw(model, pk):
    try:
        obj = model.objects.get(pk)
        return obj
    except model.DoesNotExist:
        return RestResponse(status=status.HTTP_404_NOT_FOUND)
