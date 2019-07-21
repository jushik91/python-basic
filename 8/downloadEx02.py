

import urllib.request as request


imgUrl = 'http://post.phinf.naver.net/MjAxOTAxMTdfMTcy/MDAxNTQ3NzAyOTM5MjA2.Q9esCJBNfwU5_Km2knanRajjBVv0VlP8kLf2sZQVNG0g.jNnLObz2UsNUuUKJRgIVNxlrjDXEU9LW1coRlfMs7bog.JPEG/IJQzrtncR28ecyJoBHmE_-Z2WD6A.jpg'


savePath='D:\\pythonProject\\project\\day20190518\\cat04.png'

img=request.urlopen(imgUrl).read()

# saveImg=open(savePath,'wb')  ##wb는 binary 파일로 저장해라
# saveImg.write(img)
# saveImg.close()


###with 문으로 사용

with open(savePath,'wb') as saveImg:
    saveImg.write(img)



print('success~~~~!!!')
