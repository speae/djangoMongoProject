from django.contrib import admin
from django.urls import include, path

#
urlpatterns = [
    #     # include : 다른 url을 참조할 수 있도록 함
    #     # admin은 파일 내부에 정의되어 있음
    #
    #     path("polls/", include("rest_api.urls")),
    #
    #     # path('articles/<int:year>/', views.year_archive),
    #     # path('articles/<int:year>/<int:month>/', views.month_archive),
    #     # path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]
