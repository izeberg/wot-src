from __future__ import absolute_import
import typing
from external_strings_utils import unicode_from_utf8
from soft_exception import SoftException
from messenger.m_settings import MessengerSettings

class error(SoftException):
    pass


g_settings = MessengerSettings()

def normalizeGroupId(itemId):
    if isinstance(itemId, bytes):
        return unicode_from_utf8(itemId)[1]
    return itemId