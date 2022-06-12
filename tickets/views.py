from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from tickets.models import Guest
from rest_framework.response import Response as RestResponse
from rest_framework.request import Request as RestRequest
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics

from tickets.serializers import GuestSerializer
from tickets.utils import get_or_throw

# 1  fbv no rest_framework , no model query


def no_rest_no_model(request):
    guest = [{"id": 1, "name": "omar", "mobile": 123456}, {"id": 2, "name": "ali", "mobile": 654321}]
    return JsonResponse(guest, safe=False)


def no_rest_with_model(request):

    guest = Guest.objects.all()
    vals = guest.values("name", "mobile")
    lista = list(vals)

    response = {"guest": lista}

    return JsonResponse(response)


# fbv rest_framework

# list GET
# create POST

# DELETE DELETE
# UPDATE PUT
# pk query GET

# list GET
# create POST

# FBV
@api_view(["GET", "POST"])
def guest_list(request):
    if request.method == "GET":
        guests = Guest.objects.all()
        data = GuestSerializer(guests, many=True).data
        return RestResponse(data=data)

    elif request.method == "POST":
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# DELETE DELETE
# UPDATE PUT
# pk query GET
@api_view(["GET", "DELETE", "PUT"])
def guest_pk(request: RestRequest, pk: int):

    guest = get_object_or_404(Guest, pk)

    if request.method == "GET":
        data = GuestSerializer(guest).data
        return RestResponse(data=data)

    elif request.method == "PUT":
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":

        guest.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


# CBV
class GuestList(APIView):
    def get(self, request):

        guests = Guest.objects.all()
        data = GuestSerializer(guests, many=True).data
        return RestResponse(data=data)

    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class Guest_pk(APIView):
    def get(self, request):
        data = GuestSerializer(guest).data
        return RestResponse(data=data)

    def put(self, request):
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        guest.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


# mixin
class GuestListMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class Guest_pk_Mixin(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request):
        return self.retrieve(request)

    def put(self, request):
        return self.update(request)

    def delete(self, request):
        return self.destroy(request)


# Generics
class GuestListGenerics(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class Guest_pk_Generics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


from rest_framework import viewsets

# View Sets
class GuestViewset(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
