from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(120111)

    shared = _shared(120112)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(120114)
    ExtraVideo = DynAccessor(120115)
    Intro = DynAccessor(120116)
    ChapterChoice = DynAccessor(120117)
    Progression = DynAccessor(120118)
    PostProgression = DynAccessor(120119)
    BuyPass = DynAccessor(120120)
    BuyPassConfirm = DynAccessor(120121)
    BuyPassRewards = DynAccessor(120122)
    BuyLevels = DynAccessor(120123)
    BuyLevelsRewards = DynAccessor(120124)
    HolidayFinal = DynAccessor(120125)
    FinalRewardPreview = DynAccessor(120126)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(120128)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(120129)
        Vehicle = DynAccessor(120130)

    contextMenu = _contextMenu(120131)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(120133)
    UserMissions = DynAccessor(120134)
    VehiclesInventory = DynAccessor(120135)
    VehiclesFilter = DynAccessor(120136)
    AlertMessage = DynAccessor(120137)
    Header = DynAccessor(120138)
    LoadoutPanelContainer = DynAccessor(120139)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(120140)
        EventShop = DynAccessor(120141)

    hangarWidget = _hangarWidget(120142)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(120143)
        Commander = DynAccessor(120144)

    loadoutPanelContainer = _loadoutPanelContainer(120145)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(120147)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(120148)

    contextMenu = _contextMenu(120149)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(120150)
        Wulf = DynAccessor(120151)
        Param = DynAccessor(120152)

    tooltip = _tooltip(120153)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(120154)

    popOver = _popOver(120155)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(120156)

    shared = _shared(120157)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(120159)
        Schedule = DynAccessor(120160)
        SeasonModifier = DynAccessor(120161)
        RoleSkillSlot = DynAccessor(120162)
        UserMissions = DynAccessor(120163)
        EntryPoint = DynAccessor(120164)
        WeeklyQuestsWidget = DynAccessor(120165)

    shared = _shared(120166)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(120168)
        SeasonModifier = DynAccessor(120169)
        RoleSkillSlot = DynAccessor(120170)
        UserMissions = DynAccessor(120171)
        EntryPoint = DynAccessor(120172)
        Quests = DynAccessor(120173)

    shared = _shared(120174)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(120176)

    loadout = _loadout(120177)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(120178)
        AlertMessage = DynAccessor(120179)

    shared = _shared(120180)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(120182)
        ProgressionEntryPoint = DynAccessor(120183)

    shared = _shared(120184)


class halloween(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(120186)
        AmmunitionPanel = DynAccessor(120187)
        Difficulty = DynAccessor(120188)
        MoneyBalance = DynAccessor(120189)
        TeamStats = DynAccessor(120190)
        Meta = DynAccessor(120191)
        Keys = DynAccessor(120192)
        Quests = DynAccessor(120193)
        RewardPath = DynAccessor(120194)
        Shop = DynAccessor(120195)
        Gsw = DynAccessor(120196)
        Switcher = DynAccessor(120197)
        CrewMembers = DynAccessor(120198)

    shared = _shared(120199)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(120201)
        VehiclesStatistics = DynAccessor(120202)
        Consumables = DynAccessor(120203)
        Equipments = DynAccessor(120204)
        Instructions = DynAccessor(120205)
        Shells = DynAccessor(120206)
        Loadout = DynAccessor(120207)
        Crew = DynAccessor(120208)
        VehicleParams = DynAccessor(120209)
        CurrentVehicle = DynAccessor(120210)
        VehiclesInventory = DynAccessor(120211)
        MainMenu = DynAccessor(120212)
        VehicleMenu = DynAccessor(120213)
        LootboxEntryPoint = DynAccessor(120214)
        VehicleFilters = DynAccessor(120215)
        VehiclePlaylists = DynAccessor(120216)
        Teaser = DynAccessor(120217)
        OptionalDevicesAssistant = DynAccessor(120218)
        SpaceInteraction = DynAccessor(120219)
        HeroTank = DynAccessor(120220)
        UserMissions = DynAccessor(120221)
        ModeState = DynAccessor(120222)

    shared = _shared(120223)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(120225)
        AmmunitionPanel = DynAccessor(120226)
        Difficulty = DynAccessor(120227)
        MoneyBalance = DynAccessor(120228)
        TeamStats = DynAccessor(120229)
        Meta = DynAccessor(120230)
        Keys = DynAccessor(120231)
        Quests = DynAccessor(120232)
        RewardPath = DynAccessor(120233)
        Shop = DynAccessor(120234)
        Gsw = DynAccessor(120235)
        Switcher = DynAccessor(120236)

    shared = _shared(120237)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(120239)
        ContactsList = DynAccessor(120240)
        SessionStats = DynAccessor(120241)
        VehicleCompare = DynAccessor(120242)
        NotificationsCenter = DynAccessor(120243)
        Chats = DynAccessor(120244)
        ReferralProgram = DynAccessor(120245)
        ServerInfo = DynAccessor(120246)

    default = _default(120247)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(120249)
        NavigationBar = DynAccessor(120250)
        Prebattle = DynAccessor(120251)
        Wallet = DynAccessor(120252)
        AccountDashboard = DynAccessor(120253)
        HeaderState = DynAccessor(120254)
        UserAccount = DynAccessor(120255)
        ReservesEntryPoint = DynAccessor(120256)
        PremShop = DynAccessor(120257)

    default = _default(120258)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(120260)
            Instructions = DynAccessor(120261)
            Shells = DynAccessor(120262)
            Consumables = DynAccessor(120263)

        Loadout = _Loadout(120264)
        Vehicles = DynAccessor(120265)

    Hangar = _Hangar(120266)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(120268)
        Events = DynAccessor(120269)
        Quests = DynAccessor(120270)
        EventMainInfoTip = DynAccessor(120271)

    hangarWidget = _hangarWidget(120272)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(120273)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(120274)
                DailyBlock = DynAccessor(120275)
                PremiumBlock = DynAccessor(120276)
                RewardProgressBlock = DynAccessor(120277)

            DailyMissionsSection = _DailyMissionsSection(120278)
            WeeklyMissions = DynAccessor(120279)
            PersonalMissions = DynAccessor(120280)

        basicMissions = _basicMissions(120281)

    hub = _hub(120282)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(120284)
        Wallet = DynAccessor(120285)

    default = _default(120286)


class Aliases(DynAccessor):
    __slots__ = ()
    battle_modifiers = battle_modifiers()
    battle_pass = battle_pass()
    battle_result = battle_result()
    battle_royale = battle_royale()
    common = common()
    comp7 = comp7()
    comp7_light = comp7_light()
    frontline = frontline()
    fun_random = fun_random()
    halloween = halloween()
    hangar = hangar()
    last_stand = last_stand()
    lobby_footer = lobby_footer()
    lobby_header = lobby_header()
    states = states()
    user_missions = user_missions()
    vehicle_hub = vehicle_hub()