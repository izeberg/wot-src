from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(129033)

    shared = _shared(129034)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(129036)
    ExtraVideo = DynAccessor(129037)
    Intro = DynAccessor(129038)
    ChapterChoice = DynAccessor(129039)
    Progression = DynAccessor(129040)
    PostProgression = DynAccessor(129041)
    BuyPass = DynAccessor(129042)
    BuyPassRewards = DynAccessor(129043)
    BuyLevels = DynAccessor(129044)
    BuyLevelsRewards = DynAccessor(129045)
    HolidayFinal = DynAccessor(129046)
    FinalRewardPreview = DynAccessor(129047)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129049)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(129050)
        Vehicle = DynAccessor(129051)

    contextMenu = _contextMenu(129052)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(129054)
        WeeklyMissions = DynAccessor(129055)
        PersonalMissions = DynAccessor(129056)
        BattlePass = DynAccessor(129057)
        Prestige = DynAccessor(129058)
        BattleMatters = DynAccessor(129059)
        ModuleVehicleUnlocks = DynAccessor(129060)
        CommonQuests = DynAccessor(129061)

    progression = _progression(129062)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129064)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129065)

    contextMenu = _contextMenu(129066)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129067)
        Wulf = DynAccessor(129068)
        Param = DynAccessor(129069)

    tooltip = _tooltip(129070)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129071)

    popOver = _popOver(129072)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(129073)

    shared = _shared(129074)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129076)
        VehiclesStatistics = DynAccessor(129077)
        Consumables = DynAccessor(129078)
        Equipments = DynAccessor(129079)
        Instructions = DynAccessor(129080)
        Shells = DynAccessor(129081)
        Loadout = DynAccessor(129082)
        Crew = DynAccessor(129083)
        VehicleParams = DynAccessor(129084)
        ETEVehicleParams = DynAccessor(129085)
        CurrentVehicle = DynAccessor(129086)
        VehiclesInventory = DynAccessor(129087)
        MainMenu = DynAccessor(129088)
        VehicleMenu = DynAccessor(129089)
        LootboxEntryPoint = DynAccessor(129090)
        VehicleFilters = DynAccessor(129091)
        VehiclePlaylists = DynAccessor(129092)
        Teaser = DynAccessor(129093)
        OptionalDevicesAssistant = DynAccessor(129094)
        SpaceInteraction = DynAccessor(129095)
        HeroTank = DynAccessor(129096)
        UserMissions = DynAccessor(129097)
        ModeState = DynAccessor(129098)
        EasyTankEquip = DynAccessor(129099)
        PetEvent = DynAccessor(129100)
        PetObjectTooltip = DynAccessor(129101)
        Settings = DynAccessor(129102)
        KeyBindings = DynAccessor(129103)
        ManageableVehiclePlaylists = DynAccessor(129104)

    shared = _shared(129105)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(129107)
        ContactsList = DynAccessor(129108)
        SessionStats = DynAccessor(129109)
        VehicleCompare = DynAccessor(129110)
        NotificationsCenter = DynAccessor(129111)
        Chats = DynAccessor(129112)
        ReferralProgram = DynAccessor(129113)
        ServerInfo = DynAccessor(129114)

    default = _default(129115)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(129117)
        NavigationBar = DynAccessor(129118)
        Prebattle = DynAccessor(129119)
        Wallet = DynAccessor(129120)
        AccountDashboard = DynAccessor(129121)
        HeaderState = DynAccessor(129122)
        UserAccount = DynAccessor(129123)
        ReservesEntryPoint = DynAccessor(129124)
        PremShop = DynAccessor(129125)
        CurrentVehicle = DynAccessor(129126)

    default = _default(129127)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129129)
        VehiclesInventory = DynAccessor(129130)
        VehiclesStatistics = DynAccessor(129131)
        VehicleFilters = DynAccessor(129132)
        VehiclePlaylists = DynAccessor(129133)

    select_vehicle = _select_vehicle(129134)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(129136)
            Instructions = DynAccessor(129137)
            Shells = DynAccessor(129138)
            Consumables = DynAccessor(129139)

        Loadout = _Loadout(129140)
        Vehicles = DynAccessor(129141)

    Hangar = _Hangar(129142)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(129144)
        Events = DynAccessor(129145)
        Quests = DynAccessor(129146)
        EventMainInfoTip = DynAccessor(129147)

    hangarWidget = _hangarWidget(129148)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(129149)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(129150)
                DailyBlock = DynAccessor(129151)
                PremiumBlock = DynAccessor(129152)
                RewardProgressBlock = DynAccessor(129153)

            DailyMissionsSection = _DailyMissionsSection(129154)
            WeeklyMissions = DynAccessor(129155)
            PersonalMissions = DynAccessor(129156)

        basicMissions = _basicMissions(129157)

    hub = _hub(129158)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(129160)
        Wallet = DynAccessor(129161)
        VehicleInfo = DynAccessor(129162)
        ManageableVehiclePlaylists = DynAccessor(129163)
        VehiclesInfo = DynAccessor(129164)
        VehiclesStatistics = DynAccessor(129165)
        VehicleFilters = DynAccessor(129166)
        VehiclePlaylists = DynAccessor(129167)
        VehiclesInventory = DynAccessor(129168)

    default = _default(129169)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(129171)
        CrewAutoReturn = DynAccessor(129172)
        CrewRetrain = DynAccessor(129173)
        QuickTraining = DynAccessor(129174)
        CrewOut = DynAccessor(129175)
        CrewBack = DynAccessor(129176)
        EasyEquip = DynAccessor(129177)
        ArmorInspector = DynAccessor(129178)
        FieldModification = DynAccessor(129179)
        NationChange = DynAccessor(129180)
        Research = DynAccessor(129181)
        AboutVehicle = DynAccessor(129182)
        Compare = DynAccessor(129183)
        Repairs = DynAccessor(129184)
        VehSkillTree = DynAccessor(129185)
        ProBoost = DynAccessor(129186)

    default = _default(129187)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129189)
        ConsumablesPanel = DynAccessor(129190)
        Progression = DynAccessor(129191)
        Crewman = DynAccessor(129192)
        VehicleStats = DynAccessor(129193)
        ProgressionContent = DynAccessor(129194)
        ProgressionQuests = DynAccessor(129195)
        LootboxEntryPoint = DynAccessor(129196)

    shared = _shared(129197)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(129199)
    UserMissions = DynAccessor(129200)
    VehiclesInventory = DynAccessor(129201)
    VehiclesFilter = DynAccessor(129202)
    AlertMessage = DynAccessor(129203)
    Header = DynAccessor(129204)
    LoadoutPanelContainer = DynAccessor(129205)
    Events = DynAccessor(129206)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(129207)
        EventShop = DynAccessor(129208)

    hangarWidget = _hangarWidget(129209)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(129210)
        Commander = DynAccessor(129211)

    loadoutPanelContainer = _loadoutPanelContainer(129212)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129214)
        Schedule = DynAccessor(129215)
        SeasonModifier = DynAccessor(129216)
        RoleSkillSlot = DynAccessor(129217)
        UserMissions = DynAccessor(129218)
        EntryPoint = DynAccessor(129219)
        WeeklyQuestsWidget = DynAccessor(129220)
        BattleResultsWeeklyQuests = DynAccessor(129221)
        BattleResultsCustomizationQuests = DynAccessor(129222)

    shared = _shared(129223)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129225)
        SeasonModifier = DynAccessor(129226)
        RoleSkillSlot = DynAccessor(129227)
        UserMissions = DynAccessor(129228)
        EntryPoint = DynAccessor(129229)
        Quests = DynAccessor(129230)

    shared = _shared(129231)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(129233)

    loadout = _loadout(129234)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129235)
        AlertMessage = DynAccessor(129236)

    shared = _shared(129237)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129239)
        ProgressionEntryPoint = DynAccessor(129240)

    shared = _shared(129241)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129243)
        Difficulty = DynAccessor(129244)
        MoneyBalance = DynAccessor(129245)
        TeamStats = DynAccessor(129246)
        Meta = DynAccessor(129247)
        Keys = DynAccessor(129248)
        Quests = DynAccessor(129249)
        RewardPath = DynAccessor(129250)
        Shop = DynAccessor(129251)
        Gsw = DynAccessor(129252)
        Switcher = DynAccessor(129253)
        PresetsSwitcher = DynAccessor(129254)
        VehiclesDaily = DynAccessor(129255)
        BundleCard = DynAccessor(129256)
        DailyCard = DynAccessor(129257)
        Parallax = DynAccessor(129258)

    shared = _shared(129259)


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
    select_vehicle = select_vehicle()
    states = states()
    user_missions = user_missions()
    vehicle_hub = vehicle_hub()
    vehicle_menu = vehicle_menu()
    white_tiger = white_tiger()
    battle_royale = battle_royale()
    comp7 = comp7()
    comp7_light = comp7_light()
    frontline = frontline()
    fun_random = fun_random()
    last_stand = last_stand()