
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),        # /를 붙임으로써 페이지 정규화를 진행하혀 /admin/ /admin 둘 모두 해당시킨다.
    path('', include('cache_video.urls'))   # 메인 페이지
]
