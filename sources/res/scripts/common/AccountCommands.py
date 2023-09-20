from streamIDs import STREAM_ID_ACCOUNT_CMDS_MIN, STREAM_ID_ACCOUNT_CMDS_MAX
RES_FAILURE = -1
RES_WRONG_ARGS = -2
RES_NON_PLAYER = -3
RES_SHOP_DESYNC = -4
RES_COOLDOWN = -5
RES_HIDDEN_DOSSIER = -6
RES_CENTER_DISCONNECTED = -7
RES_NOT_AVAILABLE = -10
RES_BOOTCAMP_DISABLED = -11
RES_BOOTCAMP_ALREADY_RUNNING = -12
RES_DISABLED = -13
RES_SUCCESS = 0
RES_STREAM = 1
RES_CACHE = 2

def isCodeValid(code):
    return code >= 0


CMD_RESERVED = 0
CMD_SYNC_DATA = 100
CMD_EQUIP = 101
CMD_EQUIP_OPTDEV = 102
CMD_EQUIP_SHELLS = 103
CMD_EQUIP_EQS = 104
CMD_EQUIP_TMAN = 105
CMD_REPAIR = 106
CMD_VEH_SETTINGS = 107
CMD_SET_AND_FILL_LAYOUTS = 108
CMD_SELL_C11N_ITEMS = 117
CMD_BUY_C11N_ITEMS = 118
CMD_VEH_APPLY_OUTFIT = 119
CMD_RESET_C11N_ITEMS_NOVELTY = 120
CMD_SET_ACTIVE_VEH_SEASON = 121
CMD_SELECT_POTAPOV_QUESTS = 124
CMD_GET_POTAPOV_QUEST_REWARD = 125
CMD_BUY_POTAPOV_QUEST_TILE = 126
CMD_BUY_POTAPOV_QUEST_SLOT = 127
CMD_RESET_POTAPOV_QUESTS = 128
CMD_PAUSE_POTAPOV_QUESTS = 129
CMD_TMAN_ADD_SKILL = 151
CMD_TMAN_DROP_SKILLS = 152
CMD_TMAN_RESPEC = 153
CMD_TMAN_PASSPORT = 154
CMD_TRAINING_TMAN = 155
CMD_TMAN_MULTI_RESPEC = 156
CMD_RETURN_CREW = 157
CMD_TMAN_CHANGE_ROLE = 158
CMD_TMAN_RECRUIT = 159
CMD_TMAN_EQUIP_CREW_SKIN = 160
CMD_TMAN_UNEQUIP_CREW_SKIN = 161
CMD_LEARN_CREW_BOOK = 162
CMD_LEARN_TMAN_FREE_SKILL = 163
CMD_EARN_ALL_SKILLS = 164
CMD_UNLOCK = 201
CMD_EXCHANGE = 202
CMD_FREE_XP_CONV = 203
CMD_PREMIUM = 204
CMD_BUY_SLOT = 205
CMD_BUY_BERTHS = 206
CMD_VEHICLE_CHANGE_NATION = 207
CMD_BLUEPRINTS_CONVERT_SALE = 208
CMD_SYNC_SHOP = 300
CMD_BUY_VEHICLE = 301
CMD_BUY_ITEM = 302
CMD_BUY_TMAN = 303
CMD_SELL_VEHICLE = 304
CMD_SELL_ITEM = 305
CMD_DISMISS_TMAN = 306
CMD_VERIFY_FIN_PSWD = 307
CMD_BUY_AND_EQUIP_ITEM = 308
CMD_BUY_AND_EQUIP_TMAN = 309
CMD_SELL_MULTIPLE_ITEMS = 310
CMD_PRB_JOIN = 400
CMD_PRB_LEAVE = 401
CMD_PRB_READY = 402
CMD_PRB_NOT_READY = 403
CMD_PRB_ASSIGN = 404
CMD_PRB_SWAP_TEAM = 405
CMD_PRB_CH_ARENA = 406
CMD_PRB_CH_ROUND = 407
CMD_PRB_OPEN = 408
CMD_PRB_CH_COMMENT = 409
CMD_PRB_CH_ARENAVOIP = 410
CMD_PRB_TEAM_READY = 411
CMD_PRB_TEAM_NOT_READY = 412
CMD_PRB_KICK = 414
CMD_PRB_CH_GAMEPLAYSMASK = 416
CMD_PRB_ACCEPT_INVITE = 417
CMD_PRB_DECLINE_INVITE = 418
CMD_PRB_SWAP_TEAMS_WITHIN_GROUP = 419
CMD_PRB_SWAP_GROUPS_WITHIN_TEAM = 420
CMD_REQ_SERVER_STATS = 501
CMD_REQ_QUEUE_INFO = 502
CMD_REQ_PLAYER_INFO = 503
CMD_REQ_ACCOUNT_DOSSIER = 504
CMD_REQ_VEHICLE_DOSSIER = 505
CMD_REQ_PLAYER_CLAN_INFO = 506
CMD_REQ_PLAYER_GLOBAL_RATING = 507
CMD_REQ_PLAYERS_GLOBAL_RATING = 508
CMD_REQ_PREBATTLES = 520
CMD_REQ_PREBATTLES_BY_CREATOR = 521
CMD_REQ_PREBATTLE_ROSTER = 523
CMD_SYNC_DOSSIERS = 600
CMD_ENQUEUE_IN_BATTLE_QUEUE = 700
CMD_DEQUEUE_FROM_BATTLE_QUEUE = 701
CMD_ENQUEUE_BOOTCAMP = 718
CMD_DEQUEUE_BOOTCAMP = 719
CMD_REQUEST_BOOTCAMP_QUIT = 720
CMD_REQUEST_BOOTCAMP_START = 721
CMD_GAMEPLAY_CHOICE = 722
CMD_ENQUEUE_MAPS_TRAINING = 723
CMD_DEQUEUE_MAPS_TRAINING = 724
CMD_REQ_MAPS_TRAINING_INITIAL_CONFIGURATION = 725
CMD_SELECT_BADGES = 800
CMD_ENQUEUE_EPIC = 900
CMD_DEQUEUE_EPIC = 901
CMD_FORCE_EPIC_DEV_START = 903
CMD_UPDATE_SELECTED_EPIC_META_ABILITY = 905
CMD_INCREASE_EPIC_META_ABILITY = 906
CMD_RESET_EPIC_META_GAME = 907
CMD_GET_FREE_EPIC_DISCOUNT = 910
CMD_ENQUEUE_BATTLE_ROYALE = 913
CMD_DEQUEUE_BATTLE_ROYALE = 914
CMD_SET_LANGUAGE = 1000
CMD_MAKE_DENUNCIATION = 1100
CMD_BAN_UNBAN_USER = 1400
CMD_REQ_BATTLE_RESULTS = 1500
CMD_BATTLE_RESULTS_RECEIVED = 1501
CMD_ADD_INT_USER_SETTINGS = 1600
CMD_DEL_INT_USER_SETTINGS = 1601
CMD_GET_AVATAR_SYNC = 1602
CMD_LOG_CLIENT_UX_EVENTS = 1603
CMD_LOG_CLIENT_XMPP_EVENTS = 1604
CMD_UPDATE_USER_RELATIONS = 1605
CMD_RANK_UPDATED = 1606
CMD_NOTIFICATION_REPLY = 1800
CMD_SET_DOSSIER_FIELD = 2000
CMD_SET_MONEY = 10001
CMD_ADD_XP = 10002
CMD_ADD_TMAN_XP = 10003
CMD_UNLOCK_ALL = 10004
CMD_SET_RANKED_INFO = 10005
CMD_RESET_INVENTORY_LOCKS = 10006
CMD_FORCE_QUEUE = 10008
CMD_INVITATION_ACCEPT = 10010
CMD_INVITATION_DECLINE = 10011
CMD_INVITATION_SEND = 10012
CMD_ACTIVATE_GOODIE = 10013
CMD_BUY_GOODIE = 10014
CMD_TMAN_RESTORE = 10015
CMD_VEHICLE_TRADE_IN = 10016
CMD_QUERY_BALANCE_INFO = 10017
CMD_RUN_QUEST = 10018
CMD_PAWN_FREE_AWARD_LIST = 10019
CMD_ADD_FREE_AWARD_LISTS = 10020
CMD_DRAW_FREE_AWARD_LISTS = 10021
CMD_COMPLETE_PERSONAL_MISSION = 10022
CMD_GET_TANKMAN_GIFT = 10023
CMD_ADD_TOKENS = 10024
CMD_DRAW_TOKENS = 10025
CMD_CHOOSE_QUEST_REWARD = 10026
CMD_PROCESS_RECEIPT_LIST = 10027
CMD_LOOTBOX_OPEN = 10028
CMD_LOOTBOX_GETINFO = 10029
CMD_ADD_GOODIE = 10030
CMD_BPF_CONVERT_FRAGMENTS = 1024
CMD_BPF_ADD_FRAGMENTS_DEV = 1025
CMD_BPF_MARK_FRAGMENTS_SEEN = 1026
CMD_BPF_STAMP = 1027
CMD_WISHLIST_GET_DEV = 1028
CMD_TMAN_ADD_CREW_SKIN = 10031
CMD_APPLY_ADDITIONAL_XP = 10032
CMD_SET_MAPS_BLACK_LIST = 10033
CMD_SET_PREMIUM = 10034
CMD_RESET_SESSION_STAT = 10035
CMD_ADD_CREW_BOOK = 10036
CMD_GET_SINGLE_TOKEN = 10037
CMD_SET_ANONYMIZER_STATE = 10038
CMD_SET_BATTLE_NAMES = 10039
CMD_FLUSH_ARENA_RELATIONS = 10040
CMD_EQUIP_ENHANCEMENT = 10041
CMD_REROLL_DAILY_QUEST = 10042
CMD_REROLL_DAILY_QUEST_DEV = 10043
CMD_RESET_REROLL_TIMEOUT = 10044
CMD_COMPLETE_DAILY_QUEST = 10045
CMD_SET_EPIC_REWARD_TOKENS = 10046
CMD_RESET_BONUS_QUEST = 10047
CMD_OBTAIN_ALL = 10048
CMD_OBTAIN_VEHICLE = 10049
CMD_UPGRADE_OPTDEV = 10050
CMD_BUY_BATTLE_PASS = 10051
CMD_BUY_BATTLE_PASS_LEVELS = 10052
CMD_SET_BATTLE_PASS_POINTS = 10053
CMD_ADD_PERK_TO_BATTLE = 10055
CMD_RESET_PERK_FOR_BATTLE = 10056
CMD_RECEIVE_OFFER_GIFT = 10057
CMD_SET_OFFER_BANNER_SEEN = 10058
CMD_DISMOUNT_ENHANCEMENT = 10059
CMD_EQUIP_OPT_DEVS_SEQUENCE = 10060
CMD_UPDATE_PLAYER_DOG_TAG = 10062
CMD_UNLOCK_DOG_TAG_COMPONENTS_DEV = 10063
CMD_LOCK_DOG_TAG_COMPONENTS_DEV = 10064
CMD_UNLOCK_ALL_DOG_TAG_COMPONENTS_DEV = 10065
CMD_SET_DOG_TAG_COMPONENT_PROGRESS_DEV = 10066
CMD_UPDATE_SETTING = 10067
CMD_CHANGE_EVENT_ENQUEUE_DATA = 10068
CMD_WATCH_REPLAY = 11000
CMD_BUY_PROGRESS_LVL_C11N_ITEMS = 10071
CMD_SWITCH_LAYOUT = 10075
CMD_VPP_UNLOCK_ITEMS = 10076
CMD_VPP_SELECT_PAIR = 10077
CMD_VPP_DISCARD_PAIRS = 10078
CMD_VPP_UNLOCK_TREE = 10079
CMD_SET_CUSTOM_ROLE_SLOT = 10080
CMD_TOGGLE_SWITCH_LAYOUT = 10081
CMD_TOGGLE_RENEWABLE_SUB_DEV = 10082
CMD_IDLE_CREW_XP_SELECT_VEHICLE = 10083
CMD_SET_RESERVES_PIGGY_BANK_DEV = 10084
CMD_ACTIVATE_RENEWABLE_SUB_DEV = 10085
CMD_WOT_PLUS_NEW_GAME_DAY = 10086
CMD_SMASH_PIGGY_BANK_DEV = 10088
CMD_SYNC_GIFTS = 10089
CMD_TELECOM_RENTALS_VEHICLE_RENT_AMOUNT = 10091
CMD_TELECOM_RENTALS_TOGGLE_ACTIVE = 10092
CMD_TELECOM_RENTALS_RENT_TANK = 10093
CMD_RECEIVE_OFFER_GIFT_MULTIPLE = 10095
CMD_SET_BATTLE_PASS_CHAPTER = 10096
CMD_TRADE_IN_ADD_TOKEN = 10097
CMD_TRADE_IN_REMOVE_TOKEN = 10098
CMD_UPDATE_SELECTED_EPIC_META_ABILITY_VEHICLES = 10099
CMD_SHOW_FRONTLINE_SYS_MSG = 10100
CMD_FRONTLINE_UNLOCK_RESERVES = 10101
CMD_RESOURCE_WELL_PUT = 10102
CMD_RESOURCE_WELL_TAKE = 10103
CMD_REMOVE_GOODIES_DEV = 10104
CMD_ACTIVATE_CLAN_BOOSTER = 10105
CMD_DEACTIVATE_CLAN_BOOSTERS = 10106
CMD_CONVERT_OBSOLETE_SKILLS = 10107
CMD_ADD_EQUIPMENT = 10108
CMD_SET_ACCOUNT_WTR = 10109
CMD_TURNOFF_WINBACK_BATTLES = 10110
CMD_SET_ACHIEVEMENTS20_LAYOUT = 10111
CMD_GIVE_ATTENDANCE_REWARD_DEV = 10112
CMD_COMPLETE_QUESTS_DEV = 10113
CMD_SET_ACCOUNT_RBR = 10114
CMD_LOOTBOX_REROLL = 10115
CMD_LOOTBOX_REROLL_RECORDS = 10116
PLAYER_CMD_NAMES = dict([ (v, k) for k, v in globals().items() if k.startswith('CMD_') ])
KEYS_ARE_UNIQUE = len(PLAYER_CMD_NAMES) == len(set(key for key in globals() if key.startswith('CMD_')))

