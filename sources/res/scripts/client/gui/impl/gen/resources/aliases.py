from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(129018)

    shared = _shared(129019)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(129021)
    ExtraVideo = DynAccessor(129022)
    Intro = DynAccessor(129023)
    ChapterChoice = DynAccessor(129024)
    Progression = DynAccessor(129025)
    PostProgression = DynAccessor(129026)
    BuyPass = DynAccessor(129027)
    BuyPassRewards = DynAccessor(129028)
    BuyLevels = DynAccessor(129029)
    BuyLevelsRewards = DynAccessor(129030)
    HolidayFinal = DynAccessor(129031)
    FinalRewardPreview = DynAccessor(129032)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129034)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(129035)
        Vehicle = DynAccessor(129036)

    contextMenu = _contextMenu(129037)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(129039)
        WeeklyMissions = DynAccessor(129040)
        PersonalMissions = DynAccessor(129041)
        BattlePass = DynAccessor(129042)
        Prestige = DynAccessor(129043)
        BattleMatters = DynAccessor(129044)
        ModuleVehicleUnlocks = DynAccessor(129045)
        CommonQuests = DynAccessor(129046)

    progression = _progression(129047)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129049)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129050)

    contextMenu = _contextMenu(129051)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129052)
        Wulf = DynAccessor(129053)
        Param = DynAccessor(129054)

    tooltip = _tooltip(129055)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129056)

    popOver = _popOver(129057)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(129058)

    shared = _shared(129059)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129061)
        VehiclesStatistics = DynAccessor(129062)
        Consumables = DynAccessor(129063)
        Equipments = DynAccessor(129064)
        Instructions = DynAccessor(129065)
        Shells = DynAccessor(129066)
        Loadout = DynAccessor(129067)
        Crew = DynAccessor(129068)
        VehicleParams = DynAccessor(129069)
        ETEVehicleParams = DynAccessor(129070)
        CurrentVehicle = DynAccessor(129071)
        VehiclesInventory = DynAccessor(129072)
        MainMenu = DynAccessor(129073)
        VehicleMenu = DynAccessor(129074)
        LootboxEntryPoint = DynAccessor(129075)
        VehicleFilters = DynAccessor(129076)
        VehiclePlaylists = DynAccessor(129077)
        Teaser = DynAccessor(129078)
        OptionalDevicesAssistant = DynAccessor(129079)
        SpaceInteraction = DynAccessor(129080)
        HeroTank = DynAccessor(129081)
        UserMissions = DynAccessor(129082)
        ModeState = DynAccessor(129083)
        EasyTankEquip = DynAccessor(129084)
        PetEvent = DynAccessor(129085)
        PetObjectTooltip = DynAccessor(129086)
        Settings = DynAccessor(129087)
        KeyBindings = DynAccessor(129088)
        ManageableVehiclePlaylists = DynAccessor(129089)

    shared = _shared(129090)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(129092)
        ContactsList = DynAccessor(129093)
        SessionStats = DynAccessor(129094)
        VehicleCompare = DynAccessor(129095)
        NotificationsCenter = DynAccessor(129096)
        Chats = DynAccessor(129097)
        ReferralProgram = DynAccessor(129098)
        ServerInfo = DynAccessor(129099)

    default = _default(129100)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(129102)
        NavigationBar = DynAccessor(129103)
        Prebattle = DynAccessor(129104)
        Wallet = DynAccessor(129105)
        AccountDashboard = DynAccessor(129106)
        HeaderState = DynAccessor(129107)
        UserAccount = DynAccessor(129108)
        ReservesEntryPoint = DynAccessor(129109)
        PremShop = DynAccessor(129110)
        CurrentVehicle = DynAccessor(129111)

    default = _default(129112)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129114)
        VehiclesInventory = DynAccessor(129115)
        VehiclesStatistics = DynAccessor(129116)
        VehicleFilters = DynAccessor(129117)
        VehiclePlaylists = DynAccessor(129118)

    select_vehicle = _select_vehicle(129119)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(129121)
            Instructions = DynAccessor(129122)
            Shells = DynAccessor(129123)
            Consumables = DynAccessor(129124)

        Loadout = _Loadout(129125)
        Vehicles = DynAccessor(129126)

    Hangar = _Hangar(129127)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(129129)
        Events = DynAccessor(129130)
        Quests = DynAccessor(129131)
        EventMainInfoTip = DynAccessor(129132)

    hangarWidget = _hangarWidget(129133)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(129134)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(129135)
                DailyBlock = DynAccessor(129136)
                PremiumBlock = DynAccessor(129137)
                RewardProgressBlock = DynAccessor(129138)

            DailyMissionsSection = _DailyMissionsSection(129139)
            WeeklyMissions = DynAccessor(129140)
            PersonalMissions = DynAccessor(129141)

        basicMissions = _basicMissions(129142)

    hub = _hub(129143)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(129145)
        Wallet = DynAccessor(129146)
        VehicleInfo = DynAccessor(129147)
        ManageableVehiclePlaylists = DynAccessor(129148)
        VehiclesInfo = DynAccessor(129149)
        VehiclesStatistics = DynAccessor(129150)
        VehicleFilters = DynAccessor(129151)
        VehiclePlaylists = DynAccessor(129152)
        VehiclesInventory = DynAccessor(129153)

    default = _default(129154)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(129156)
        CrewAutoReturn = DynAccessor(129157)
        CrewRetrain = DynAccessor(129158)
        QuickTraining = DynAccessor(129159)
        CrewOut = DynAccessor(129160)
        CrewBack = DynAccessor(129161)
        EasyEquip = DynAccessor(129162)
        ArmorInspector = DynAccessor(129163)
        FieldModification = DynAccessor(129164)
        NationChange = DynAccessor(129165)
        Research = DynAccessor(129166)
        AboutVehicle = DynAccessor(129167)
        Compare = DynAccessor(129168)
        Repairs = DynAccessor(129169)
        VehSkillTree = DynAccessor(129170)
        ProBoost = DynAccessor(129171)

    default = _default(129172)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129174)
        ConsumablesPanel = DynAccessor(129175)
        Progression = DynAccessor(129176)
        Crewman = DynAccessor(129177)
        VehicleStats = DynAccessor(129178)
        ProgressionContent = DynAccessor(129179)
        ProgressionQuests = DynAccessor(129180)
        LootboxEntryPoint = DynAccessor(129181)

    shared = _shared(129182)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(129184)
    UserMissions = DynAccessor(129185)
    VehiclesInventory = DynAccessor(129186)
    VehiclesFilter = DynAccessor(129187)
    AlertMessage = DynAccessor(129188)
    Header = DynAccessor(129189)
    LoadoutPanelContainer = DynAccessor(129190)
    Events = DynAccessor(129191)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(129192)
        EventShop = DynAccessor(129193)

    hangarWidget = _hangarWidget(129194)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(129195)
        Commander = DynAccessor(129196)

    loadoutPanelContainer = _loadoutPanelContainer(129197)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129199)
        Schedule = DynAccessor(129200)
        SeasonModifier = DynAccessor(129201)
        RoleSkillSlot = DynAccessor(129202)
        UserMissions = DynAccessor(129203)
        EntryPoint = DynAccessor(129204)
        WeeklyQuestsWidget = DynAccessor(129205)
        BattleResultsWeeklyQuests = DynAccessor(129206)
        BattleResultsCustomizationQuests = DynAccessor(129207)

    shared = _shared(129208)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129210)
        SeasonModifier = DynAccessor(129211)
        RoleSkillSlot = DynAccessor(129212)
        UserMissions = DynAccessor(129213)
        EntryPoint = DynAccessor(129214)
        Quests = DynAccessor(129215)

    shared = _shared(129216)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(129218)

    loadout = _loadout(129219)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129220)
        AlertMessage = DynAccessor(129221)

    shared = _shared(129222)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129224)
        ProgressionEntryPoint = DynAccessor(129225)

    shared = _shared(129226)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129228)
        Difficulty = DynAccessor(129229)
        MoneyBalance = DynAccessor(129230)
        TeamStats = DynAccessor(129231)
        Meta = DynAccessor(129232)
        Keys = DynAccessor(129233)
        Quests = DynAccessor(129234)
        RewardPath = DynAccessor(129235)
        Shop = DynAccessor(129236)
        Gsw = DynAccessor(129237)
        Switcher = DynAccessor(129238)
        PresetsSwitcher = DynAccessor(129239)
        VehiclesDaily = DynAccessor(129240)
        BundleCard = DynAccessor(129241)
        DailyCard = DynAccessor(129242)
        Parallax = DynAccessor(129243)

    shared = _shared(129244)


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