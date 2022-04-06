from nntplib import ArticleInfo
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer


class ArticleAPIView(APIView):

    def get(self, request):
        query = Article.objects.all()
        serializer = ArticleSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_dict = serializer.data
            serializer_dict["response"] = "successful"
            serializer_dict["status"] = "article_added_successful"
            return Response(serializer_dict, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleEditAPIView(APIView):
    def get(self, request, id):
        try:
            query = Article.objects.get(id=id)
        except ObjectDoesNotExist:
            data = {
                "message": "error",
                "status": "region_not_found"
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer = ArticleSerializer(query)
        data = serializer.data
        data["status"] = "successful"
        data["message"] = "article_fetched_successfully"
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            query = Article.objects.get(id=id)
        except ObjectDoesNotExist:
            data = {
                "message": "error",
                "status": "article_not_found",
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer = ArticleSerializer(query, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            serializer_msg = serializer.data
            serializer_msg["response"] = "Successful"
            serializer_msg["status"] = "article_updated"
            return Response(data=serializer_msg, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            query = Article.objects.get(id=id)
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
