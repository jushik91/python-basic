
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


from bs4 import BeautifulSoup
import urllib.request as request

url='https://media.daum.net/'
path='D:\\pythonProject\\project\\day20190518\\news.txt'

url_read=request.urlopen(url).read()

#print(url_read)

soup=BeautifulSoup(url_read,'html.parser')

news = soup.find('ol',class_='list_popcmt').find_all('a')


##print(news)


for idx,n in enumerate(news,1):
    print('{}. {}'.format(idx,n.get_text().splitlines()[2].strip()))

#print(type(get_text()))
