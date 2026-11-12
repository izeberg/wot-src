import BigWorld

class AccountNewbieChatLockComponent(BigWorld.StaticScriptComponent):

    @property
    def chatLocked(self):
        from account_helpers.newbie_chat_lock import isNewbieChatLocked
        return isNewbieChatLocked()