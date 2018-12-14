# -*- coding: utf-8 -*-
'''
直播 example

创建__secret.py 添加cc的APIKEY
'''
from __secret import APIKEY

from bokecc_sdk import constants
from bokecc_sdk.live import LiveAPI


def room_create_nopassword():
    '''
    创建直播间, 不需要密码
    response:
    {u'result': u'OK', u'room': {u'atlasRoomId': u'', u'id': u'06B80689C1653A459C33DC5901307461'}}
    # 有时候会有这种返回
    {u'result': u'OK', u'room': {u'atlasRoomId': u'', u'id': u'C3A806559DE44DB19C33DC5901307461',
     u'publishUrl': u'rtmp://119.23.200.43/origin/C3A806559DE44DB19C33DC5901307461?token=DVD2sV74'}}
    '''
    live_api = LiveAPI(APIKEY)
    name = 'sdk测试创建直播间name免密码'
    desc = 'sdk测试创建直播间desc'
    templatetype = constants.LiveTemplateType.video_chat.value
    authtype = constants.LiveAuthType.no_password.value
    # no_password教师和助教的密码也是需要的
    publisherpass = 'tcctest'
    assistantpass = 'acctest'
    response = live_api.room_create(
        name, desc, templatetype, authtype, publisherpass, assistantpass
    )
    return response


def room_create_password():
    '''
    创建直播间, 需要密码
    response:
    {u'result': u'OK', u'room': {u'atlasRoomId': u'', u'id': u'F620B27CA1FEFA269C33DC5901307461'}}
    '''
    live_api = LiveAPI(APIKEY)
    name = 'sdk测试创建直播间name密码'
    desc = 'sdk测试创建直播间desc'
    templatetype = constants.LiveTemplateType.video_doc_chat_qa.value
    authtype = constants.LiveAuthType.password.value
    publisherpass = 'tcctest'
    assistantpass = 'acctest'
    response = live_api.room_create(
        name, desc, templatetype, authtype, publisherpass, assistantpass
    )
    return response

def room_update(roomid):
    '''
    编辑直播间
    response
    {u'result': u'OK'}
    '''
    live_api = LiveAPI(APIKEY)
    name = 'sdk测试修改创建直播间name 无密码'
    desc = 'sdk测试创建直播间desc111'
    templatetype = constants.LiveTemplateType.video_doc_chat_qa.value
    authtype = constants.LiveAuthType.no_password.value
    publisherpass = 'tcctest1'
    assistantpass = 'acctest1'
    response = live_api.room_update(
        roomid, name, desc, templatetype, authtype, publisherpass, assistantpass
    )
    return response


def room_close(roomid):
    '''
    关闭直播间
    response
    {u'result': u'OK'}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.room_close(roomid)
    return response


def room_info(pagenum=50, pageindex=1):
    '''
    获取直播间列表
    response
    {u'count': 18,
     u'pageIndex': 1,
     u'result': u'OK',
     u'rooms': [{u'alarms': u'',
       u'assistantPass': u'123',
       u'authType': 2,
       u'barrage': 1,
       u'checkUrl': u'',
       u'clientDocPermissions': u'1',
       u'delayTime': u'3',
       u'desc': u'<p>\u6211\u4eec\u662f\u5144\u5f1f</p>',
       u'documentDisplayMode': u'1',
       u'dvr': u'0',
       u'foreignPublish': 0,
       u'hostLoginMode': u'0',
       u'id': u'7980A264F1C5F17F9C33DC5901307461',
       u'liveStartTime': u'',
       u'loginPageBannerImageUri': u'',
       u'manuallyRecordMode': u'0',
       u'maxAudienceNum': u'0',
       u'multiQuality': u'0',
       u'name': u'\u8d75\u6668\u9633\u6d4b\u8bd5\uff08\u52ff\u52a81\uff09',
       u'openHostMode': u'0',
       u'openLiveCountdown': u'0',
       u'openLowDelayMode': u'0',
       u'openMarquee': u'0',
       u'playPass': u'',
       u'playerBackgroundHint': u'',
       u'playerBackgroundImageUri': u'',
       u'publishUrls': [],
       u'publisherPass': u'123',
       u'repeatedLoginSetting': u'0',
       u'showAssistOnlineNum': u'1',
       u'showLectuerOnlineNum': u'1',
       u'showMobileAdvertisement': u'0',
       u'showUserCount': u'1',
       u'status': 10,
       u'templateType': 5,
       u'viewPageBannerImageUri': u'',
       u'warmVideoId': u'',
       u'whiteListId': u'9C33DC5901307461'}]}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.room_info(pagenum, pageindex)
    return response


