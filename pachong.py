import requests,threading
from bs4 import BeautifulSoup
import lxml
from lxml import etree
import re
from urllib.request import urlretrieve
def down_load():
    url='https://www.pearvideo.com/category_59'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    html=requests.get(url,headers=headers).text
    #把文本文件处理成可解析的对象
    html=etree.HTML(html )
    #<div class="vervideo-bd">
    #<a href="video_1583148" class="vervideo-lilink actplay" target="_blank">
    video_id=html.xpath('//div[@class="vervideo-bd"]/a/@href')
    start_url='https://www.pearvideo.com/'
    video_url=[]
    for id in video_id:
        new_url=start_url+id
        video_url.append(new_url)
    for playurl in video_url:
        html=requests.get(playurl).text
        req=r'srcUrl="(.*?)"'
        req=re.compile(req)
        purl=re.findall(req,html)
        req='<h1 class="video-tt">(.*?)</h1>'
        req=re.compile(req)
        pname=re.findall(req,html)
        print("正在下载视频%s"%pname)
        urlretrieve(purl[0],'D:\\reach\\down_mp4\\%s.mp4'%pname[0])
if __name__=="__main__":
    down_load()
#import requests
#import os
#import time
#import threading
#from bs4 import BeautifulSoup
#import lxml
#from urllib.request import urlretrieve
#
##def download_page(url): 
#    '''
#    用于下载页面
#    '''
#    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
#    r = requests.get(url, headers=headers)
#    r.encoding = 'gb2312'
#    return r.text
#
#
#
#
#
#def get_pic(link, text):
#    '''
#    获取当前页面的图片,并保存
#    '''
#    html = download_page(link)  # 下载界面
#    soup = BeautifulSoup(html, 'lxml')
#    pic_list = soup.find('div'e, id="picture").find_all('img')  # 找到界面所有图片
#    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
#    create_dir('pic/{}'.format(text))
#    for i in pic_list:
#        pic_link = i.get('src')  # 拿到图片的具体 url
#        r = requests.get(pic_link, headers=headers)  # 下载图片，之后保存到文件
#        with open('pic/{}/{}'.format(text, pic_link.split('/')[-1]), 'wb') as f:
#            f.write(r.content)
#            time.sleep(2)   # 休息一下，不要给网站太大压力，避免被封
#def get_pic_list(html):
#    '''
#    获取每个页面的套图列表,之后循环调用get_pic函数获取图片
#    '''
#    soup = BeautifulSoup(html, 'lxml')
#    pic_list = soup.find_all('li', class_='wp-item')
#    for i in pic_list:
#        a_tag = i.find('h3', class_='tit').find('a')
#        link = a_tag.get('href')
#        text = a_tag.get_text()
#        get_pic(link, text)
#
#def create_dir(name):
#    if not os.path.exists(name):
#        os.makedirs(name)
##        
##
##
#def execute(url):
#    page_html = download_page(url)
#    get_pic_list(page_html)
#
#
#def main():
#    create_dir('D:\\pic')
#    queue = [i for i in range(1, 7)]   # 构造 url 链接 页码。
#    threads = []
#    while len(queue) > 0:
#        for thread in threads:
#            if not thread.is_alive():
#                threads.remove(thread)
#        while len(threads) < 3 and len(queue) > 0:   # 最大线程数设置为 5
#            cur_page = queue.pop(0)
#            url = 'http://www.mzitu.com/mm/page/{}.html'.format(cur_page)
#            thread = threading.Thread(target=execute, args=(url,))
#            thread.setDaemon(True)
#            thread.start()
#            print('{}正在下载{}页'.format(threading.current_thread().name, cur_page))
#            threads.append(thread)
#
#if __name__ == '__main__':
#    main()
#    print('完成')
#url='https://ev.phncdn.com/videos/201303/14/10502701/vl_480P_720.0k_10502701.mp4?validfrom=1564451992&validto=1564459192&rate=127k&burst=2000k&hash=Xuvluyg6JX%2FVexaN8tBtaMpXudo%3D'
#root="D:\\reach\\down_mp4\\"
#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
#path=root+'dada.mp4'
#r=requests.get(url,headers=headers)
#with open(path,'wb') as f:
#    
#    f.write(r.content)
#    f.close()
#    print('文件保存成功')
#url_list=['https://dv.phncdn.com/videos/201808/22/179721421/480P_600K_179721421.mp4?ttl=1564476786&ri=2048000&rs=632&hash=fcf83eecb55c6656c692d94525b3e497','https://ev.phncdn.com/videos/201906/27/231876982/480P_600K_231876982.mp4?validfrom=1564470871&validto=1564478071&rate=58k&burst=1000k&hash=FRfsM1uvWF0hogMsKaCGYCzv6WE%3D','https://cv.phncdn.com/videos/201907/03/233088761/480P_600K_233088761.mp4?lp22yHW72gl7KeYkZ3DxkvnKFonhnNIvA10NjqFW04Nw3ZWqqTzIxeQJhpo0TM7MVca91Jgo--d55T5MzDbD_MTDDj0P65zHxOkeiuAYhWxxSB_DC_iYIqLwGgN0qviCJSxW2FohoTKcPJ8Ng9WS9vB8WQKUWWTTxzrNxhVshV06EygFnaDLISiXaMbVSnH7UokOS53G']
#name=['aa','bb','cc','dd','ee','ff']
#url_list=['https://cv.phncdn.com/videos/201905/11/223051481/480P_600K_223051481.mp4?IoNNavml4rnO-0OhmfAVRlhZi8RvjwfHJxKeY7CdV3VZs5YAxVoMfPMkwTaoGgu-gLvHC03bL34KoqBuKJNmleF5J253c_iXmuELKUnMB1b6b098KO4gp77s3X9H0KEyb4m-wLJeU7Dfd_Bx8soPZALE30EuZ1g7-jGV7KPJR4-m2g7WHLuEy4z8nm458lUFY19M_mzU','https://cv.phncdn.com/videos/201809/07/181860811/480P_600K_181860811.mp4?xibi-TvkOa7D2mBVGXmz2knNSwXuEEZteVHbadgAHeP6Lm4KyBWxTcmTjZkR9u0BbwUMHURY-7c7_0GuYpWptVqv6NUewDWGkTGvzKuXOuk04BtssNQfScTUTQh9YinNvMC9BYltSQ6fuEI6zOHU2tJEQH2Dj8ufA4YurW2injliFWgXGvGsRe1dJfe8J-Yt1uozPcNn','https://em.phncdn.com/videos/201905/11/223050921/480P_600K_223050921.mp4?validfrom=1564475975&validto=1564483175&rate=58k&burst=1200k&hash=5rP%2F%2BWs5xkI4Ppj3YqvD64%2FbmT8%3D','https://cm.phncdn.com/videos/201903/25/214848412/480P_600K_214848412.mp4?QpBgDt20uDJH2MqEGNXdhQWCGgRn_5Q41sxtug4eDmm2KwUi1YqHU6fQiTzVQKvuBpef9CD3-2uDGYqBH5bmr9IguEgLEhoTv7zzaF1YnEWRpCOT6DMN8zwf3EIlBooOHSBPVSQL76yjUuCM_LtLhTtaH9-bC1zpoJNbnBghUj7VxPppYy15C6w-VKJB0W-zYviiBAEM','https://dm.phncdn.com/videos/201905/31/226673641/480P_600K_226673641.mp4?ttl=1564483294&ri=1024000&rs=416&hash=039a09c67231147d8afa9c707a8ef6fc','https://dm.phncdn.com/videos/201907/20/236555521/480P_600K_236555521.mp4?ttl=1564483370&ri=1638400&rs=704&hash=4af34506af01bf3ab4194ac77fc2cfe9']
#root="D:\\reach\\down_mp4\\"
#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
#for i,name1 in zip(url_list,name):
#    r=requests.get(i,headers=headers,stream=True)
#    path=root+name1+'.mp4'
#    with open(path,'wb') as f:
#        f.write(r.content)
#        f.close()
#print('文件保存成功')
#    
    


    



















