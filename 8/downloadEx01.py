

#import urllib.request

from urllib.request import urlretrieve

imgUrl="http://blogfiles.naver.net/20120808_257/aaugh33_1344410923803jfnxF_PNG/%BB%FD%B0%A2%B8%B9%C0%BA%B0%ED%BE%E7%C0%CC2.png"

savePath='D:\\pythonProject\\project\\day20190518\\cat03.png'

##urllib.request.urlretrieve(imgUrl,savePath)
urlretrieve(imgUrl,savePath)

print('sucess~~~!!!')
