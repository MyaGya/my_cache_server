from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from .forms import UploadForm

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
            form.save()
            return redirect('cache_video:main')
    else:
        form = UploadForm()
    context = {'form': form}
    return render(request, 'cache_video/upload.html', context)

