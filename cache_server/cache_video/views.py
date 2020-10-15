from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse("메인 페이지의 테스트 입니다")