from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from .forms import UploadForm
from .models import UploadedFile, User
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
            my_form.uploaded_date = timezone.now()
            my_form.user = get_object_or_404(User, pk=request.user.id)
            my_form.save()
            return redirect('cache_video:')
    else:
        form = UploadForm()
    context = {'form': form}
    return render(request, 'cache_video/upload.html', context)

def my_video(request):
    documents = UploadedFile.objects.all()
    return render(request, 'cache_video/my_video.html', {'documents': documents})