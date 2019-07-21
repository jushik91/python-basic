
from bs4 import BeautifulSoup
from urllib import request
from urllib import parse

import sys,io,os

url='https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query='

parse_quote = parse.quote('강아지')

print(parse_quote)


img_url= url+parse_quote

savePath='D:\\pythonProject\\project\\day20190518\\img\\'

try:
    os.makedirs(savePath)
except:
    print('Fail')
    

html=request.urlopen(img_url).read()   ##해당되는 전체 Tage를 읽기 위해서 실행함

#print(html)

soup = BeautifulSoup(html,'html.parser')

#print(soup)  ##요건  주석풀면 에러남

list=soup.find_all('img', class_='_img')
#print(list)
#print(list[0])
#print(len(list))

for idx, img in enumerate(list,1):
    print(img['data-source'])   ## 이미지의 각 주소
    saveName=savePath + str(idx) + '.png'
    #print(saveName)

    request.urlretrieve(img['data-source'],saveName)  ## 파일마다 각 주소를 찾아가서 저장해라


print('success!!!!')
