from django.urls import path
from . import views

app_name = 'cache_video'
urlpatterns = [
    path('', views.go_main, name='go_main'),                                                     # 메인 페이지
    path('main/', views.main, name='main'),                                                     # 메인 페이지
    path('upload/', views.upload, name='upload'),                                           # 업로드 페이지
    path('my_video/', views.my_video, name='my_video')                                           # 내 비디오

    #path('<int:question_id>/', views.detail, name='detail'),                              # 상세보기 페이지
    #path('answer/create/', views.question_create, name='question_create'),                # 질문 생성 페이지
]