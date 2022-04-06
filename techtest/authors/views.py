from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Author
from .serializers import AuthorSerializer


class AuthorAPIView(APIView):

    def get(self, request):
        shifts = Author.objects.all()
        serializer = AuthorSerializer(shifts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_dict = serializer.data
            serializer_dict["response"] = "successful"
            serializer_dict["status"] = "author_added_successful"
            return Response(serializer_dict, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorEditAPIView(APIView):
    def get(self, request, id):
        try:
            query = Author.objects.get(id=id)
        except ObjectDoesNotExist:
            data = {
                "message": "error",
                "status": "author_not_found"
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(query)
        data = serializer.data
        data["status"] = "successful"
        data["message"] = "author_fetched_successfully"
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            query = Author.objects.get(id=id)
        except ObjectDoesNotExist:
            data = {
                "message": "error",
                "status": "author_not_found",
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer = AuthorSerializer(query, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            serializer_msg = serializer.data
            serializer_msg["response"] = "Successful"
            serializer_msg["status"] = "author_updated"
            return Response(data=serializer_msg, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            query = Author.objects.get(id=id)
            query.delete()
            data = {
                "message": "successful",
                "status": "deleted_successfully",
            }
            return Response(data=data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            data = {
                "message": "error",
                "status": "author_not_found"
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
