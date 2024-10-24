from gui.Scaleform.locale.MESSENGER import MESSENGER
from helpers import i18n
from messenger.gui.Scaleform.meta.BaseManageContactViewMeta import BaseManageContactViewMeta
from messenger import normalizeGroupId
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.xmpp.xmpp_constants import CONTACT_LIMIT
from messenger.proto.xmpp.xmpp_string_utils import validateRosterItemGroup
from messenger.storage import storage_getter
from messenger.ext import passCensor

class GroupManageView(BaseManageContactViewMeta):

    def __init__(self):
        super(GroupManageView, self).__init__()
        self._currentName = None
        return

    @proto_getter(PROTO_TYPE.MIGRATION)
    def proto(self):
        return

    @storage_getter('users')
    def usersStorage(self):
        return

    def checkText(self, name):
        name = name.strip()
        if self._currentName != name:
            self._currentName = name
            isAllowedResult, errorMsg = False, ''
            name, error = validateRosterItemGroup(self._currentName)
            if error:
                if self._currentName != '':
                    errorMsg = error.getMessage()
                else:
                    errorMsg = ''
            elif self.usersStorage.isGroupExists(name):
                errorMsg = i18n.makeString(MESSENGER.MESSENGER_CONTACTS_VIEW_ADDUSER_ERROR_GROUPALREADYEXIST)
            else:
                isAllowedResult = True
                self._currentName = name
            self.as_setLabelS(errorMsg)
            self.as_setOkBtnEnabledS(isAllowedResult)

    def _getDefaultInitData(self, mainLbl, btOkLbl, btnCancelLbl, btOkTooltip, btnCancelTooltip):
        defData = super(GroupManageView, self)._getDefaultInitData(mainLbl, btOkLbl, btnCancelLbl, btOkTooltip, btnCancelTooltip)
        defData['inputPrompt'] = i18n.makeString(MESSENGER.MESSENGER_CONTACTS_VIEW_MANAGEGROUP_RENAMEGROUP_SEARCHINPUTPROMPT, symbols=CONTACT_LIMIT.GROUP_MAX_LENGTH)
        defData['groupMaxChars'] = CONTACT_LIMIT.GROUP_MAX_LENGTH
        defData['inputTooltip'] = i18n.makeString(MESSENGER.CONTACTS_MANAGEGROUPVIEW_TOOLTIPS_INPUT, maxChars=CONTACT_LIMIT.GROUP_MAX_LENGTH)
        return defData


class GroupCreateView(GroupManageView):

    def onOk(self, data):
        name = normalizeGroupId(passCensor(data.currValue.strip()))
        resultSuccess = self.proto.contacts.addGroup(name)
        if resultSuccess:
            self.as_closeViewS()

    def _getInitDataObject(self):
        defData = self._getDefaultInitData(MESSENGER.MESSENGER_CONTACTS_VIEW_MANAGEGROUP_CREATEGROUP_MAINLABEL, MESSENGER.MESSENGER_CONTACTS_VIEW_MANAGEGROUP_CREATEGROUP_BTNOK_LABEL, MESSENGER.MESSENGER_CONTACTS_VIEW_MANAGEGROUP_CREATEGROUP_BTNCANCEL_LABEL, MESSENGER.CONTACTS_CREATEGROUPVIEW_TOOLTIPS_BTNS_APPLY, MESSENGER.CONTACTS_CREATEGROUPVIEW_TOOLTIPS_BTNS_CLOSE)
        return defData


class GroupRenameView(GroupManageView):

    def __init__(self):
        super(GroupRenameView, self).__init__()
        self.__isInited = False

    def onOk(self, data):
        name = normalizeGroupId(passCensor(data.currValue.strip()))
        prevName = normalizeGroupId(data.defValue)
        successResult = self.proto.contacts.renameGroup(prevName, name)
        if successResult:
            self.as_closeViewS()

    def _getInitDataObject(self):
        defData = self._getDefaultInitData(MESSENGER.MESSENGER_CONTACTS_VIEW_MANAGEGROUP_RENAMEGROUP_MAINLABEL, MESSENGER.MESSENGER_CONTACTS_VIEW_MANAGEGROUP_RENAMEGROUP_BTNOK_LABEL, MESSENGER.MESSENGER_CONTACTS_VIEW_MANAGEGROUP_RENAMEGROUP_BTNCANCEL_LABEL, MESSENGER.CONTACTS_GROUPRENAMEVIEW_TOOLTIPS_BTNS_APPLY, MESSENGER.CONTACTS_GROUPRENAMEVIEW_TOOLTIPS_BTNS_CLOSE)
        return defData

    def as_setLabelS(self, msg):
        if self.__isInited is False:
            self.__isInited = True
            return None
        else:
            return super(GroupRenameView, self).as_setLabelS(msg)