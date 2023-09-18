import itchat
from itchat.content import *
from get_shop_Url import get_url



class wxBox:
     
     def __init__(self):
        itchat.auto_login(hotReload=True)
        self.wxBox= itchat 

     def run(self,block=True):
        self.notifySelf('wxBox is running')         
        @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
        def text_reply(msg):
            if( (msg.User is  None) or (msg.User["UserName"]!=msg['FromUserName'])):return
            if(msg.type=='Text'):
                get_url(msg)
        @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
        def download_files(msg):
            msg.download(msg.fileName)
            typeSymbol = {
                PICTURE: 'img',
                VIDEO: 'vid', }.get(msg.type, 'fil')
            msg.user.send('你好 我现在休息  我会记录您的消息，您看可以吗')
            return '@%s@%s' % (typeSymbol, msg.fileName)

        @itchat.msg_register(FRIENDS)
        def add_friend(msg):
            msg.user.verify()
            msg.user.send('Nice to meet you!')

        @itchat.msg_register(TEXT, isGroupChat=True)
        def text_reply(msg):
            if(msg.User["UserName"]!=msg['FromUserName']):return
            get_url(msg)
            if msg.isAt:
                # msg.user.send(u'@%s\u2005I received: %s' % (msg.actualNickName, msg.text))
                msg.user.send(u'@%s\u2005: %s' % (msg.actualNickName, '我还休息，看到后回复您'))
        self.wxBox.run(block)


     def notifySelf(self,text):
        friend= self.wxBox.search_friends(name='那以前是海')[0]
        self.wxBox.send(text,toUserName=friend.UserName)

     def notifyAll(self,text):
        friends = self.get_friends()
        for friend in friends:
            self.wxBox.send(text,toUserName=friend.UserName)
            
     def get_friends(self):
        return self.wxBox.get_friends(update=True)

if __name__ == "__main__":
    wx = wxBox()
    wx.run()