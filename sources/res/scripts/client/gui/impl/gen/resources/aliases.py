from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(129024)

    shared = _shared(129025)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(129027)
    ExtraVideo = DynAccessor(129028)
    Intro = DynAccessor(129029)
    ChapterChoice = DynAccessor(129030)
    Progression = DynAccessor(129031)
    PostProgression = DynAccessor(129032)
    BuyPass = DynAccessor(129033)
    BuyPassRewards = DynAccessor(129034)
    BuyLevels = DynAccessor(129035)
    BuyLevelsRewards = DynAccessor(129036)
    HolidayFinal = DynAccessor(129037)
    FinalRewardPreview = DynAccessor(129038)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129040)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(129041)
        Vehicle = DynAccessor(129042)

    contextMenu = _contextMenu(129043)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(129045)
        WeeklyMissions = DynAccessor(129046)
        PersonalMissions = DynAccessor(129047)
        BattlePass = DynAccessor(129048)
        Prestige = DynAccessor(129049)
        BattleMatters = DynAccessor(129050)
        ModuleVehicleUnlocks = DynAccessor(129051)
        CommonQuests = DynAccessor(129052)

    progression = _progression(129053)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129055)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129056)

    contextMenu = _contextMenu(129057)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129058)
        Wulf = DynAccessor(129059)
        Param = DynAccessor(129060)

    tooltip = _tooltip(129061)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129062)

    popOver = _popOver(129063)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(129064)

    shared = _shared(129065)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129067)
        VehiclesStatistics = DynAccessor(129068)
        Consumables = DynAccessor(129069)
        Equipments = DynAccessor(129070)
        Instructions = DynAccessor(129071)
        Shells = DynAccessor(129072)
        Loadout = DynAccessor(129073)
        Crew = DynAccessor(129074)
        VehicleParams = DynAccessor(129075)
        ETEVehicleParams = DynAccessor(129076)
        CurrentVehicle = DynAccessor(129077)
        VehiclesInventory = DynAccessor(129078)
        MainMenu = DynAccessor(129079)
        VehicleMenu = DynAccessor(129080)
        LootboxEntryPoint = DynAccessor(129081)
        VehicleFilters = DynAccessor(129082)
        VehiclePlaylists = DynAccessor(129083)
        Teaser = DynAccessor(129084)
        OptionalDevicesAssistant = DynAccessor(129085)
        SpaceInteraction = DynAccessor(129086)
        HeroTank = DynAccessor(129087)
        UserMissions = DynAccessor(129088)
        ModeState = DynAccessor(129089)
        EasyTankEquip = DynAccessor(129090)
        PetEvent = DynAccessor(129091)
        PetObjectTooltip = DynAccessor(129092)
        Settings = DynAccessor(129093)
        KeyBindings = DynAccessor(129094)
        ManageableVehiclePlaylists = DynAccessor(129095)

    shared = _shared(129096)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(129098)
        ContactsList = DynAccessor(129099)
        SessionStats = DynAccessor(129100)
        VehicleCompare = DynAccessor(129101)
        NotificationsCenter = DynAccessor(129102)
        Chats = DynAccessor(129103)
        ReferralProgram = DynAccessor(129104)
        ServerInfo = DynAccessor(129105)

    default = _default(129106)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(129108)
        NavigationBar = DynAccessor(129109)
        Prebattle = DynAccessor(129110)
        Wallet = DynAccessor(129111)
        AccountDashboard = DynAccessor(129112)
        HeaderState = DynAccessor(129113)
        UserAccount = DynAccessor(129114)
        ReservesEntryPoint = DynAccessor(129115)
        PremShop = DynAccessor(129116)
        CurrentVehicle = DynAccessor(129117)

    default = _default(129118)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129120)
        VehiclesInventory = DynAccessor(129121)
        VehiclesStatistics = DynAccessor(129122)
        VehicleFilters = DynAccessor(129123)
        VehiclePlaylists = DynAccessor(129124)

    select_vehicle = _select_vehicle(129125)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(129127)
            Instructions = DynAccessor(129128)
            Shells = DynAccessor(129129)
            Consumables = DynAccessor(129130)

        Loadout = _Loadout(129131)
        Vehicles = DynAccessor(129132)

    Hangar = _Hangar(129133)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(129135)
        Events = DynAccessor(129136)
        Quests = DynAccessor(129137)
        EventMainInfoTip = DynAccessor(129138)

    hangarWidget = _hangarWidget(129139)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(129140)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(129141)
                DailyBlock = DynAccessor(129142)
                PremiumBlock = DynAccessor(129143)
                RewardProgressBlock = DynAccessor(129144)

            DailyMissionsSection = _DailyMissionsSection(129145)
            WeeklyMissions = DynAccessor(129146)
            PersonalMissions = DynAccessor(129147)

        basicMissions = _basicMissions(129148)

    hub = _hub(129149)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(129151)
        Wallet = DynAccessor(129152)
        VehicleInfo = DynAccessor(129153)
        ManageableVehiclePlaylists = DynAccessor(129154)
        VehiclesInfo = DynAccessor(129155)
        VehiclesStatistics = DynAccessor(129156)
        VehicleFilters = DynAccessor(129157)
        VehiclePlaylists = DynAccessor(129158)
        VehiclesInventory = DynAccessor(129159)

    default = _default(129160)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(129162)
        CrewAutoReturn = DynAccessor(129163)
        CrewRetrain = DynAccessor(129164)
        QuickTraining = DynAccessor(129165)
        CrewOut = DynAccessor(129166)
        CrewBack = DynAccessor(129167)
        EasyEquip = DynAccessor(129168)
        ArmorInspector = DynAccessor(129169)
        FieldModification = DynAccessor(129170)
        NationChange = DynAccessor(129171)
        Research = DynAccessor(129172)
        AboutVehicle = DynAccessor(129173)
        Compare = DynAccessor(129174)
        Repairs = DynAccessor(129175)
        VehSkillTree = DynAccessor(129176)
        ProBoost = DynAccessor(129177)

    default = _default(129178)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129180)
        ConsumablesPanel = DynAccessor(129181)
        Progression = DynAccessor(129182)
        Crewman = DynAccessor(129183)
        VehicleStats = DynAccessor(129184)
        ProgressionContent = DynAccessor(129185)
        ProgressionQuests = DynAccessor(129186)
        LootboxEntryPoint = DynAccessor(129187)

    shared = _shared(129188)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(129190)
    UserMissions = DynAccessor(129191)
    VehiclesInventory = DynAccessor(129192)
    VehiclesFilter = DynAccessor(129193)
    AlertMessage = DynAccessor(129194)
    Header = DynAccessor(129195)
    LoadoutPanelContainer = DynAccessor(129196)
    Events = DynAccessor(129197)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(129198)
        EventShop = DynAccessor(129199)

    hangarWidget = _hangarWidget(129200)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(129201)
        Commander = DynAccessor(129202)

    loadoutPanelContainer = _loadoutPanelContainer(129203)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129205)
        Schedule = DynAccessor(129206)
        SeasonModifier = DynAccessor(129207)
        RoleSkillSlot = DynAccessor(129208)
        UserMissions = DynAccessor(129209)
        EntryPoint = DynAccessor(129210)
        WeeklyQuestsWidget = DynAccessor(129211)
        BattleResultsWeeklyQuests = DynAccessor(129212)
        BattleResultsCustomizationQuests = DynAccessor(129213)

    shared = _shared(129214)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129216)
        SeasonModifier = DynAccessor(129217)
        RoleSkillSlot = DynAccessor(129218)
        UserMissions = DynAccessor(129219)
        EntryPoint = DynAccessor(129220)
        Quests = DynAccessor(129221)

    shared = _shared(129222)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(129224)

    loadout = _loadout(129225)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129226)
        AlertMessage = DynAccessor(129227)

    shared = _shared(129228)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129230)
        ProgressionEntryPoint = DynAccessor(129231)

    shared = _shared(129232)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129234)
        Difficulty = DynAccessor(129235)
        MoneyBalance = DynAccessor(129236)
        TeamStats = DynAccessor(129237)
        Meta = DynAccessor(129238)
        Keys = DynAccessor(129239)
        Quests = DynAccessor(129240)
        RewardPath = DynAccessor(129241)
        Shop = DynAccessor(129242)
        Gsw = DynAccessor(129243)
        Switcher = DynAccessor(129244)
        PresetsSwitcher = DynAccessor(129245)
        VehiclesDaily = DynAccessor(129246)
        BundleCard = DynAccessor(129247)
        DailyCard = DynAccessor(129248)
        Parallax = DynAccessor(129249)

    shared = _shared(129250)


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