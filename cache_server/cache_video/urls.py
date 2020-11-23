from django.urls import path
from . import views

app_name = 'cache_video'
urlpatterns = [
    path('', views.go_main, name='go_main'), # 메인 페이지
    path('main/', views.main, name='main'),  # 메인 페이지
    path('main_detail/<int:tracking_url_id>', views.main_detail, name='main_detail'),  # 메인 페이지의 상세 보기
    path('upload/', views.upload, name='upload'),  # 업로드 페이지
    path('upload_check/', views.upload_check, name='upload_check'),  # 업로드 파일 확인 페이지
    path('upload_check/video_delete/<int:uploadedfile_id>', views.video_delete, name='video_delete'),  # 비디오 삭제 기능
    path('upload_check/url_delete/<int:urltracking_id>', views.url_delete, name='url_delete'),  # url 삭제 기능
    path('upload_check/add_url', views.add_url, name='add_url'),  # url 등록 페이지


    # path('<int:question_id>/', views.main_detail, name='main_detail'),                              # 상세보기 페이지
    # path('answer/create/', views.question_create, name='question_create'),                # 질문 생성 페이지
]
