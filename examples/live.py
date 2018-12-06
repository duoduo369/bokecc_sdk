# -*- coding: utf-8 -*-
'''
直播 example

创建__secret.py 添加cc的USERID, APIKEY
'''
from __secret import USERID, APIKEY

from ccsdk import constants
from ccsdk.live import LiveAPI


def room_create_nopassword():
    '''
    response: {u'result': u'OK', u'room': {u'atlasRoomId': u'', u'id': u'06B80689C1653A459C33DC5901307461'}}
    # 有时候会有这种返回
    {u'result': u'OK', u'room': {u'atlasRoomId': u'', u'id': u'C3A806559DE44DB19C33DC5901307461',
     u'publishUrl': u'rtmp://119.23.200.43/origin/C3A806559DE44DB19C33DC5901307461?token=DVD2sV74'}}
    '''
    live_api = LiveAPI(APIKEY)
    userid = USERID
    name = 'sdk测试创建直播间name免密码'
    desc = 'sdk测试创建直播间desc'
    templatetype = constants.LiveTemplateType.video_chat.value
    authtype = constants.LiveAuthType.no_password.value
    # no_password教师和助教的密码也是需要的
    publisherpass = 'tcctest'
    assistantpass = 'acctest'
    response = live_api.room_create(
        userid, name, desc, templatetype, authtype, publisherpass, assistantpass
    )
    return response


def room_create_password():
    '''
    response: {u'result': u'OK', u'room': {u'atlasRoomId': u'', u'id': u'F620B27CA1FEFA269C33DC5901307461'}}
    '''
    live_api = LiveAPI(APIKEY)
    userid = USERID
    name = 'sdk测试创建直播间name密码'
    desc = 'sdk测试创建直播间desc'
    templatetype = constants.LiveTemplateType.video_doc_chat_qa.value
    authtype = constants.LiveAuthType.password.value
    publisherpass = 'tcctest'
    assistantpass = 'acctest'
    response = live_api.room_create(
        userid, name, desc, templatetype, authtype, publisherpass, assistantpass
    )
    return response

def room_update(roomid):
    '''
    {u'result': u'OK'}
    '''
    live_api = LiveAPI(APIKEY)
    userid = USERID
    name = 'sdk测试修改创建直播间name 无密码'
    desc = 'sdk测试创建直播间desc111'
    templatetype = constants.LiveTemplateType.video_doc_chat_qa.value
    authtype = constants.LiveAuthType.no_password.value
    publisherpass = 'tcctest1'
    assistantpass = 'acctest1'
    response = live_api.room_update(
        roomid, userid, name, desc, templatetype, authtype, publisherpass, assistantpass
    )
    return response


def room_close(roomid):
    live_api = LiveAPI(APIKEY)
    userid = USERID
    response = live_api.room_close(userid, roomid)
    return response


def viewtemplate_info():
    '''
    看起来是固定的
    视频 1
    视频，聊天，问答 2
    视频，聊天 3
    视频，文档，聊天 4
    视频，文档，聊天，问答 5
    视频，问答 6
    '''
    live_api = LiveAPI(APIKEY)
    userid = USERID
    response = live_api.viewtemplate_info(userid)
    return response
