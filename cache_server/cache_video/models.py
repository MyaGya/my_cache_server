from django.db import models
from django.contrib.auth.models import User

#class User(models.Model):
#    email = models.CharField(max_length=30)     # 이메일
#    password = models.CharField(max_length=20)  # 패스워드
#    name = models.CharField(max_length=20)      # 이름


class TrackingUrl(models.Model):
    '''
    사용자가 추적하고자 하는 유투브 채널
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # 등록한 유저
    url = models.CharField(max_length=100)                      # 등록한 url
    subject = models.CharField(max_length=100)                  # 유저가 붙인 해당 채널의 이름


class LocalUrl(models.Model):
    '''
    해당 유투브 채널이 가지고 있는 동영상 정보
    '''
    tracking_url = models.ForeignKey(TrackingUrl, on_delete=models.CASCADE)  # 지정되어있는 트래킹 url
    subject = models.CharField(max_length=100)                               # 제목
    url = models.CharField(max_length=100)                                   # 다운하고자 하는 파일의 웹 위치
    local = models.CharField(max_length=100, blank=True)                     # 다운하고자 하는 파일의 local 위치
    thumbnail = models.CharField(max_length=100, blank=True)                 # 썸네일 파일의 local 위치
    running_time = models.DateTimeField(max_length=100)                      # 동영상 길이


class UploadedFile(models.Model):
    '''
    개별 업로드 파일의 데이터
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # 파일을 올린 유저
    subject = models.CharField(max_length=100)                  # 제목
    upload_time = models.DateTimeField()                        # 업로드된 시간
    local = models.FileField(upload_to='media/')                # 다운하고자 하는 파일의 local 위치

