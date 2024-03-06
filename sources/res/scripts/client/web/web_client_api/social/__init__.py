import BigWorld
from gui.clans.clan_cache import g_clanCache
from gui.shared.view_helpers import UsersInfoHelper
from helpers import isPlayerAccount
from messenger.m_constants import USER_TAG, PROTO_TYPE
from messenger.proto import proto_getter
from messenger.proto.shared_find_criteria import MutualFriendsFindCriteria
from messenger.storage import storage_getter
from web.web_client_api import w2capi, w2c, W2CSchema, Field
from web.web_client_api.common import SPA_ID_TYPES
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

class _OnlineStatus(object):
    OFFLINE = 0
    ONLINE = 1
    BUSY = 2


def getStatuses(users):
    statuses = {}
    for user in users:
        if user.isOnline():
            if USER_TAG.PRESENCE_DND in user.getTags():
                status = _OnlineStatus.BUSY
            else:
                status = _OnlineStatus.ONLINE
        else:
            status = _OnlineStatus.OFFLINE
        statuses[user.getID()] = status

    return statuses


class _PlayerStatusSchema(W2CSchema):
    player_id = Field(required=True, type=SPA_ID_TYPES)


class _PlayersTagsSchema(W2CSchema):
    player_ids = Field(required=True, type=list)


class _AddFriendSchema(W2CSchema):
    player_id = Field(required=True, type=SPA_ID_TYPES)
    name = Field(required=True, type=basestring)


@w2capi(name='social', key='action')
class SocialWebApi(object):
    lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        super(SocialWebApi, self).__init__()
        self.__usersInfoHelper = UsersInfoHelper()

    @storage_getter('users')
    def usersStorage(self):
        return

    @proto_getter(PROTO_TYPE.MIGRATION)
    def proto(self):
        return

    @w2c(W2CSchema, name='friends_status')
    def friendsStatus(self, cmd):
        storage = self.usersStorage
        friends = storage.getList(MutualFriendsFindCriteria())
        return {'action': 'friends_status', 
           'friends_status': getStatuses(friends)}

    @w2c(_PlayerStatusSchema, name='player_status')
    def isPlayerOnline(self, cmd, ctx):
        callback = ctx.get('callback')
        playerId = cmd.player_id

        def isAvailable():
            player = self.__usersInfoHelper.getContact(playerId)
            return {'is_online': player.isOnline() if player is not None else False}

        def onNamesReceivedCallback():
            callback(isAvailable())
            self.__usersInfoHelper.onNamesReceived -= onNamesReceivedCallback

        if not bool(self.__usersInfoHelper.getUserName(playerId)):
            self.__usersInfoHelper.onNamesReceived += onNamesReceivedCallback
            self.__usersInfoHelper.syncUsersInfo()
        else:
            return isAvailable()

    @w2c(W2CSchema, name='get_player_info')
    def getPlayerInfo(self, _):
        if not isPlayerAccount():
            return {}
        name = BigWorld.player().name
        clanInfo = g_clanCache.clanInfo
        if clanInfo and len(clanInfo) > 1:
            clanAbbrev = clanInfo[1]
        else:
            clanAbbrev = ''
        return {'fullName': self.lobbyContext.getPlayerFullName(name, clanInfo=clanInfo), 
           'userName': name, 
           'clanAbbrev': clanAbbrev}

    @w2c(_PlayersTagsSchema, name='get_players_tags')
    def getPlayersTags(self, cmd, ctx):
        callback = ctx.get('callback')
        playerIds = cmd.player_ids

        def playersTags():
            players = (self.__usersInfoHelper.getContact(playerId) for playerId in playerIds)
            return {player.getID():list(player.getTags()) for player in players}

        def onNamesReceivedCallback():
            callback(playersTags())
            self.__usersInfoHelper.onNamesReceived -= onNamesReceivedCallback

        if any(not bool(self.__usersInfoHelper.getUserName(playerId)) for playerId in playerIds):
            self.__usersInfoHelper.onNamesReceived += onNamesReceivedCallback
            self.__usersInfoHelper.syncUsersInfo()
        else:
            return playersTags()

    @w2c(_AddFriendSchema, name='add_friend')
    def addFriend(self, cmd):
        playerId = cmd.player_id
        name = cmd.name
        return self.proto.contacts.addFriend(playerId, name)