# -*- coding: utf-8 -*-
from __future__ import absolute_import

from enum import IntEnum


class LiveAuthType(IntEnum):
    api = 0
    password = 1
    no_password = 2


class LiveTemplateType(IntEnum):
    video = 1 # 视频
    video_chat_qa = 2 # 视频，聊天，问答
    video_chat = 3 # 视频，聊天 3
    video_doc_chat = 4 # 视频，文档，聊天 4
    video_doc_chat_qa = 5 # 视频，文档，聊天，问答 5
    video_qa = 6 # 视频，问答 6


class LiveAutoLoginType(IntEnum):
    user = 1
    assistant = 2
    manage = 3
    lecturer = 4
    no_password = 2
