from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

def find_video(url):
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
    youtube.to_csv(base_url.split('/')[-2] +'.csv', encoding='', index=False)
    driver.close()


find_video('https://www.youtube.com/channel/UCyn-K7rZLXjGl7VXGweIlcA')


# 코드 출처 https://m.blog.naver.com/tamiblue/221723206818