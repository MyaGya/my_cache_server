from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from .forms import UploadForm, RegisterUrlForm
from .models import UploadedFile, TrackingUrl
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import os, time


def go_main(request):
    '''
    시작페이지를 main으로 보내기 위한 기본 기능
    '''
    return redirect('cache_video:main')


def main(request):
    '''
    동영상 출력 페이지
    '''
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    main = TrackingUrl.objects.all()

    # 페이징처리
    paginator = Paginator(main, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'main': page_obj}
    return render(request, 'cache_video/main.html', context)


def upload(request):
    '''
    동영상 업로드
    '''
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.upload_time = timezone.now()
            my_form.user = request.user
            my_form.save()
            return redirect('cache_video:main')
    else:
        form = UploadForm()
    context = {'form': form}
    return render(request, 'cache_video/upload.html', context)


def upload_check(request):
    return render(request, 'cache_video/upload_check.html', {'user': request.user})


def main_detail(request, tracking_url_id:int):
    Obj = get_object_or_404(TrackingUrl, pk=tracking_url_id)
    Obj = Obj.localurl_set.all()
    print(Obj)
    return render(request, 'cache_video/main_detail.html', {'main': Obj})


def video_delete(request, uploadedfile_id):
    '''
    등록된 비디오를 삭제합니다.
    '''
    data = get_object_or_404(UploadedFile, pk=uploadedfile_id)
    data.delete()

    # os.remove(os.path.join(settings.MEDIA_ROOT, str(data.local)))
    return redirect('cache_video:upload_check')


def url_delete(request, urltracking_id):
    '''
    등록된 url을 삭제합니다.
    '''
    data = get_object_or_404(TrackingUrl, pk=urltracking_id)
    data.delete()

    return redirect('cache_video:add_url')

def add_url(request):
    '''
    트래킹 URL을 등록합니다.
    '''
    if request.method == 'POST':
        form = RegisterUrlForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            return redirect('cache_video:add_url')
    else:
        form = RegisterUrlForm()
    context = {'form': form, 'user': request.user}
    return render(request, 'cache_video/add_url.html', context)
