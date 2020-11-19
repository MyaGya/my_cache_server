from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from pytube import YouTube
import os
import django
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cache_server.settings')
django.setup()
from cache_video.models import TrackingUrl, LocalUrl, UploadedFile


def download_video(url, path):
    '''
    완성된 URL을 받아(실제 동영상 실행 페이지) 동영상을 path에 1080p으로 다운로드합니다.
    'https://www.youtube.com/watch?v=riI4FGbKN9k'
    '''
    try:
        data = YouTube(url).streams
        '''
        1080p 기능 임시 비활성화
        for s in data:
            if s.resolution == "1080p":
                return s.download(path)
        return data[0].download(path)
        '''
        return data.first().download(path)
    except:
        return "ERROR"


def find_video(url, path):
    '''
    채널의 url을 입력받아 path위치에 csv 파일을 생성합니다.
    '''
    driver = webdriver.Chrome('./chromedriver.exe')
    base_url = url +'/videos'
    driver.get(base_url)

    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    # 제목 조회
    all_videos = soup.find_all(id='dismissable')

    title_list = []
    video_time_list = []
    url_list = []
    thumbnail_list = []
    for video in all_videos[:10]:
        # 제목
        title = video.find(id='video-title')
        if len(title.text.strip())>0:
            title_list.append(title.text)

        # 재생 시간
        video_time = video.find('span',{'class' : 'style-scope ytd-thumbnail-overlay-time-status-renderer'})
        video_time_list.append(video_time.text.strip())


        # 링크 조회
        tmp_url = video.find(id='thumbnail')['href']
        url_list.append('https://www.youtube.com' + tmp_url)


        # 썸네일
        thumbnail = video.find(id='img')
        if 'src' in thumbnail.attrs:
            thumbnail_list.append(thumbnail)
        else:
            thumbnail_list.append('')
    dict_youtube = {'subject':title_list,'thumbnail':thumbnail_list, 'url':url_list, 'running_time':video_time_list}

    youtube = pd.DataFrame(dict_youtube)
    path = path + '/' + base_url.split('/')[-2] +'.csv'
    youtube.to_csv(path, encoding='', index=False)
    driver.close()
    csv_db_connection(url, path)


def csv_db_connection(url, filename):
    '''
    url : DB의 키값이 되어줄 URL입니다.(채널값) 예시 : 'https://www.youtube.com/channel/UCyn-K7rZLXjGl7VXGweIlcA'
    filename : 파일 전체 이름이 포함된 csv파일을 기준으로 데이터를 DB와 연동합니다. 예시 : './media/csv/ebsdocumentary.csv'
    '''
    f = open(filename, 'r')
    info = []
    rdr = csv.reader(f)
    tracking_url = TrackingUrl.objects.get(url=url)
    for i, row in enumerate(rdr):
        if i == 0:
            continue
        subject, thumbnail, url, running_time = row
        local = download_video(url, './media/' + filename.split('/')[-1][:-4])
        db = LocalUrl(tracking_url=tracking_url, subject=subject, thumbnail=thumbnail, local=local, url=url, running_time=running_time)
        print("처리중 : ", subject)
        db.save()



if __name__ == '__main__':
    tracking_url = TrackingUrl.objects.all()
    for url in tracking_url:
        print("작업중인 url : ", url.url)
        find_video(url.url, './media/csv')
