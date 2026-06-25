from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(130269)

    shared = _shared(130270)


class battle_pass(DynAccessor):
    __slots__ = ()
    ChapterChoice = DynAccessor(130272)
    Progression = DynAccessor(130273)
    PostProgression = DynAccessor(130274)
    BuyPass = DynAccessor(130275)
    BuyPassRewards = DynAccessor(130276)
    BuyLevels = DynAccessor(130277)
    BuyLevelsRewards = DynAccessor(130278)
    HolidayFinal = DynAccessor(130279)
    FinalRewardPreview = DynAccessor(130280)
    TankmenScreen = DynAccessor(130281)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(130283)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(130284)
        Vehicle = DynAccessor(130285)

    contextMenu = _contextMenu(130286)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(130288)
        WeeklyMissions = DynAccessor(130289)
        PersonalMissions = DynAccessor(130290)
        BattlePass = DynAccessor(130291)
        Prestige = DynAccessor(130292)
        BattleMatters = DynAccessor(130293)
        ModuleVehicleUnlocks = DynAccessor(130294)
        CommonQuests = DynAccessor(130295)
        Challenges = DynAccessor(130296)

    progression = _progression(130297)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(130299)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(130300)

    contextMenu = _contextMenu(130301)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(130302)
        Wulf = DynAccessor(130303)
        Param = DynAccessor(130304)

    tooltip = _tooltip(130305)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(130306)

    popOver = _popOver(130307)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(130308)

    shared = _shared(130309)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(130311)
        VehiclesStatistics = DynAccessor(130312)
        Consumables = DynAccessor(130313)
        Equipments = DynAccessor(130314)
        Instructions = DynAccessor(130315)
        Shells = DynAccessor(130316)
        Loadout = DynAccessor(130317)
        Crew = DynAccessor(130318)
        VehicleParams = DynAccessor(130319)
        ETEVehicleParams = DynAccessor(130320)
        CurrentVehicle = DynAccessor(130321)
        VehiclesInventory = DynAccessor(130322)
        MainMenu = DynAccessor(130323)
        VehicleMenu = DynAccessor(130324)
        LootboxEntryPoint = DynAccessor(130325)
        VehicleFilters = DynAccessor(130326)
        VehiclePlaylists = DynAccessor(130327)
        Teaser = DynAccessor(130328)
        OptionalDevicesAssistant = DynAccessor(130329)
        SpaceInteraction = DynAccessor(130330)
        HeroTank = DynAccessor(130331)
        UserMissions = DynAccessor(130332)
        ModeState = DynAccessor(130333)
        EasyTankEquip = DynAccessor(130334)
        PetEvent = DynAccessor(130335)
        PetObjectTooltip = DynAccessor(130336)
        Settings = DynAccessor(130337)
        KeyBindings = DynAccessor(130338)
        ManageableVehiclePlaylists = DynAccessor(130339)

    shared = _shared(130340)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(130342)
        ContactsList = DynAccessor(130343)
        SessionStats = DynAccessor(130344)
        VehicleCompare = DynAccessor(130345)
        NotificationsCenter = DynAccessor(130346)
        Chats = DynAccessor(130347)
        ReferralProgram = DynAccessor(130348)
        ServerInfo = DynAccessor(130349)

    default = _default(130350)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(130352)
        NavigationBar = DynAccessor(130353)
        Prebattle = DynAccessor(130354)
        Wallet = DynAccessor(130355)
        AccountDashboard = DynAccessor(130356)
        HeaderState = DynAccessor(130357)
        UserAccount = DynAccessor(130358)
        ReservesEntryPoint = DynAccessor(130359)
        PremShop = DynAccessor(130360)
        CurrentVehicle = DynAccessor(130361)

    default = _default(130362)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(130364)
        VehiclesInventory = DynAccessor(130365)
        VehiclesStatistics = DynAccessor(130366)
        VehicleFilters = DynAccessor(130367)
        VehiclePlaylists = DynAccessor(130368)

    select_vehicle = _select_vehicle(130369)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(130371)
            Instructions = DynAccessor(130372)
            Shells = DynAccessor(130373)
            Consumables = DynAccessor(130374)

        Loadout = _Loadout(130375)
        Vehicles = DynAccessor(130376)

    Hangar = _Hangar(130377)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(130379)
        Events = DynAccessor(130380)
        Quests = DynAccessor(130381)
        EventMainInfoTip = DynAccessor(130382)

    hangarWidget = _hangarWidget(130383)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(130384)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(130385)
                DailyBlock = DynAccessor(130386)
                PremiumBlock = DynAccessor(130387)
                RewardProgressBlock = DynAccessor(130388)

            DailyMissionsSection = _DailyMissionsSection(130389)
            WeeklyMissions = DynAccessor(130390)
            PersonalMissions = DynAccessor(130391)

        basicMissions = _basicMissions(130392)

        class _challengeMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(130393)

        challengeMissions = _challengeMissions(130394)

    hub = _hub(130395)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(130397)
        Wallet = DynAccessor(130398)
        VehicleInfo = DynAccessor(130399)
        ManageableVehiclePlaylists = DynAccessor(130400)
        VehiclesInfo = DynAccessor(130401)
        VehiclesStatistics = DynAccessor(130402)
        VehicleFilters = DynAccessor(130403)
        VehiclePlaylists = DynAccessor(130404)
        VehiclesInventory = DynAccessor(130405)

    default = _default(130406)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(130408)
        CrewAutoReturn = DynAccessor(130409)
        CrewRetrain = DynAccessor(130410)
        QuickTraining = DynAccessor(130411)
        CrewOut = DynAccessor(130412)
        CrewBack = DynAccessor(130413)
        EasyEquip = DynAccessor(130414)
        ArmorInspector = DynAccessor(130415)
        FieldModification = DynAccessor(130416)
        NationChange = DynAccessor(130417)
        Research = DynAccessor(130418)
        AboutVehicle = DynAccessor(130419)
        Compare = DynAccessor(130420)
        Repairs = DynAccessor(130421)
        VehSkillTree = DynAccessor(130422)
        ProBoost = DynAccessor(130423)

    default = _default(130424)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(130426)
        ConsumablesPanel = DynAccessor(130427)
        Progression = DynAccessor(130428)
        Crewman = DynAccessor(130429)
        VehicleStats = DynAccessor(130430)
        ProgressionContent = DynAccessor(130431)
        ProgressionQuests = DynAccessor(130432)
        LootboxEntryPoint = DynAccessor(130433)

    shared = _shared(130434)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(130436)
    UserMissions = DynAccessor(130437)
    VehiclesInventory = DynAccessor(130438)
    VehiclesFilter = DynAccessor(130439)
    AlertMessage = DynAccessor(130440)
    Header = DynAccessor(130441)
    LoadoutPanelContainer = DynAccessor(130442)
    Events = DynAccessor(130443)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(130444)
        EventShop = DynAccessor(130445)

    hangarWidget = _hangarWidget(130446)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(130447)
        Commander = DynAccessor(130448)

    loadoutPanelContainer = _loadoutPanelContainer(130449)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(130451)
        Schedule = DynAccessor(130452)
        SeasonModifier = DynAccessor(130453)
        RoleSkillSlot = DynAccessor(130454)
        UserMissions = DynAccessor(130455)
        EntryPoint = DynAccessor(130456)
        WeeklyQuestsWidget = DynAccessor(130457)
        BattleResultsWeeklyQuests = DynAccessor(130458)
        BattleResultsCustomizationQuests = DynAccessor(130459)

    shared = _shared(130460)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(130462)
        SeasonModifier = DynAccessor(130463)
        RoleSkillSlot = DynAccessor(130464)
        UserMissions = DynAccessor(130465)
        EntryPoint = DynAccessor(130466)
        Quests = DynAccessor(130467)
        BattleResultsProgressionQuests = DynAccessor(130468)

    shared = _shared(130469)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(130471)

    loadout = _loadout(130472)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(130473)
        AlertMessage = DynAccessor(130474)

    shared = _shared(130475)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(130477)
        ProgressionEntryPoint = DynAccessor(130478)
        ProgressionQuests = DynAccessor(130479)

    shared = _shared(130480)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(130482)
        Difficulty = DynAccessor(130483)
        MoneyBalance = DynAccessor(130484)
        TeamStats = DynAccessor(130485)
        Meta = DynAccessor(130486)
        Keys = DynAccessor(130487)
        Quests = DynAccessor(130488)
        RewardPath = DynAccessor(130489)
        Shop = DynAccessor(130490)
        Gsw = DynAccessor(130491)
        Switcher = DynAccessor(130492)
        PresetsSwitcher = DynAccessor(130493)
        VehiclesDaily = DynAccessor(130494)
        BundleCard = DynAccessor(130495)
        DailyCard = DynAccessor(130496)
        Parallax = DynAccessor(130497)

    shared = _shared(130498)


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