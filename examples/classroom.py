# -*- coding: utf-8 -*-
'''
云课堂 example

创建__secret.py 添加cc的USERID, APIKEY
'''

from __secret import USERID, APIKEY

from bokecc_sdk import constants
from bokecc_sdk.classroom import ClassRoomAPI


def room_chat():
    '''
    创建直播间, 不需要密码
    response:
    {u'data': {u'roomid': u'E3EAA8CE5B3AF7BD9C33DC5901307461'}, u'result': u'OK'}
    '''
    classroom_api = ClassRoomAPI(APIKEY)
    userid = USERID
    name = 'sdk测试创建云课堂群聊视频直播间免密码'
    desc = 'sdk测试创建云课堂直播间desc'
    templatetype = constants.ClassRoomTemplateType.talk.value
    max_streams = max_users = 4 # 1vN = 1+N
    room_type = constants.ClassRoomRoomType.chat.value
    # no_password教师和助教的密码也是需要的
    publisherpass = 'tcctest'
    assist_pass = 'acctest'
    response = classroom_api.room_create(
        userid, name, room_type, templatetype, publisherpass, assist_pass,
        max_users=max_users, max_streams=max_streams, desc=desc,
    )
    return response


def room_small_classroom():
    '''
    创建直播间, 不需要密码
    response:
    {u'data': {u'roomid': u'E3EAA8CE5B3AF7BD9C33DC5901307461'}, u'result': u'OK'}
    '''
    classroom_api = ClassRoomAPI(APIKEY)
    userid = USERID
    name = 'sdk测试创建云课堂小班课直播间name免密码'
    desc = 'sdk测试创建云课堂直播间desc'
    templatetype = constants.ClassRoomTemplateType.talk.value
    max_streams = max_users = 5 # 1vN = 1+N
    room_type = constants.ClassRoomRoomType.small_class.value
    # no_password教师和助教的密码也是需要的
    publisherpass = 'tcctest'
    assist_pass = 'acctest'
    audience_pass = 'aucctest'
    talker_pass = 'tlcctest'
    inspector_pass = 'icctest'
    response = classroom_api.room_create(
        userid, name, room_type, templatetype, publisherpass, assist_pass,
        audience_pass=audience_pass, talker_pass=talker_pass,
        inspector_pass=inspector_pass, max_users=max_users, max_streams=max_streams, desc=desc,
    )
    return response


def update_room(roomid):
    '''
    修改直播间
    response
    {u'data': u'', u'result': u'OK'}
    '''
    classroom_api = ClassRoomAPI(APIKEY)
    userid = USERID
    name = 'sdk测试修改云课堂小班课直播间'
    desc = 'sdk测试修改云课堂直播间desc'
    templatetype = constants.ClassRoomTemplateType.talk.value
    max_streams = max_users = 2 # 1vN = 1+N
    room_type = constants.ClassRoomRoomType.small_class.value
    # no_password教师和助教的密码也是需要的
    publisherpass = 'tcctest1'
    audience_pass = 'aucctest1'
    assist_pass = 'acctest1'
    talker_pass = 'tlcctest1'
    inspector_pass = 'icctest1'
    response = classroom_api.room_update(
        userid, roomid, templatetype, name, publisherpass, assist_pass,
        audience_pass=audience_pass, talker_pass=talker_pass,
        inspector_pass=inspector_pass, max_users=max_users, max_streams=max_streams, desc=desc,
    )
    return response


def room_live_start(roomid):
    '''
    开始直播
    '''
    classroom_api = ClassRoomAPI(APIKEY)
    userid = USERID
    response = classroom_api.room_live_start(userid, roomid)
    return response


def room_live_stop(roomid):
    '''
    结束直播
    '''
    classroom_api = ClassRoomAPI(APIKEY)
    userid = USERID
    response = classroom_api.room_live_stop(userid, roomid)
    return response


def room_close(roomid):
    '''
    关闭直播间
    '''
    classroom_api = ClassRoomAPI(APIKEY)
    userid = USERID
    response = classroom_api.room_close(userid, roomid)
    return response