def room_search(roomid):
    '''
    获取直播间信息
    response
    {u'result': u'OK',
     u'room': {u'alarms': u'',
      u'assistantPass': u'acctest1',
      u'authType': 2,
      u'barrage': 0,
      u'cashsReward': u'0',
      u'checkUrl': u'None',
      u'clientDocPermissions': u'0',
      u'delayTime': u'3',
      u'desc': u'sdk\u6d4b\u8bd5\u521b\u5efa\u76f4\u64ad\u95f4desc111',
      u'documentDisplayMode': u'1',
      u'dvr': u'0',
      u'foreignPublish': -1,
      u'hostLoginMode': u'0',
      u'id': u'780DEE01F06950939C33DC5901307461',
      u'liveStartTime': u'',
      u'loginPageBannerImageUri': u'',
      u'manuallyRecordMode': u'0',
      u'maxAudienceNum': u'0',
      u'multiQuality': u'0',
      u'name': u'sdk\u6d4b\u8bd5\u4fee\u6539\u521b\u5efa\u76f4\u64ad\u95f4name \u65e0\u5bc6\u7801',
      u'openHostMode': u'0',
      u'openLiveCountdown': u'0',                                                                                       [0/1803]
      u'openLowDelayMode': u'0',
      u'openMarquee': u'0',
      u'playPass': u'None',
      u'playerBackgroundHint': u'',
      u'playerBackgroundImageUri': u'',
      u'propsReward': u'0',
      u'publishUrls': [],
      u'publisherPass': u'tcctest1',
      u'repeatedLoginSetting': u'0',
      u'shareDescribe': u'',
      u'sharePicture': u'',
      u'shareTitle': u'',
      u'showAssistOnlineNum': u'1',
      u'showLectuerOnlineNum': u'1',
      u'showMobileAdvertisement': u'0',
      u'showUserCount': u'1',
      u'status': 10,
      u'templateType': 5,
      u'viewPageBannerImageUri': u'',
      u'warmVideoId': u'',
      u'webLoginVerify': u'0',
      u'whiteListId': u'9C33DC5901307461'}}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.room_search(roomid)
    return response

def room_code(roomid):
    '''
    获取直播间代码
    response
    {u'assistantLoginUrl': u'https://view.csslcloud.net/api/view/assistant?roomid=780DEE01F06950939C33DC5901307461&userid=BC36C6119CAB4A42',
     u'clientLoginUrl': u'https://view.csslcloud.net/api/view/lecturer?roomid=780DEE01F06950939C33DC5901307461&userid=BC36C6119CAB4A42',
     u'publishUrls': [],
     u'result': u'OK',
     u'roomId': u'780DEE01F06950939C33DC5901307461',
     u'viewUrl': u'https://view.csslcloud.net/api/view/index?roomid=780DEE01F06950939C33DC5901307461&userid=BC36C6119CAB4A42'}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.room_code(roomid)
    return response


def live_info(roomid, pagenum=50, pageindex=1, starttime='', endtime=''):
    '''
    获取直播列表
    response
    {u'count': 4,
     u'lives': [{u'endTime': u'2018-12-07 10:42:17',
       u'id': u'5B14026348D1A9BE',
       u'recordVideoStatus': 110,
       u'sourceType': 1,
       u'startTime': u'2018-12-07 10:41:01',
       u'templateType': 3}],
     u'pageIndex': 1,
     u'result': u'OK'}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.live_info(roomid, pagenum=pagenum, pageindex=pageindex)
    return response


def record_info(roomid, pagenum=50, pageindex=1, starttime='', endtime=''):
    '''
    获取回放列表
    response
    {u'count': 4,
     u'pageIndex': 1,
     u'records': [{u'id': u'C029B2B66ECAD010',
       u'liveId': u'5B14026348D1A9BE',
       u'offlinePackageMd5': u'369CC79D9739A90A0DFACBAD0CB97BB4',
       u'offlinePackageUrl': u'http://ccr.csslcloud.net/BC36C6119CAB4A42/06B80689C1653A459C33DC5901307461/C029B2B66ECAD010.ccr',
       u'recordStatus': 1,
       u'recordVideoId': u'6F171D9A70E8F5B99C33DC5901307461',
       u'recordVideoStatus': 3,
       u'replayUrl': u'http://view.csslcloud.net/api/view/callback?roomid=06B80689C1653A459C33DC5901307461&userid=BC36C6119CAB4A42&liveid=5B14026348D1A9BE&recordid=C029B2B66ECAD010',
       u'sourceType': 1,
       u'startTime': u'2018-12-07 10:41:01',
       u'stopTime': u'2018-12-07 10:42:17',
       u'templateType': 3}],
     u'result': u'OK'}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.record_info(roomid, pagenum=pagenum, pageindex=pageindex)
    return response


