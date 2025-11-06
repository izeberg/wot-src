from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(119984)

    shared = _shared(119985)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(119987)
    ExtraVideo = DynAccessor(119988)
    Intro = DynAccessor(119989)
    ChapterChoice = DynAccessor(119990)
    Progression = DynAccessor(119991)
    PostProgression = DynAccessor(119992)
    BuyPass = DynAccessor(119993)
    BuyPassConfirm = DynAccessor(119994)
    BuyPassRewards = DynAccessor(119995)
    BuyLevels = DynAccessor(119996)
    BuyLevelsRewards = DynAccessor(119997)
    HolidayFinal = DynAccessor(119998)
    FinalRewardPreview = DynAccessor(119999)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(120001)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(120002)
        Vehicle = DynAccessor(120003)

    contextMenu = _contextMenu(120004)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(120006)
    UserMissions = DynAccessor(120007)
    VehiclesInventory = DynAccessor(120008)
    VehiclesFilter = DynAccessor(120009)
    AlertMessage = DynAccessor(120010)
    Header = DynAccessor(120011)
    LoadoutPanelContainer = DynAccessor(120012)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(120013)
        EventShop = DynAccessor(120014)

    hangarWidget = _hangarWidget(120015)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(120016)
        Commander = DynAccessor(120017)

    loadoutPanelContainer = _loadoutPanelContainer(120018)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(120020)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(120021)

    contextMenu = _contextMenu(120022)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(120023)
        Wulf = DynAccessor(120024)
        Param = DynAccessor(120025)

    tooltip = _tooltip(120026)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(120027)

    popOver = _popOver(120028)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(120029)

    shared = _shared(120030)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(120032)
        Schedule = DynAccessor(120033)
        SeasonModifier = DynAccessor(120034)
        RoleSkillSlot = DynAccessor(120035)
        UserMissions = DynAccessor(120036)
        EntryPoint = DynAccessor(120037)
        WeeklyQuestsWidget = DynAccessor(120038)

    shared = _shared(120039)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(120041)
        SeasonModifier = DynAccessor(120042)
        RoleSkillSlot = DynAccessor(120043)
        UserMissions = DynAccessor(120044)
        EntryPoint = DynAccessor(120045)
        Quests = DynAccessor(120046)

    shared = _shared(120047)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(120049)

    loadout = _loadout(120050)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(120051)
        AlertMessage = DynAccessor(120052)

    shared = _shared(120053)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(120055)
        ProgressionEntryPoint = DynAccessor(120056)

    shared = _shared(120057)


class halloween(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(120059)
        AmmunitionPanel = DynAccessor(120060)
        Difficulty = DynAccessor(120061)
        MoneyBalance = DynAccessor(120062)
        TeamStats = DynAccessor(120063)
        Meta = DynAccessor(120064)
        Keys = DynAccessor(120065)
        Quests = DynAccessor(120066)
        RewardPath = DynAccessor(120067)
        Shop = DynAccessor(120068)
        Gsw = DynAccessor(120069)
        Switcher = DynAccessor(120070)
        CrewMembers = DynAccessor(120071)

    shared = _shared(120072)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(120074)
        VehiclesStatistics = DynAccessor(120075)
        Consumables = DynAccessor(120076)
        Equipments = DynAccessor(120077)
        Instructions = DynAccessor(120078)
        Shells = DynAccessor(120079)
        Loadout = DynAccessor(120080)
        Crew = DynAccessor(120081)
        VehicleParams = DynAccessor(120082)
        CurrentVehicle = DynAccessor(120083)
        VehiclesInventory = DynAccessor(120084)
        MainMenu = DynAccessor(120085)
        VehicleMenu = DynAccessor(120086)
        LootboxEntryPoint = DynAccessor(120087)
        VehicleFilters = DynAccessor(120088)
        VehiclePlaylists = DynAccessor(120089)
        Teaser = DynAccessor(120090)
        OptionalDevicesAssistant = DynAccessor(120091)
        SpaceInteraction = DynAccessor(120092)
        HeroTank = DynAccessor(120093)
        UserMissions = DynAccessor(120094)
        ModeState = DynAccessor(120095)

    shared = _shared(120096)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(120098)
        AmmunitionPanel = DynAccessor(120099)
        Difficulty = DynAccessor(120100)
        MoneyBalance = DynAccessor(120101)
        TeamStats = DynAccessor(120102)
        Meta = DynAccessor(120103)
        Keys = DynAccessor(120104)
        Quests = DynAccessor(120105)
        RewardPath = DynAccessor(120106)
        Shop = DynAccessor(120107)
        Gsw = DynAccessor(120108)
        Switcher = DynAccessor(120109)

    shared = _shared(120110)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(120112)
        ContactsList = DynAccessor(120113)
        SessionStats = DynAccessor(120114)
        VehicleCompare = DynAccessor(120115)
        NotificationsCenter = DynAccessor(120116)
        Chats = DynAccessor(120117)
        ReferralProgram = DynAccessor(120118)
        ServerInfo = DynAccessor(120119)

    default = _default(120120)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(120122)
        NavigationBar = DynAccessor(120123)
        Prebattle = DynAccessor(120124)
        Wallet = DynAccessor(120125)
        AccountDashboard = DynAccessor(120126)
        HeaderState = DynAccessor(120127)
        UserAccount = DynAccessor(120128)
        ReservesEntryPoint = DynAccessor(120129)
        PremShop = DynAccessor(120130)

    default = _default(120131)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(120133)
            Instructions = DynAccessor(120134)
            Shells = DynAccessor(120135)
            Consumables = DynAccessor(120136)

        Loadout = _Loadout(120137)
        Vehicles = DynAccessor(120138)

    Hangar = _Hangar(120139)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(120141)
        Events = DynAccessor(120142)
        Quests = DynAccessor(120143)
        EventMainInfoTip = DynAccessor(120144)

    hangarWidget = _hangarWidget(120145)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(120146)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(120147)
                DailyBlock = DynAccessor(120148)
                PremiumBlock = DynAccessor(120149)
                RewardProgressBlock = DynAccessor(120150)

            DailyMissionsSection = _DailyMissionsSection(120151)
            WeeklyMissions = DynAccessor(120152)
            PersonalMissions = DynAccessor(120153)

        basicMissions = _basicMissions(120154)

    hub = _hub(120155)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(120157)
        Wallet = DynAccessor(120158)

    default = _default(120159)


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