def room_list(name=None, status=None, page=1, lines=50, roomid=None):
    '''
    获取账号下房间列表
    '''
    classroom_api = ClassRoomAPI(APIKEY)
    userid = USERID
    response = classroom_api.room_list(
        userid, name=name, status=status, page=page, lines=lines, roomid=roomid
    )
    return response


def room_room_detail(roomid):
    '''
    获取房间信息
    '''
    classroom_api = ClassRoomAPI(APIKEY)
    userid = USERID
    response = classroom_api.room_room_detail(userid, roomid)
    return response


def room_link(roomid):
    '''
    获取房间登录链接
    response
    {u'data': {u'assist_url': u'https://class.csslcloud.net/index/assistant/?roomid=C9CBAB7F53A201249C33DC5901307461&userid=BC36C6119CAB4A42',
      u'audience_url': u'https://view.csslcloud.net/api/view/index?roomid=C9CBAB7F53A201249C33DC5901307461&userid=BC36C6119CAB4A42',
      u'inspector_url': u'https://class.csslcloud.net/index/inspector/?roomid=C9CBAB7F53A201249C33DC5901307461&userid=BC36C6119CAB4A42',
      u'presenter_url': u'https://class.csslcloud.net/index/presenter/?roomid=C9CBAB7F53A201249C33DC5901307461&userid=BC36C6119CAB4A42',
      u'talker_url': u'https://class.csslcloud.net/index/talker/?roomid=C9CBAB7F53A201249C33DC5901307461&userid=BC36C6119CAB4A42'},
     u'result': u'OK'}
    '''
    classroom_api = ClassRoomAPI(APIKEY)
    userid = USERID
    response = classroom_api.room_link(userid, roomid)
    return response


def room_set_single(roomid, status):
    '''
    获取房间信息
    '''
    classroom_api = ClassRoomAPI(APIKEY)
    userid = USERID
    response = classroom_api.room_set_single(userid, roomid, status)
    return response


def room_user_list(roomid):
    '''
    获取当前房间人员列表
    '''
    classroom_api = ClassRoomAPI(APIKEY)
    userid = USERID
    response = classroom_api.room_user_list(userid, roomid)
    return response


def room_live_stat(roomid):
    '''
    查询直播状态
    '''
    classroom_api = ClassRoomAPI(APIKEY)
    userid = USERID
    response = classroom_api.room_live_stat(userid, roomid)
    return response


def get_auto_login_url(roomid):
    '''获取直播间免密码登录url'''
    classroom_api = ClassRoomAPI(APIKEY)
    userid = USERID
    response = classroom_api.room_link(userid, roomid)['data']
    # 教师
    presenter_login_url = response['presenter_url']
    # 助教
    assist_login_url = response['assist_url']
    # 旁听
    audience_login_url = response['audience_url']
    # 互动
    talker_login_url = response['talker_url']
    # 隐身者
    inspector_login_url = response['inspector_url']

    name = 'test'

    publisherpass = 'tcctest'
    assist_pass = 'acctest'
    audience_pass = 'aucctest'
    talker_pass = 'tlcctest'
    inspector_pass = 'icctest'

    presenter_auto_login_url = classroom_api.get_auto_login_url(
        presenter_login_url, name, publisherpass, login_type=constants.ClassRoomAutoLoginType.presenter.value
    )
    assist_auto_login_url = classroom_api.get_auto_login_url(
        assist_login_url, name, assist_pass, login_type=constants.ClassRoomAutoLoginType.assistant.value
    )
    audience_auto_url = classroom_api.get_auto_login_url(
        audience_login_url, name, audience_pass, login_type=constants.ClassRoomAutoLoginType.audience.value
    )
    talker_auto_login_url = classroom_api.get_auto_login_url(
        talker_login_url, name, talker_pass, login_type=constants.ClassRoomAutoLoginType.talker.value
    )
    inspector_auto_login_url = classroom_api.get_auto_login_url(
        inspector_login_url, name, inspector_pass, login_type=constants.ClassRoomAutoLoginType.inspector.value
    )

    data = {
        'presenter_auto_login_url': presenter_auto_login_url,
        'assist_auto_login_url': assist_auto_login_url,
        'audience_auto_url': audience_auto_url,
        'talker_auto_login_url': talker_auto_login_url,
        'inspector_auto_login_url': inspector_auto_login_url,
    }
    return data
