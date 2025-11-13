from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(118084)

    shared = _shared(118085)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(118087)
    ExtraVideo = DynAccessor(118088)
    Intro = DynAccessor(118089)
    ChapterChoice = DynAccessor(118090)
    Progression = DynAccessor(118091)
    PostProgression = DynAccessor(118092)
    BuyPass = DynAccessor(118093)
    BuyPassConfirm = DynAccessor(118094)
    BuyPassRewards = DynAccessor(118095)
    BuyLevels = DynAccessor(118096)
    BuyLevelsRewards = DynAccessor(118097)
    HolidayFinal = DynAccessor(118098)
    FinalRewardPreview = DynAccessor(118099)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(118101)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(118102)
        Vehicle = DynAccessor(118103)

    contextMenu = _contextMenu(118104)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(118106)
    UserMissions = DynAccessor(118107)
    VehiclesInventory = DynAccessor(118108)
    VehiclesFilter = DynAccessor(118109)
    AlertMessage = DynAccessor(118110)
    Header = DynAccessor(118111)
    LoadoutPanelContainer = DynAccessor(118112)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(118113)
        EventShop = DynAccessor(118114)

    hangarWidget = _hangarWidget(118115)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(118116)
        Commander = DynAccessor(118117)

    loadoutPanelContainer = _loadoutPanelContainer(118118)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(118120)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(118121)

    contextMenu = _contextMenu(118122)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(118123)
        Wulf = DynAccessor(118124)
        Param = DynAccessor(118125)

    tooltip = _tooltip(118126)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(118127)

    popOver = _popOver(118128)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(118129)

    shared = _shared(118130)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(118132)
        Schedule = DynAccessor(118133)
        SeasonModifier = DynAccessor(118134)
        RoleSkillSlot = DynAccessor(118135)
        UserMissions = DynAccessor(118136)
        EntryPoint = DynAccessor(118137)
        WeeklyQuestsWidget = DynAccessor(118138)

    shared = _shared(118139)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(118141)
        SeasonModifier = DynAccessor(118142)
        RoleSkillSlot = DynAccessor(118143)
        UserMissions = DynAccessor(118144)
        EntryPoint = DynAccessor(118145)
        Quests = DynAccessor(118146)

    shared = _shared(118147)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(118149)

    loadout = _loadout(118150)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(118151)
        AlertMessage = DynAccessor(118152)

    shared = _shared(118153)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(118155)
        ProgressionEntryPoint = DynAccessor(118156)

    shared = _shared(118157)


class halloween(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(118159)
        AmmunitionPanel = DynAccessor(118160)
        Difficulty = DynAccessor(118161)
        MoneyBalance = DynAccessor(118162)
        TeamStats = DynAccessor(118163)
        Meta = DynAccessor(118164)
        Keys = DynAccessor(118165)
        Quests = DynAccessor(118166)
        RewardPath = DynAccessor(118167)
        Shop = DynAccessor(118168)
        Gsw = DynAccessor(118169)
        Switcher = DynAccessor(118170)
        CrewMembers = DynAccessor(118171)

    shared = _shared(118172)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(118174)
        VehiclesStatistics = DynAccessor(118175)
        Consumables = DynAccessor(118176)
        Equipments = DynAccessor(118177)
        Instructions = DynAccessor(118178)
        Shells = DynAccessor(118179)
        Loadout = DynAccessor(118180)
        Crew = DynAccessor(118181)
        VehicleParams = DynAccessor(118182)
        CurrentVehicle = DynAccessor(118183)
        VehiclesInventory = DynAccessor(118184)
        MainMenu = DynAccessor(118185)
        VehicleMenu = DynAccessor(118186)
        LootboxEntryPoint = DynAccessor(118187)
        VehicleFilters = DynAccessor(118188)
        VehiclePlaylists = DynAccessor(118189)
        Teaser = DynAccessor(118190)
        OptionalDevicesAssistant = DynAccessor(118191)
        SpaceInteraction = DynAccessor(118192)
        HeroTank = DynAccessor(118193)
        UserMissions = DynAccessor(118194)
        ModeState = DynAccessor(118195)
        PetEvent = DynAccessor(118196)
        PetObjectTooltip = DynAccessor(118197)
        Settings = DynAccessor(118198)
        KeyBindings = DynAccessor(118199)

    shared = _shared(118200)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(118202)
        AmmunitionPanel = DynAccessor(118203)
        Difficulty = DynAccessor(118204)
        MoneyBalance = DynAccessor(118205)
        TeamStats = DynAccessor(118206)
        Meta = DynAccessor(118207)
        Keys = DynAccessor(118208)
        Quests = DynAccessor(118209)
        RewardPath = DynAccessor(118210)
        Shop = DynAccessor(118211)
        Gsw = DynAccessor(118212)
        Switcher = DynAccessor(118213)

    shared = _shared(118214)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(118216)
        ContactsList = DynAccessor(118217)
        SessionStats = DynAccessor(118218)
        VehicleCompare = DynAccessor(118219)
        NotificationsCenter = DynAccessor(118220)
        Chats = DynAccessor(118221)
        ReferralProgram = DynAccessor(118222)
        ServerInfo = DynAccessor(118223)

    default = _default(118224)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(118226)
        NavigationBar = DynAccessor(118227)
        Prebattle = DynAccessor(118228)
        Wallet = DynAccessor(118229)
        AccountDashboard = DynAccessor(118230)
        HeaderState = DynAccessor(118231)
        UserAccount = DynAccessor(118232)
        ReservesEntryPoint = DynAccessor(118233)
        PremShop = DynAccessor(118234)
        CurrentVehicle = DynAccessor(118235)

    default = _default(118236)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(118238)
            Instructions = DynAccessor(118239)
            Shells = DynAccessor(118240)
            Consumables = DynAccessor(118241)

        Loadout = _Loadout(118242)
        Vehicles = DynAccessor(118243)

    Hangar = _Hangar(118244)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(118246)
        Events = DynAccessor(118247)
        Quests = DynAccessor(118248)
        EventMainInfoTip = DynAccessor(118249)

    hangarWidget = _hangarWidget(118250)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(118251)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(118252)
                DailyBlock = DynAccessor(118253)
                PremiumBlock = DynAccessor(118254)
                RewardProgressBlock = DynAccessor(118255)

            DailyMissionsSection = _DailyMissionsSection(118256)
            WeeklyMissions = DynAccessor(118257)
            PersonalMissions = DynAccessor(118258)

        basicMissions = _basicMissions(118259)

    hub = _hub(118260)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(118262)
        Wallet = DynAccessor(118263)

    default = _default(118264)


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