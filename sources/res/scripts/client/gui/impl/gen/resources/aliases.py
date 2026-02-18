from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(125095)

    shared = _shared(125096)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(125098)
    ExtraVideo = DynAccessor(125099)
    Intro = DynAccessor(125100)
    ChapterChoice = DynAccessor(125101)
    Progression = DynAccessor(125102)
    PostProgression = DynAccessor(125103)
    BuyPass = DynAccessor(125104)
    BuyPassConfirm = DynAccessor(125105)
    BuyPassRewards = DynAccessor(125106)
    BuyLevels = DynAccessor(125107)
    BuyLevelsRewards = DynAccessor(125108)
    HolidayFinal = DynAccessor(125109)
    FinalRewardPreview = DynAccessor(125110)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(125112)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(125113)
        Vehicle = DynAccessor(125114)

    contextMenu = _contextMenu(125115)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(125117)
        WeeklyMissions = DynAccessor(125118)
        PersonalMissions = DynAccessor(125119)
        BattlePass = DynAccessor(125120)
        Prestige = DynAccessor(125121)
        BattleMatters = DynAccessor(125122)
        ModuleVehicleUnlocks = DynAccessor(125123)
        CommonQuests = DynAccessor(125124)

    progression = _progression(125125)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(125127)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125128)

    contextMenu = _contextMenu(125129)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125130)
        Wulf = DynAccessor(125131)
        Param = DynAccessor(125132)

    tooltip = _tooltip(125133)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125134)

    popOver = _popOver(125135)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(125136)

    shared = _shared(125137)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(125139)
        VehiclesStatistics = DynAccessor(125140)
        Consumables = DynAccessor(125141)
        Equipments = DynAccessor(125142)
        Instructions = DynAccessor(125143)
        Shells = DynAccessor(125144)
        Loadout = DynAccessor(125145)
        Crew = DynAccessor(125146)
        VehicleParams = DynAccessor(125147)
        ETEVehicleParams = DynAccessor(125148)
        CurrentVehicle = DynAccessor(125149)
        VehiclesInventory = DynAccessor(125150)
        MainMenu = DynAccessor(125151)
        VehicleMenu = DynAccessor(125152)
        LootboxEntryPoint = DynAccessor(125153)
        VehicleFilters = DynAccessor(125154)
        VehiclePlaylists = DynAccessor(125155)
        Teaser = DynAccessor(125156)
        OptionalDevicesAssistant = DynAccessor(125157)
        SpaceInteraction = DynAccessor(125158)
        HeroTank = DynAccessor(125159)
        UserMissions = DynAccessor(125160)
        ModeState = DynAccessor(125161)
        EasyTankEquip = DynAccessor(125162)
        PetEvent = DynAccessor(125163)
        PetObjectTooltip = DynAccessor(125164)
        Settings = DynAccessor(125165)
        KeyBindings = DynAccessor(125166)

    shared = _shared(125167)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(125169)
        ContactsList = DynAccessor(125170)
        SessionStats = DynAccessor(125171)
        VehicleCompare = DynAccessor(125172)
        NotificationsCenter = DynAccessor(125173)
        Chats = DynAccessor(125174)
        ReferralProgram = DynAccessor(125175)
        ServerInfo = DynAccessor(125176)

    default = _default(125177)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(125179)
        NavigationBar = DynAccessor(125180)
        Prebattle = DynAccessor(125181)
        Wallet = DynAccessor(125182)
        AccountDashboard = DynAccessor(125183)
        HeaderState = DynAccessor(125184)
        UserAccount = DynAccessor(125185)
        ReservesEntryPoint = DynAccessor(125186)
        PremShop = DynAccessor(125187)
        CurrentVehicle = DynAccessor(125188)

    default = _default(125189)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(125191)
            Instructions = DynAccessor(125192)
            Shells = DynAccessor(125193)
            Consumables = DynAccessor(125194)

        Loadout = _Loadout(125195)
        Vehicles = DynAccessor(125196)

    Hangar = _Hangar(125197)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(125199)
        Events = DynAccessor(125200)
        Quests = DynAccessor(125201)
        EventMainInfoTip = DynAccessor(125202)

    hangarWidget = _hangarWidget(125203)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(125204)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(125205)
                DailyBlock = DynAccessor(125206)
                PremiumBlock = DynAccessor(125207)
                RewardProgressBlock = DynAccessor(125208)

            DailyMissionsSection = _DailyMissionsSection(125209)
            WeeklyMissions = DynAccessor(125210)
            PersonalMissions = DynAccessor(125211)

        basicMissions = _basicMissions(125212)

    hub = _hub(125213)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(125215)
        Wallet = DynAccessor(125216)

    default = _default(125217)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(125219)
    UserMissions = DynAccessor(125220)
    VehiclesInventory = DynAccessor(125221)
    VehiclesFilter = DynAccessor(125222)
    AlertMessage = DynAccessor(125223)
    Header = DynAccessor(125224)
    LoadoutPanelContainer = DynAccessor(125225)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(125226)
        EventShop = DynAccessor(125227)

    hangarWidget = _hangarWidget(125228)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(125229)
        Commander = DynAccessor(125230)

    loadoutPanelContainer = _loadoutPanelContainer(125231)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(125233)
        Schedule = DynAccessor(125234)
        SeasonModifier = DynAccessor(125235)
        RoleSkillSlot = DynAccessor(125236)
        UserMissions = DynAccessor(125237)
        EntryPoint = DynAccessor(125238)
        WeeklyQuestsWidget = DynAccessor(125239)

    shared = _shared(125240)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(125242)
        SeasonModifier = DynAccessor(125243)
        RoleSkillSlot = DynAccessor(125244)
        UserMissions = DynAccessor(125245)
        EntryPoint = DynAccessor(125246)
        Quests = DynAccessor(125247)

    shared = _shared(125248)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(125250)

    loadout = _loadout(125251)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(125252)
        AlertMessage = DynAccessor(125253)

    shared = _shared(125254)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(125256)
        ProgressionEntryPoint = DynAccessor(125257)

    shared = _shared(125258)


class Aliases(DynAccessor):
    __slots__ = ()
    battle_modifiers = battle_modifiers()
    battle_pass = battle_pass()
    battle_result = battle_result()
    battle_results = battle_results()
    common = common()
    hangar = hangar()
    lobby_footer = lobby_footer()
    lobby_header = lobby_header()
    states = states()
    user_missions = user_missions()
    vehicle_hub = vehicle_hub()
    battle_royale = battle_royale()
    comp7 = comp7()
    comp7_light = comp7_light()
    frontline = frontline()
    fun_random = fun_random()