def record_search(recordid):
    '''
    查询回放信息
    response
    {u'record': {u'downloadUrl': u'http://cm14-ccm1-2.play.bokecc.com/flvs/ca/Qxnlj/urotONRGuW-90.mp4?t=1544161456&key=22EB5613B3D6F39E0A478A8F49B9B371',
      u'id': u'C029B2B66ECAD010',
      u'liveId': u'5B14026348D1A9BE',
      u'offlinePackageMd5': u'369CC79D9739A90A0DFACBAD0CB97BB4',
      u'offlinePackageUrl': u'http://ccr.csslcloud.net/BC36C6119CAB4A42/06B80689C1653A459C33DC5901307461/C029B2B66ECAD010.ccr',
      u'recordStatus': 1,
      u'recordVideoId': u'6F171D9A70E8F5B99C33DC5901307461',
      u'recordVideoStatus': 3,
      u'replayUrl': u'http://view.csslcloud.net/api/view/callback?roomid=06B80689C1653A459C33DC5901307461&userid=BC36C6119CAB4A42&liveid=5B14026348D1A9BE&recordid=C029B2B66ECAD010',
      u'sourceType': 1,
      u'startTime': u'2018-12-07 10:41:01',
      u'stopTime': u'2018-12-07 10:42:17',
      u'templateType': 3},
     u'result': u'OK'}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.record_search(recordid)
    return response


def live_merge(roomid, recordids):
    '''
    合并回放接口
    response
    {u'recordid': u'4068F1FEFC947A6F', u'result': u'OK'}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.live_merge(roomid, recordids)
    return response


def rooms_broadcasting(roomid):
    '''
    获取正在直播的直播间列表
    response
    {u'result': u'OK',
     u'rooms': [{u'liveId': u'50CCA32FA0C855B1',
       u'roomId': u'06B80689C1653A459C33DC5901307461',
       u'startTime': u'2018-12-07 12:00:55'}]}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.rooms_broadcasting(roomid)
    return response


def rooms_publishing(roomids):
    '''
    获取直播间直播状态
    response
    {u'result': u'OK',
     u'rooms': [{u'liveStatus': 0,
       u'roomId': u'06B80689C1653A459C33DC5901307461'}]}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.rooms_publishing(roomids)
    return response


def statis_connections(roomid, starttime, endtime):
    '''
    获取直播间连接数
    response
    {u'connections': [{u'count': 2,
       u'replayCount': 0,
       u'time': u'2018-12-07 10:01:39'},
      {u'count': 1, u'replayCount': 0, u'time': u'2018-12-07 10:03:39'},
      {u'count': 1, u'replayCount': 0, u'time': u'2018-12-07 10:05:39'},
      {u'count': 1, u'replayCount': 0, u'time': u'2018-12-07 10:07:39'},
      {u'count': 1, u'replayCount': 0, u'time': u'2018-12-07 10:09:39'},
      {u'count': 1, u'replayCount': 0, u'time': u'2018-12-07 10:11:39'},
      {u'count': 1, u'replayCount': 0, u'time': u'2018-12-07 10:13:39'},
      {u'count': 1, u'replayCount': 0, u'time': u'2018-12-07 10:15:39'},
      {u'count': 1, u'replayCount': 0, u'time': u'2018-12-07 10:17:39'},
      {u'count': 1, u'replayCount': 0, u'time': u'2018-12-07 10:19:39'},
      {u'count': 1, u'replayCount': 0, u'time': u'2018-12-07 10:21:39'},
      {u'count': 1, u'replayCount': 0, u'time': u'2018-12-07 10:23:39'},
      {u'count': 1, u'replayCount': 0, u'time': u'2018-12-07 11:55:39'},
      {u'count': 1, u'replayCount': 0, u'time': u'2018-12-07 11:57:39'}],
     u'count': 14,
     u'pageIndex': 1,
     u'result': u'OK',
     u'roomId': u'06B80689C1653A459C33DC5901307461'}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.statis_connections(roomid, starttime, endtime)
    return response


def statis_useraction(roomid, starttime, endtime):
    '''
    获取直播间连接数
    response
    {u'result': u'OK',
     u'roomId': u'06B80689C1653A459C33DC5901307461',
     u'userActions': [{u'enterTime': u'2018-12-07 10:05:05',
       u'leaveTime': u'2018-12-07 10:05:21',
       u'userCustomInfo': u'',
       u'userId': u'e8b9d06ccc4048959ae5f415dd6ee36a',
       u'userIp': u'182.46.3.164',
       u'userIpArea': u'\u4e2d\u56fd\t\u5c71\u4e1c\t\u6f4d\u574a\t',
       u'userName': u'xxx',
       u'userPlatform': 0}]}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.statis_useraction(roomid, starttime, endtime)
    return response

