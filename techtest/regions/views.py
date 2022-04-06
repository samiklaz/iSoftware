from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Region
from .serializers import RegionSerializer


class RegionAPIView(APIView):

    def get(self, request):
        query = Region.objects.all()
        serializer = RegionSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_dict = serializer.data
            serializer_dict["response"] = "successful"
            serializer_dict["status"] = "region_added_successful"
            return Response(serializer_dict, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegionEditAPIView(APIView):
    def get(self, request, id):
        try:
            query = Region.objects.get(id=id)
        except ObjectDoesNotExist:
            data = {
                "message": "error",
                "status": "region_not_found"
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer = RegionSerializer(query)
        data = serializer.data
        data["status"] = "successful"
        data["message"] = "region_fetched_successfully"
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            query = Region.objects.get(id=id)
        except ObjectDoesNotExist:
            data = {
                "message": "error",
                "status": "region_not_found",
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer = RegionSerializer(query, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            serializer_msg = serializer.data
            serializer_msg["response"] = "Successful"
            serializer_msg["status"] = "region_updated"
            return Response(data=serializer_msg, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            query = Region.objects.get(id=id)
            query.delete()
            data = {
                "message": "successful",
                "status": "deleted_successfully",
            }
            return Response(data=data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {
                "message": "error",
                "status": "region_not_found"
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
