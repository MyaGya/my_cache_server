from django.db import models

# DB를 계산함에 있어서 id는 자동으로 추가된다.


class User(models.Model):
    email = models.CharField(max_length=30)     # 이메일
    password = models.CharField(max_length=20)  # 패스워드
    name = models.CharField(max_length=20)      # 이름


class TrackingUrl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # 등록한 유저
    url = models.CharField(max_length=100)                      # 등록한 url


class LocalUrl(models.Model):
    tracking_url = models.ForeignKey(TrackingUrl, on_delete=models.CASCADE)  # 지정되어있는 트래킹 url
    url = models.CharField(max_length=100)                                   # 실제 다운로드 하고자 하는 url
    local = models.CharField(max_length=100)                                 # 다운하고자 하는 파일의 local 위치

