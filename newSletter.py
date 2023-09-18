



def kaisuo(msg):
      msg.user.send('开锁电话：13663235181')
      msg.user.send_raw_msg(42, '<?xml version="1.0"?><msg bigheadimgurl="http://wx.qlogo.cn/mmhead/ver_1/fyGR9ibicQSiazsxmLBof5VsVWwFibofQBvmMicdjARIeBNROw0DZxTyIP6ia2kTiby9ibAzmAhUlEwR8xsSViadecgibqYw/0" smallheadimgurl="http://wx.qlogo.cn/mmhead/ver_1/fyGR9ibicQSiazsxmLBof5VsVWwFibofQBvmMicdjARIeBNROw0DZxTyIP6ia2kTiby9ibAzmAhUlEwR8xsSViadecgibqYw/132" username="wyl801827" nickname="A开锁换锁 汽车钥匙13663235181"  shortpy="" alias="" imagestatus="3" scene="17" province="河北" city="中国大陆" sign="" sex="1" certflag="0" certinfo="" brandIconUrl="" brandHomeUrl="" brandSubscriptConfigUrl="" brandFlags="0" regionCode="CN_Hebei_Zhangjiakou" biznamecardinfo="" />')
      msg.user.send_image('./data/img/kaisuo.jpg')

if __name__ == '__main__':
        kaisuo(None)