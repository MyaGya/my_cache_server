from django.urls import path
from . import views

app_name = 'cache_video'
urlpatterns = [
    path('', views.main, name='main'),                                                     # 메인 페이지
    path('upload/', views.upload, name='upload')                                                     # 메인 페이지
    #path('<int:question_id>/', views.detail, name='detail'),                              # 상세보기 페이지
    #path('answer/create/', views.question_create, name='question_create'),                # 질문 생성 페이지
]