def statis_userview(liveid):
    '''
    获取观看直播的统计信息
    response
    # 统计未完成的response
    {u'liveId': u'D95AD073F20E70FA', u'result': u'OK', u'status': 0}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.statis_userview(liveid)
    return response


def statis_replay_useraction(recordid, pagenum=50, pageindex=1):
    '''
    获取单个直播回放的观看统计信息
    response
    {u'count': 1,
     u'pageIndex': 1,
     u'recordId': u'C029B2B66ECAD010',
     u'result': u'OK',
     u'userActions': [{u'enterTime': u'2018-12-07 12:41:37.0',
       u'leaveTime': u'2018-12-07 12:41:41.0',
       u'userId': u'250cad29086a405891b29df82e7fe040',
       u'userIp': u'182.46.3.164',
       u'userName': u'182.46.3.164, 47.110.176.158'}]}

    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.statis_replay_useraction(recordid, pagenum=pagenum, pageindex=pageindex)
    return response


def statis_replay(starttime, endtime, pagenum=50, pageindex=1):
    '''
    获取所有直播回放的观看统计信息
    response
    {u'count': 3,
     u'pageIndex': 1,
     u'result': u'OK',
     u'userActions': [{u'enterTime': u'2018-12-06 17:28:11.0',
       u'leaveTime': u'2018-12-06 17:28:13.0',
       u'recordId': u'0AEA0E1676B0727B',
       u'roomId': u'C9C251783586DB859C33DC5901307461',
       u'userId': u'6504489b6dea4d508964f47d5a254f8b',
       u'userIp': u'182.46.3.164',
       u'userName': u'182.46.3.164, 47.110.176.193'}]}
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.statis_replay(starttime, endtime, pagenum=pagenum, pageindex=pageindex)
    return response


def get_auto_login_url(roomid):
    '''获取直播间免密码登录url'''
    live_api = LiveAPI(APIKEY)
    response = live_api.room_code(roomid)
    assistant_login_url = response['assistantLoginUrl']
    client_login_url = response['clientLoginUrl']
    view_url = response['viewUrl']
    name = 'test'
    token = 'test'
    publisherpass = 'tcctest'
    assistantpass = 'acctest'
    assistant_auto_login_url = live_api.get_auto_login_url(assistant_login_url, name, assistantpass, login_type=constants.LiveAutoLoginType.assistant.value)
    client_auto_login_url = live_api.get_auto_login_url(client_login_url, name, publisherpass, login_type=constants.LiveAutoLoginType.lecturer.value)
    user_auto_login_url = live_api.get_auto_login_url(view_url, name, token, login_type=constants.LiveAutoLoginType.user.value)
    data = {
        'assistant_auto_login_url': assistant_auto_login_url,
        'client_auto_login_url': client_auto_login_url,
        'user_auto_login_url': user_auto_login_url,
    }
    return data


def viewtemplate_info():
    '''
    获取直播间模板信息, 看起来是固定的
    视频 1
    视频，聊天，问答 2
    视频，聊天 3
    视频，文档，聊天 4
    视频，文档，聊天，问答 5
    视频，问答 6
    '''
    live_api = LiveAPI(APIKEY)
    response = live_api.viewtemplate_info(userid)
    return response
