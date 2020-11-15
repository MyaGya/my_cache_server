from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd


driver = webdriver.Chrome('./chromedriver.exe')
url = 'https://www.youtube.com/channel/UCyn-K7rZLXjGl7VXGweIlcA/videos'
driver.get(url)
'''
스크롤 기능 미사용
import time
SCROLL_PAUSE_TIME = 0.5
# 한번 스크롤 하고 멈출 시간 설정

body = driver.find_element_by_tag_name('body')
# body태그를 선택하여 body에 넣음

while True:
    last_height = driver.execute_script('return document.documentElement.scrollHeight')
    # 현재 화면의 길이를 리턴 받아 last_height에 넣음
    for i in range(10):
        body.send_keys(Keys.END)
        # body 본문에 END키를 입력(스크롤내림)
        time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script('return document.documentElement.scrollHeight')
    if new_height == last_height:
        break;
'''

page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
# 제목 조회
all_videos = soup.find_all(id='dismissable')

title_list = []
for video in all_videos:
    title = video.find(id='video-title')
    print(type(title))
    if len(title.text.strip())>0:
        title_list.append(title.text)
    # 공백을 제거하고 글자수가 0보다 크면 append

# 재생 시간 조회
video_time_list = []
for video in all_videos:
    video_time = video.find('span',{'class' : 'style-scope ytd-thumbnail-overlay-time-status-renderer'})
    video_time_list.append(video_time.text.strip())


# 링크 조회
url_list = []
for video in all_videos:
    url = video.find(id='thumbnail')['href']
    url_list.append(url)

# 썸네일
thumbnail_list = []
for video in all_videos:
    thumbnail = video.find(id='img')
    if 'src' in thumbnail.attrs:
        thumbnail_list.append(thumbnail)
    else:
        thumbnail_list.append('')
'''
재생 시간 데이터 클렌징(미사용)
def stime(text):
    time = text.split(':')
    if len(time) == 1:
        return int(time[0])
    elif len(time) == 2:
        return int(time[0])*60 + int(time[1])
    else:
        return int(time[0])*3600 + int(time[1]*60 + int(time[2]))
    
video_time_seperate_list = []
for time in video_time_list:
    video_time_seperate_list.append(stime(time))

print(video_time_seperate_list)
'''

dict_youtube = {'subject':title_list, 'running_time':video_time_list, 'thumbnail':thumbnail_list, 'url':url_list}

youtube = pd.DataFrame(dict_youtube)
youtube.to_csv('오마이걸유튜브.csv', encoding='', index=False)
driver.close()