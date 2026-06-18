from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(130223)

    shared = _shared(130224)


class battle_pass(DynAccessor):
    __slots__ = ()
    ChapterChoice = DynAccessor(130226)
    Progression = DynAccessor(130227)
    PostProgression = DynAccessor(130228)
    BuyPass = DynAccessor(130229)
    BuyPassRewards = DynAccessor(130230)
    BuyLevels = DynAccessor(130231)
    BuyLevelsRewards = DynAccessor(130232)
    HolidayFinal = DynAccessor(130233)
    FinalRewardPreview = DynAccessor(130234)
    TankmenScreen = DynAccessor(130235)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(130237)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(130238)
        Vehicle = DynAccessor(130239)

    contextMenu = _contextMenu(130240)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(130242)
        WeeklyMissions = DynAccessor(130243)
        PersonalMissions = DynAccessor(130244)
        BattlePass = DynAccessor(130245)
        Prestige = DynAccessor(130246)
        BattleMatters = DynAccessor(130247)
        ModuleVehicleUnlocks = DynAccessor(130248)
        CommonQuests = DynAccessor(130249)
        Challenges = DynAccessor(130250)

    progression = _progression(130251)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(130253)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(130254)

    contextMenu = _contextMenu(130255)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(130256)
        Wulf = DynAccessor(130257)
        Param = DynAccessor(130258)

    tooltip = _tooltip(130259)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(130260)

    popOver = _popOver(130261)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(130262)

    shared = _shared(130263)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(130265)
        VehiclesStatistics = DynAccessor(130266)
        Consumables = DynAccessor(130267)
        Equipments = DynAccessor(130268)
        Instructions = DynAccessor(130269)
        Shells = DynAccessor(130270)
        Loadout = DynAccessor(130271)
        Crew = DynAccessor(130272)
        VehicleParams = DynAccessor(130273)
        ETEVehicleParams = DynAccessor(130274)
        CurrentVehicle = DynAccessor(130275)
        VehiclesInventory = DynAccessor(130276)
        MainMenu = DynAccessor(130277)
        VehicleMenu = DynAccessor(130278)
        LootboxEntryPoint = DynAccessor(130279)
        VehicleFilters = DynAccessor(130280)
        VehiclePlaylists = DynAccessor(130281)
        Teaser = DynAccessor(130282)
        OptionalDevicesAssistant = DynAccessor(130283)
        SpaceInteraction = DynAccessor(130284)
        HeroTank = DynAccessor(130285)
        UserMissions = DynAccessor(130286)
        ModeState = DynAccessor(130287)
        EasyTankEquip = DynAccessor(130288)
        PetEvent = DynAccessor(130289)
        PetObjectTooltip = DynAccessor(130290)
        Settings = DynAccessor(130291)
        KeyBindings = DynAccessor(130292)
        ManageableVehiclePlaylists = DynAccessor(130293)

    shared = _shared(130294)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(130296)
        ContactsList = DynAccessor(130297)
        SessionStats = DynAccessor(130298)
        VehicleCompare = DynAccessor(130299)
        NotificationsCenter = DynAccessor(130300)
        Chats = DynAccessor(130301)
        ReferralProgram = DynAccessor(130302)
        ServerInfo = DynAccessor(130303)

    default = _default(130304)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(130306)
        NavigationBar = DynAccessor(130307)
        Prebattle = DynAccessor(130308)
        Wallet = DynAccessor(130309)
        AccountDashboard = DynAccessor(130310)
        HeaderState = DynAccessor(130311)
        UserAccount = DynAccessor(130312)
        ReservesEntryPoint = DynAccessor(130313)
        PremShop = DynAccessor(130314)
        CurrentVehicle = DynAccessor(130315)

    default = _default(130316)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(130318)
        VehiclesInventory = DynAccessor(130319)
        VehiclesStatistics = DynAccessor(130320)
        VehicleFilters = DynAccessor(130321)
        VehiclePlaylists = DynAccessor(130322)

    select_vehicle = _select_vehicle(130323)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(130325)
            Instructions = DynAccessor(130326)
            Shells = DynAccessor(130327)
            Consumables = DynAccessor(130328)

        Loadout = _Loadout(130329)
        Vehicles = DynAccessor(130330)

    Hangar = _Hangar(130331)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(130333)
        Events = DynAccessor(130334)
        Quests = DynAccessor(130335)
        EventMainInfoTip = DynAccessor(130336)

    hangarWidget = _hangarWidget(130337)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(130338)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(130339)
                DailyBlock = DynAccessor(130340)
                PremiumBlock = DynAccessor(130341)
                RewardProgressBlock = DynAccessor(130342)

            DailyMissionsSection = _DailyMissionsSection(130343)
            WeeklyMissions = DynAccessor(130344)
            PersonalMissions = DynAccessor(130345)

        basicMissions = _basicMissions(130346)

        class _challengeMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(130347)

        challengeMissions = _challengeMissions(130348)

    hub = _hub(130349)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(130351)
        Wallet = DynAccessor(130352)
        VehicleInfo = DynAccessor(130353)
        ManageableVehiclePlaylists = DynAccessor(130354)
        VehiclesInfo = DynAccessor(130355)
        VehiclesStatistics = DynAccessor(130356)
        VehicleFilters = DynAccessor(130357)
        VehiclePlaylists = DynAccessor(130358)
        VehiclesInventory = DynAccessor(130359)

    default = _default(130360)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(130362)
        CrewAutoReturn = DynAccessor(130363)
        CrewRetrain = DynAccessor(130364)
        QuickTraining = DynAccessor(130365)
        CrewOut = DynAccessor(130366)
        CrewBack = DynAccessor(130367)
        EasyEquip = DynAccessor(130368)
        ArmorInspector = DynAccessor(130369)
        FieldModification = DynAccessor(130370)
        NationChange = DynAccessor(130371)
        Research = DynAccessor(130372)
        AboutVehicle = DynAccessor(130373)
        Compare = DynAccessor(130374)
        Repairs = DynAccessor(130375)
        VehSkillTree = DynAccessor(130376)
        ProBoost = DynAccessor(130377)

    default = _default(130378)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(130380)
        ConsumablesPanel = DynAccessor(130381)
        Progression = DynAccessor(130382)
        Crewman = DynAccessor(130383)
        VehicleStats = DynAccessor(130384)
        ProgressionContent = DynAccessor(130385)
        ProgressionQuests = DynAccessor(130386)
        LootboxEntryPoint = DynAccessor(130387)

    shared = _shared(130388)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(130390)
    UserMissions = DynAccessor(130391)
    VehiclesInventory = DynAccessor(130392)
    VehiclesFilter = DynAccessor(130393)
    AlertMessage = DynAccessor(130394)
    Header = DynAccessor(130395)
    LoadoutPanelContainer = DynAccessor(130396)
    Events = DynAccessor(130397)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(130398)
        EventShop = DynAccessor(130399)

    hangarWidget = _hangarWidget(130400)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(130401)
        Commander = DynAccessor(130402)

    loadoutPanelContainer = _loadoutPanelContainer(130403)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(130405)
        Schedule = DynAccessor(130406)
        SeasonModifier = DynAccessor(130407)
        RoleSkillSlot = DynAccessor(130408)
        UserMissions = DynAccessor(130409)
        EntryPoint = DynAccessor(130410)
        WeeklyQuestsWidget = DynAccessor(130411)
        BattleResultsWeeklyQuests = DynAccessor(130412)
        BattleResultsCustomizationQuests = DynAccessor(130413)

    shared = _shared(130414)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(130416)
        SeasonModifier = DynAccessor(130417)
        RoleSkillSlot = DynAccessor(130418)
        UserMissions = DynAccessor(130419)
        EntryPoint = DynAccessor(130420)
        Quests = DynAccessor(130421)
        BattleResultsProgressionQuests = DynAccessor(130422)

    shared = _shared(130423)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(130425)

    loadout = _loadout(130426)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(130427)
        AlertMessage = DynAccessor(130428)

    shared = _shared(130429)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(130431)
        ProgressionEntryPoint = DynAccessor(130432)
        ProgressionQuests = DynAccessor(130433)

    shared = _shared(130434)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(130436)
        Difficulty = DynAccessor(130437)
        MoneyBalance = DynAccessor(130438)
        TeamStats = DynAccessor(130439)
        Meta = DynAccessor(130440)
        Keys = DynAccessor(130441)
        Quests = DynAccessor(130442)
        RewardPath = DynAccessor(130443)
        Shop = DynAccessor(130444)
        Gsw = DynAccessor(130445)
        Switcher = DynAccessor(130446)
        PresetsSwitcher = DynAccessor(130447)
        VehiclesDaily = DynAccessor(130448)
        BundleCard = DynAccessor(130449)
        DailyCard = DynAccessor(130450)
        Parallax = DynAccessor(130451)

    shared = _shared(130452)


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