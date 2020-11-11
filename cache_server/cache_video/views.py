from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from .forms import UploadForm
from .models import UploadedFile
from django.contrib.auth.models import User
import os, time
from cache_server import settings# 삭제에 사용


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
    # question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    # paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    # page_obj = paginator.get_page(page)

    # context = {'question_list': page_obj}
    return render(request, 'cache_video/video_list.html')


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


def my_video(request):
    return render(request, 'cache_video/my_video.html', {'user': request.user})


def video_delete(request, uploadedfile_id):
    '''
    등록된 비디오를 삭제합니다.
    '''
    data = get_object_or_404(UploadedFile, pk=uploadedfile_id)
    data.delete()

    # os.remove(os.path.join(settings.MEDIA_ROOT, str(data.local)))
    return redirect('cache_video:my_video')
