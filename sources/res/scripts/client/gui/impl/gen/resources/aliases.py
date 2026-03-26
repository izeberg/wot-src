from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(129020)

    shared = _shared(129021)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(129023)
    ExtraVideo = DynAccessor(129024)
    Intro = DynAccessor(129025)
    ChapterChoice = DynAccessor(129026)
    Progression = DynAccessor(129027)
    PostProgression = DynAccessor(129028)
    BuyPass = DynAccessor(129029)
    BuyPassRewards = DynAccessor(129030)
    BuyLevels = DynAccessor(129031)
    BuyLevelsRewards = DynAccessor(129032)
    HolidayFinal = DynAccessor(129033)
    FinalRewardPreview = DynAccessor(129034)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129036)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(129037)
        Vehicle = DynAccessor(129038)

    contextMenu = _contextMenu(129039)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(129041)
        WeeklyMissions = DynAccessor(129042)
        PersonalMissions = DynAccessor(129043)
        BattlePass = DynAccessor(129044)
        Prestige = DynAccessor(129045)
        BattleMatters = DynAccessor(129046)
        ModuleVehicleUnlocks = DynAccessor(129047)
        CommonQuests = DynAccessor(129048)

    progression = _progression(129049)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129051)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129052)

    contextMenu = _contextMenu(129053)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129054)
        Wulf = DynAccessor(129055)
        Param = DynAccessor(129056)

    tooltip = _tooltip(129057)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129058)

    popOver = _popOver(129059)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(129060)

    shared = _shared(129061)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129063)
        VehiclesStatistics = DynAccessor(129064)
        Consumables = DynAccessor(129065)
        Equipments = DynAccessor(129066)
        Instructions = DynAccessor(129067)
        Shells = DynAccessor(129068)
        Loadout = DynAccessor(129069)
        Crew = DynAccessor(129070)
        VehicleParams = DynAccessor(129071)
        ETEVehicleParams = DynAccessor(129072)
        CurrentVehicle = DynAccessor(129073)
        VehiclesInventory = DynAccessor(129074)
        MainMenu = DynAccessor(129075)
        VehicleMenu = DynAccessor(129076)
        LootboxEntryPoint = DynAccessor(129077)
        VehicleFilters = DynAccessor(129078)
        VehiclePlaylists = DynAccessor(129079)
        Teaser = DynAccessor(129080)
        OptionalDevicesAssistant = DynAccessor(129081)
        SpaceInteraction = DynAccessor(129082)
        HeroTank = DynAccessor(129083)
        UserMissions = DynAccessor(129084)
        ModeState = DynAccessor(129085)
        EasyTankEquip = DynAccessor(129086)
        PetEvent = DynAccessor(129087)
        PetObjectTooltip = DynAccessor(129088)
        Settings = DynAccessor(129089)
        KeyBindings = DynAccessor(129090)
        ManageableVehiclePlaylists = DynAccessor(129091)

    shared = _shared(129092)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(129094)
        ContactsList = DynAccessor(129095)
        SessionStats = DynAccessor(129096)
        VehicleCompare = DynAccessor(129097)
        NotificationsCenter = DynAccessor(129098)
        Chats = DynAccessor(129099)
        ReferralProgram = DynAccessor(129100)
        ServerInfo = DynAccessor(129101)

    default = _default(129102)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(129104)
        NavigationBar = DynAccessor(129105)
        Prebattle = DynAccessor(129106)
        Wallet = DynAccessor(129107)
        AccountDashboard = DynAccessor(129108)
        HeaderState = DynAccessor(129109)
        UserAccount = DynAccessor(129110)
        ReservesEntryPoint = DynAccessor(129111)
        PremShop = DynAccessor(129112)
        CurrentVehicle = DynAccessor(129113)

    default = _default(129114)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129116)
        VehiclesInventory = DynAccessor(129117)
        VehiclesStatistics = DynAccessor(129118)
        VehicleFilters = DynAccessor(129119)
        VehiclePlaylists = DynAccessor(129120)

    select_vehicle = _select_vehicle(129121)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(129123)
            Instructions = DynAccessor(129124)
            Shells = DynAccessor(129125)
            Consumables = DynAccessor(129126)

        Loadout = _Loadout(129127)
        Vehicles = DynAccessor(129128)

    Hangar = _Hangar(129129)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(129131)
        Events = DynAccessor(129132)
        Quests = DynAccessor(129133)
        EventMainInfoTip = DynAccessor(129134)

    hangarWidget = _hangarWidget(129135)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(129136)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(129137)
                DailyBlock = DynAccessor(129138)
                PremiumBlock = DynAccessor(129139)
                RewardProgressBlock = DynAccessor(129140)

            DailyMissionsSection = _DailyMissionsSection(129141)
            WeeklyMissions = DynAccessor(129142)
            PersonalMissions = DynAccessor(129143)

        basicMissions = _basicMissions(129144)

    hub = _hub(129145)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(129147)
        Wallet = DynAccessor(129148)
        VehicleInfo = DynAccessor(129149)
        ManageableVehiclePlaylists = DynAccessor(129150)
        VehiclesInfo = DynAccessor(129151)
        VehiclesStatistics = DynAccessor(129152)
        VehicleFilters = DynAccessor(129153)
        VehiclePlaylists = DynAccessor(129154)
        VehiclesInventory = DynAccessor(129155)

    default = _default(129156)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(129158)
        CrewAutoReturn = DynAccessor(129159)
        CrewRetrain = DynAccessor(129160)
        QuickTraining = DynAccessor(129161)
        CrewOut = DynAccessor(129162)
        CrewBack = DynAccessor(129163)
        EasyEquip = DynAccessor(129164)
        ArmorInspector = DynAccessor(129165)
        FieldModification = DynAccessor(129166)
        NationChange = DynAccessor(129167)
        Research = DynAccessor(129168)
        AboutVehicle = DynAccessor(129169)
        Compare = DynAccessor(129170)
        Repairs = DynAccessor(129171)
        VehSkillTree = DynAccessor(129172)
        ProBoost = DynAccessor(129173)

    default = _default(129174)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129176)
        ConsumablesPanel = DynAccessor(129177)
        Progression = DynAccessor(129178)
        Crewman = DynAccessor(129179)
        VehicleStats = DynAccessor(129180)
        ProgressionContent = DynAccessor(129181)
        ProgressionQuests = DynAccessor(129182)
        LootboxEntryPoint = DynAccessor(129183)

    shared = _shared(129184)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(129186)
    UserMissions = DynAccessor(129187)
    VehiclesInventory = DynAccessor(129188)
    VehiclesFilter = DynAccessor(129189)
    AlertMessage = DynAccessor(129190)
    Header = DynAccessor(129191)
    LoadoutPanelContainer = DynAccessor(129192)
    Events = DynAccessor(129193)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(129194)
        EventShop = DynAccessor(129195)

    hangarWidget = _hangarWidget(129196)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(129197)
        Commander = DynAccessor(129198)

    loadoutPanelContainer = _loadoutPanelContainer(129199)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129201)
        Schedule = DynAccessor(129202)
        SeasonModifier = DynAccessor(129203)
        RoleSkillSlot = DynAccessor(129204)
        UserMissions = DynAccessor(129205)
        EntryPoint = DynAccessor(129206)
        WeeklyQuestsWidget = DynAccessor(129207)
        BattleResultsWeeklyQuests = DynAccessor(129208)
        BattleResultsCustomizationQuests = DynAccessor(129209)

    shared = _shared(129210)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129212)
        SeasonModifier = DynAccessor(129213)
        RoleSkillSlot = DynAccessor(129214)
        UserMissions = DynAccessor(129215)
        EntryPoint = DynAccessor(129216)
        Quests = DynAccessor(129217)

    shared = _shared(129218)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(129220)

    loadout = _loadout(129221)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129222)
        AlertMessage = DynAccessor(129223)

    shared = _shared(129224)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129226)
        ProgressionEntryPoint = DynAccessor(129227)

    shared = _shared(129228)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129230)
        Difficulty = DynAccessor(129231)
        MoneyBalance = DynAccessor(129232)
        TeamStats = DynAccessor(129233)
        Meta = DynAccessor(129234)
        Keys = DynAccessor(129235)
        Quests = DynAccessor(129236)
        RewardPath = DynAccessor(129237)
        Shop = DynAccessor(129238)
        Gsw = DynAccessor(129239)
        Switcher = DynAccessor(129240)
        PresetsSwitcher = DynAccessor(129241)
        VehiclesDaily = DynAccessor(129242)
        BundleCard = DynAccessor(129243)
        DailyCard = DynAccessor(129244)
        Parallax = DynAccessor(129245)

    shared = _shared(129246)


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