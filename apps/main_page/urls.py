from django.urls import path

from apps.main_page.views import NewsListView, NewsView, BannerListView, VideoSerializerListView

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<uuid:news_id>/', NewsView.as_view(), name='news-detail'),
    path('banners/', BannerListView.as_view(), name='banners'),
    path('videos/', VideoSerializerListView.as_view(), name='videos')
]
