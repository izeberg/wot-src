from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(129022)

    shared = _shared(129023)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(129025)
    ExtraVideo = DynAccessor(129026)
    Intro = DynAccessor(129027)
    ChapterChoice = DynAccessor(129028)
    Progression = DynAccessor(129029)
    PostProgression = DynAccessor(129030)
    BuyPass = DynAccessor(129031)
    BuyPassRewards = DynAccessor(129032)
    BuyLevels = DynAccessor(129033)
    BuyLevelsRewards = DynAccessor(129034)
    HolidayFinal = DynAccessor(129035)
    FinalRewardPreview = DynAccessor(129036)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129038)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(129039)
        Vehicle = DynAccessor(129040)

    contextMenu = _contextMenu(129041)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(129043)
        WeeklyMissions = DynAccessor(129044)
        PersonalMissions = DynAccessor(129045)
        BattlePass = DynAccessor(129046)
        Prestige = DynAccessor(129047)
        BattleMatters = DynAccessor(129048)
        ModuleVehicleUnlocks = DynAccessor(129049)
        CommonQuests = DynAccessor(129050)

    progression = _progression(129051)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129053)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129054)

    contextMenu = _contextMenu(129055)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129056)
        Wulf = DynAccessor(129057)
        Param = DynAccessor(129058)

    tooltip = _tooltip(129059)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129060)

    popOver = _popOver(129061)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(129062)

    shared = _shared(129063)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129065)
        VehiclesStatistics = DynAccessor(129066)
        Consumables = DynAccessor(129067)
        Equipments = DynAccessor(129068)
        Instructions = DynAccessor(129069)
        Shells = DynAccessor(129070)
        Loadout = DynAccessor(129071)
        Crew = DynAccessor(129072)
        VehicleParams = DynAccessor(129073)
        ETEVehicleParams = DynAccessor(129074)
        CurrentVehicle = DynAccessor(129075)
        VehiclesInventory = DynAccessor(129076)
        MainMenu = DynAccessor(129077)
        VehicleMenu = DynAccessor(129078)
        LootboxEntryPoint = DynAccessor(129079)
        VehicleFilters = DynAccessor(129080)
        VehiclePlaylists = DynAccessor(129081)
        Teaser = DynAccessor(129082)
        OptionalDevicesAssistant = DynAccessor(129083)
        SpaceInteraction = DynAccessor(129084)
        HeroTank = DynAccessor(129085)
        UserMissions = DynAccessor(129086)
        ModeState = DynAccessor(129087)
        EasyTankEquip = DynAccessor(129088)
        PetEvent = DynAccessor(129089)
        PetObjectTooltip = DynAccessor(129090)
        Settings = DynAccessor(129091)
        KeyBindings = DynAccessor(129092)
        ManageableVehiclePlaylists = DynAccessor(129093)

    shared = _shared(129094)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(129096)
        ContactsList = DynAccessor(129097)
        SessionStats = DynAccessor(129098)
        VehicleCompare = DynAccessor(129099)
        NotificationsCenter = DynAccessor(129100)
        Chats = DynAccessor(129101)
        ReferralProgram = DynAccessor(129102)
        ServerInfo = DynAccessor(129103)

    default = _default(129104)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(129106)
        NavigationBar = DynAccessor(129107)
        Prebattle = DynAccessor(129108)
        Wallet = DynAccessor(129109)
        AccountDashboard = DynAccessor(129110)
        HeaderState = DynAccessor(129111)
        UserAccount = DynAccessor(129112)
        ReservesEntryPoint = DynAccessor(129113)
        PremShop = DynAccessor(129114)
        CurrentVehicle = DynAccessor(129115)

    default = _default(129116)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129118)
        VehiclesInventory = DynAccessor(129119)
        VehiclesStatistics = DynAccessor(129120)
        VehicleFilters = DynAccessor(129121)
        VehiclePlaylists = DynAccessor(129122)

    select_vehicle = _select_vehicle(129123)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(129125)
            Instructions = DynAccessor(129126)
            Shells = DynAccessor(129127)
            Consumables = DynAccessor(129128)

        Loadout = _Loadout(129129)
        Vehicles = DynAccessor(129130)

    Hangar = _Hangar(129131)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(129133)
        Events = DynAccessor(129134)
        Quests = DynAccessor(129135)
        EventMainInfoTip = DynAccessor(129136)

    hangarWidget = _hangarWidget(129137)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(129138)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(129139)
                DailyBlock = DynAccessor(129140)
                PremiumBlock = DynAccessor(129141)
                RewardProgressBlock = DynAccessor(129142)

            DailyMissionsSection = _DailyMissionsSection(129143)
            WeeklyMissions = DynAccessor(129144)
            PersonalMissions = DynAccessor(129145)

        basicMissions = _basicMissions(129146)

    hub = _hub(129147)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(129149)
        Wallet = DynAccessor(129150)
        VehicleInfo = DynAccessor(129151)
        ManageableVehiclePlaylists = DynAccessor(129152)
        VehiclesInfo = DynAccessor(129153)
        VehiclesStatistics = DynAccessor(129154)
        VehicleFilters = DynAccessor(129155)
        VehiclePlaylists = DynAccessor(129156)
        VehiclesInventory = DynAccessor(129157)

    default = _default(129158)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(129160)
        CrewAutoReturn = DynAccessor(129161)
        CrewRetrain = DynAccessor(129162)
        QuickTraining = DynAccessor(129163)
        CrewOut = DynAccessor(129164)
        CrewBack = DynAccessor(129165)
        EasyEquip = DynAccessor(129166)
        ArmorInspector = DynAccessor(129167)
        FieldModification = DynAccessor(129168)
        NationChange = DynAccessor(129169)
        Research = DynAccessor(129170)
        AboutVehicle = DynAccessor(129171)
        Compare = DynAccessor(129172)
        Repairs = DynAccessor(129173)
        VehSkillTree = DynAccessor(129174)
        ProBoost = DynAccessor(129175)

    default = _default(129176)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129178)
        ConsumablesPanel = DynAccessor(129179)
        Progression = DynAccessor(129180)
        Crewman = DynAccessor(129181)
        VehicleStats = DynAccessor(129182)
        ProgressionContent = DynAccessor(129183)
        ProgressionQuests = DynAccessor(129184)
        LootboxEntryPoint = DynAccessor(129185)

    shared = _shared(129186)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(129188)
    UserMissions = DynAccessor(129189)
    VehiclesInventory = DynAccessor(129190)
    VehiclesFilter = DynAccessor(129191)
    AlertMessage = DynAccessor(129192)
    Header = DynAccessor(129193)
    LoadoutPanelContainer = DynAccessor(129194)
    Events = DynAccessor(129195)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(129196)
        EventShop = DynAccessor(129197)

    hangarWidget = _hangarWidget(129198)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(129199)
        Commander = DynAccessor(129200)

    loadoutPanelContainer = _loadoutPanelContainer(129201)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129203)
        Schedule = DynAccessor(129204)
        SeasonModifier = DynAccessor(129205)
        RoleSkillSlot = DynAccessor(129206)
        UserMissions = DynAccessor(129207)
        EntryPoint = DynAccessor(129208)
        WeeklyQuestsWidget = DynAccessor(129209)
        BattleResultsWeeklyQuests = DynAccessor(129210)
        BattleResultsCustomizationQuests = DynAccessor(129211)

    shared = _shared(129212)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129214)
        SeasonModifier = DynAccessor(129215)
        RoleSkillSlot = DynAccessor(129216)
        UserMissions = DynAccessor(129217)
        EntryPoint = DynAccessor(129218)
        Quests = DynAccessor(129219)

    shared = _shared(129220)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(129222)

    loadout = _loadout(129223)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129224)
        AlertMessage = DynAccessor(129225)

    shared = _shared(129226)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129228)
        ProgressionEntryPoint = DynAccessor(129229)

    shared = _shared(129230)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129232)
        Difficulty = DynAccessor(129233)
        MoneyBalance = DynAccessor(129234)
        TeamStats = DynAccessor(129235)
        Meta = DynAccessor(129236)
        Keys = DynAccessor(129237)
        Quests = DynAccessor(129238)
        RewardPath = DynAccessor(129239)
        Shop = DynAccessor(129240)
        Gsw = DynAccessor(129241)
        Switcher = DynAccessor(129242)
        PresetsSwitcher = DynAccessor(129243)
        VehiclesDaily = DynAccessor(129244)
        BundleCard = DynAccessor(129245)
        DailyCard = DynAccessor(129246)
        Parallax = DynAccessor(129247)

    shared = _shared(129248)


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