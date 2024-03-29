from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.main_page.models import News, Banner, Video
from apps.main_page.serializers import NewsListSerializer, NewsSerializer, BannerSerializer, VideoSerializer


class NewsView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={200: NewsSerializer()},
        tags=['Home Page'],
    )
    def get(self, request, news_id):
        instance = get_object_or_404(News, id=news_id)
        serializer = NewsSerializer(instance, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewsListView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={200: NewsListSerializer(many=True)},
        tags=['Home Page'],
    )
    def get(self, request):
        queryset = News.objects.all()
        serializer = NewsListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class BannerListView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={200: BannerSerializer(many=True)},
        tags=['Home Page'],
    )
    def get(self, request):
        queryset = Banner.objects.all()
        serializer = BannerSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class VideoSerializerListView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={200: VideoSerializer(many=True)},
        tags=['Home Page'],
    )
    def get(self, request):
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
