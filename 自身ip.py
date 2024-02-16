#byDT
import requests #导入模块
page=requests.get('http://api.ipify.org') #get请求，page（页面）为名字
print(page.text) #打印page信息，txt形式