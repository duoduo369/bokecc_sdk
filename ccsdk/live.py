# -*- coding: utf-8 -*-
'''
直播类接口
https://doc.bokecc.com/live/dev/liveapi/
版本: 2.3.1
日期: 2018-11-23
'''
from __future__ import absolute_import

import logging
import requests
from . import constants
from . import exceptions
from .utils import THQS


class LiveAPI(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.thqs = THQS(api_key)

    def get_url(self, path):
        api_prefix = 'http://api.csslcloud.net/api/'
        return '{}{}'.format(api_prefix, path)

    def request(self, url, params, method='get', timeout=3):
        if not isinstance(params, dict):
            raise exceptions.CCSDKInvalidParamException()
        # TODO: 目前看到的都是get接口
        if method != 'get':
            raise NotImplementedError()
        url = '{}?{}'.format(url, self.thqs.encrypt(params))
        response = requests.get(url, timeout=timeout)
        data = response.json()
        if data['result'] != 'OK':
            logging.error('[CCSDK] live: %s', data['reason'])
            raise exceptions.CCServerException(data['reason'])
        return data

    def room_create(self, userid, name, desc, templatetype, authtype,
            publisherpass, assistantpass, playpass=None, checkurl=None,
            barrage=0, foreignpublish=0, openlowdelaymode=0, showusercount=1,
            openhostmode=0, warmvideoid='', livestarttime='',
            playerbackgroundhint='', manuallyrecordmode=0,
            clientdocpermissions=0, repeatedloginsetting=0, maxaudiencenum=0,
            documentdisplaymode=1, openlivecountdown=0, showlectueronlinenum=1,
            showassistonlinenum=1):
        '''
        创建直播间
        http://api.csslcloud.net/api/room/create
        userid  CC账户ID
        name    直播间名称
        desc    直播间描述
        templatetype    直播模板类型，请求模板信息接口可获得模板类型的详细信息。
        authtype    验证方式，0：接口验证，需要填写下面的checkurl；1：密码验证，需要填写下面的playpass；2：免密码验证
        publisherpass   推流端密码，即讲师密码
        assistantpass   助教端密码
        playpass    播放端密码  可选
        checkurl    验证地址    可选
        barrage 是否开启弹幕。0：不开启；1：开启    可选，默认为0
        foreignpublish  是否开启第三方推流。0：不开启；1：开启  可选，默认为0
        openlowdelaymode    开启直播低延时模式。0为关闭；1为开启    可选，默认为关闭
        showusercount   在页面显示当前在线人数。0表示不显示；1表示显示  可选，默认显示当前人数，模板一暂不支持此设置
        openhostmode    开启主持人模式，"0"表示不开启；"1"表示开启  可选，默认不开启，开通主持人模式权限后方可使用
        warmvideoid 插播暖场视频，填写同一账号下云点播视频vid   可选，默认关闭；参数值为空，表示关闭
        livestarttime   直播开始时间；格式：yyyy-MM-dd HH:mm:ss 可选，默认为空
        playerbackgroundhint    播放器提示语。未直播时播放器将显示该提示语  可选，最多15个字符
        manuallyrecordmode  手动录制模式。0：关闭；1：开启  可选，默认关闭
        clientdocpermissions    讲师文档权限。0：关闭；1：开启  可选，默认关闭；
        repeatedloginsetting    重复登录设置；0：允许后进入者登录;1:禁止后进入者登录，对讲师端和观看端生效  可选，默认0
        maxaudiencenum  直播间并发人数上限  可选，默认为0，表示不做限制
        documentdisplaymode 文档显示模式。1：适合窗口;2:适合宽度    可选，适合窗口
        openlivecountdown   倒计时功能。0：关闭；1：开启    可选，默认关闭
        showlectueronlinenum    讲师端显示在线人数。0：不显示；1：显示  可选，默认显示
        showassistonlinenum    助教主持人端显示在线人数。0：不显示；1：显示可选，默认显示
        '''
        url = self.get_url('room/create')
        authtype = constants.LiveAuthType(authtype).value
        templatetype = constants.LiveTemplateType(templatetype).value
        params = {
            'userid': userid, 'name': name, 'desc': desc, 'templatetype': templatetype,
            'authtype': authtype, 'publisherpass': publisherpass, 'assistantpass': assistantpass,
            'playpass': playpass, 'checkurl': checkurl, 'barrage': barrage,
            'foreignpublish': foreignpublish, 'openlowdelaymode': openlowdelaymode,
            'showusercount': showusercount, 'openhostmode': openhostmode,
            'warmvideoid': warmvideoid, 'livestarttime': livestarttime,
            'playerbackgroundhint': playerbackgroundhint, 'manuallyrecordmode': manuallyrecordmode,
            'clientdocpermissions': clientdocpermissions, 'repeatedloginsetting': repeatedloginsetting,
            'maxaudiencenum': maxaudiencenum, 'documentdisplaymode': documentdisplaymode,
            'openlivecountdown': openlivecountdown, 'showlectueronlinenum': showlectueronlinenum,
            'showassistonlinenum': showassistonlinenum
        }
        response = self.request(url, params, method='get')
        return response

    def viewtemplate_info(self, userid):
        url = self.get_url('viewtemplate/info')
        params = {'userid': userid}
        response = self.request(url, params, method='get')
        return response
