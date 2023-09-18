
import re


from newSletter import kaisuo



keyWords = ['开锁','换锁','钥匙丢了']

def get_url(msg):
  text= msg.text
  url=None
  if(any(keyword in text for keyword in keyWords)):
              kaisuo(msg)


                

  

if __name__ == '__main__':
       get_url(' 淘宝搜索直接打开')