class LOCK_REASON:
    NONE = 0
    ON_ARENA = 1
    IN_QUEUE = 2
    PREBATTLE = 4
    UNIT = 8
    BREAKER = 16
    ANY_MASK = 255


LOCK_REASON_NAMES = dict([ (v, k) for k, v in LOCK_REASON.__dict__.items() if not k.startswith('__') ])

class BUY_VEHICLE_FLAG:
    NONE = 0
    CREW = 1
    SHELLS = 16


class VEHICLE_SETTINGS_FLAG:
    NONE = 0
    XP_TO_TMAN = 1
    AUTO_REPAIR = 2
    AUTO_LOAD = 4
    AUTO_EQUIP = 8
    GROUP_0 = 16
    ORIGINAL_CREW = 32
    NO_BATTLE = 64
    AUTO_EQUIP_BOOSTER = 128
    AUTO_RENT_CUSTOMIZATION = 256


class VEHICLE_EXTRA_SETTING_FLAG:
    NONE = 0
    NOT_ACTIVE_IN_NATION_GROUP = 1
    WIPE_MASK = NOT_ACTIVE_IN_NATION_GROUP


REQUEST_ID_PREBATTLES = STREAM_ID_ACCOUNT_CMDS_MIN
REQUEST_ID_PREBATTLE_ROSTER = STREAM_ID_ACCOUNT_CMDS_MIN + 1
REQUEST_ID_NO_RESPONSE = STREAM_ID_ACCOUNT_CMDS_MIN + 2
REQUEST_ID_NON_CLIENT = STREAM_ID_ACCOUNT_CMDS_MIN + 3
REQUEST_ID_UNRESERVED_MIN = STREAM_ID_ACCOUNT_CMDS_MIN + 20
REQUEST_ID_UNRESERVED_MAX = STREAM_ID_ACCOUNT_CMDS_MAX