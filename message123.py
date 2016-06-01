# -*- coding: utf-8 -*-
from wechat_sdk.messages import *

@handle_for_type('text')
class TMessage(TextMessage):
    def __init__(self, message):
        self.get_text = message.pop('Content', '')
        super(TMessage, self).__init__(message)


@handle_for_type('voice')
class VMessage(VoiceMessage):
    def __init__(self, message):
        try:
            self.get_text = message.pop('Recognition', None)
        except KeyError:
            raise ParseError()
        super(VMessage, self).__init__(message)
