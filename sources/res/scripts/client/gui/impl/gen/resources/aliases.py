from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(125296)

    shared = _shared(125297)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(125299)
    ExtraVideo = DynAccessor(125300)
    Intro = DynAccessor(125301)
    ChapterChoice = DynAccessor(125302)
    Progression = DynAccessor(125303)
    PostProgression = DynAccessor(125304)
    BuyPass = DynAccessor(125305)
    BuyPassRewards = DynAccessor(125306)
    BuyLevels = DynAccessor(125307)
    BuyLevelsRewards = DynAccessor(125308)
    HolidayFinal = DynAccessor(125309)
    FinalRewardPreview = DynAccessor(125310)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(125312)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(125313)
        Vehicle = DynAccessor(125314)

    contextMenu = _contextMenu(125315)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(125317)
        WeeklyMissions = DynAccessor(125318)
        PersonalMissions = DynAccessor(125319)
        BattlePass = DynAccessor(125320)
        Prestige = DynAccessor(125321)
        BattleMatters = DynAccessor(125322)
        ModuleVehicleUnlocks = DynAccessor(125323)
        CommonQuests = DynAccessor(125324)

    progression = _progression(125325)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(125327)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125328)

    contextMenu = _contextMenu(125329)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125330)
        Wulf = DynAccessor(125331)
        Param = DynAccessor(125332)

    tooltip = _tooltip(125333)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125334)

    popOver = _popOver(125335)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(125336)

    shared = _shared(125337)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(125339)
        VehiclesStatistics = DynAccessor(125340)
        Consumables = DynAccessor(125341)
        Equipments = DynAccessor(125342)
        Instructions = DynAccessor(125343)
        Shells = DynAccessor(125344)
        Loadout = DynAccessor(125345)
        Crew = DynAccessor(125346)
        VehicleParams = DynAccessor(125347)
        ETEVehicleParams = DynAccessor(125348)
        CurrentVehicle = DynAccessor(125349)
        VehiclesInventory = DynAccessor(125350)
        MainMenu = DynAccessor(125351)
        VehicleMenu = DynAccessor(125352)
        LootboxEntryPoint = DynAccessor(125353)
        VehicleFilters = DynAccessor(125354)
        VehiclePlaylists = DynAccessor(125355)
        Teaser = DynAccessor(125356)
        OptionalDevicesAssistant = DynAccessor(125357)
        SpaceInteraction = DynAccessor(125358)
        HeroTank = DynAccessor(125359)
        UserMissions = DynAccessor(125360)
        ModeState = DynAccessor(125361)
        EasyTankEquip = DynAccessor(125362)
        PetEvent = DynAccessor(125363)
        PetObjectTooltip = DynAccessor(125364)
        Settings = DynAccessor(125365)
        KeyBindings = DynAccessor(125366)
        ManageableVehiclePlaylists = DynAccessor(125367)

    shared = _shared(125368)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(125370)
        ContactsList = DynAccessor(125371)
        SessionStats = DynAccessor(125372)
        VehicleCompare = DynAccessor(125373)
        NotificationsCenter = DynAccessor(125374)
        Chats = DynAccessor(125375)
        ReferralProgram = DynAccessor(125376)
        ServerInfo = DynAccessor(125377)

    default = _default(125378)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(125380)
        NavigationBar = DynAccessor(125381)
        Prebattle = DynAccessor(125382)
        Wallet = DynAccessor(125383)
        AccountDashboard = DynAccessor(125384)
        HeaderState = DynAccessor(125385)
        UserAccount = DynAccessor(125386)
        ReservesEntryPoint = DynAccessor(125387)
        PremShop = DynAccessor(125388)
        CurrentVehicle = DynAccessor(125389)

    default = _default(125390)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(125392)
        VehiclesInventory = DynAccessor(125393)
        VehiclesStatistics = DynAccessor(125394)
        VehicleFilters = DynAccessor(125395)
        VehiclePlaylists = DynAccessor(125396)

    select_vehicle = _select_vehicle(125397)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(125399)
            Instructions = DynAccessor(125400)
            Shells = DynAccessor(125401)
            Consumables = DynAccessor(125402)

        Loadout = _Loadout(125403)
        Vehicles = DynAccessor(125404)

    Hangar = _Hangar(125405)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(125407)
        Events = DynAccessor(125408)
        Quests = DynAccessor(125409)
        EventMainInfoTip = DynAccessor(125410)

    hangarWidget = _hangarWidget(125411)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(125412)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(125413)
                DailyBlock = DynAccessor(125414)
                PremiumBlock = DynAccessor(125415)
                RewardProgressBlock = DynAccessor(125416)

            DailyMissionsSection = _DailyMissionsSection(125417)
            WeeklyMissions = DynAccessor(125418)
            PersonalMissions = DynAccessor(125419)

        basicMissions = _basicMissions(125420)

    hub = _hub(125421)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(125423)
        Wallet = DynAccessor(125424)
        VehicleInfo = DynAccessor(125425)
        ManageableVehiclePlaylists = DynAccessor(125426)
        VehiclesInfo = DynAccessor(125427)
        VehiclesStatistics = DynAccessor(125428)
        VehicleFilters = DynAccessor(125429)
        VehiclePlaylists = DynAccessor(125430)
        VehiclesInventory = DynAccessor(125431)

    default = _default(125432)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(125434)
        CrewAutoReturn = DynAccessor(125435)
        CrewRetrain = DynAccessor(125436)
        QuickTraining = DynAccessor(125437)
        CrewOut = DynAccessor(125438)
        CrewBack = DynAccessor(125439)
        EasyEquip = DynAccessor(125440)
        ArmorInspector = DynAccessor(125441)
        FieldModification = DynAccessor(125442)
        NationChange = DynAccessor(125443)
        Research = DynAccessor(125444)
        AboutVehicle = DynAccessor(125445)
        Compare = DynAccessor(125446)
        Repairs = DynAccessor(125447)
        VehSkillTree = DynAccessor(125448)
        ProBoost = DynAccessor(125449)

    default = _default(125450)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(125452)
        ConsumablesPanel = DynAccessor(125453)
        Progression = DynAccessor(125454)
        Crewman = DynAccessor(125455)
        VehicleStats = DynAccessor(125456)
        ProgressionContent = DynAccessor(125457)
        ProgressionQuests = DynAccessor(125458)
        LootboxEntryPoint = DynAccessor(125459)

    shared = _shared(125460)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(125462)
    UserMissions = DynAccessor(125463)
    VehiclesInventory = DynAccessor(125464)
    VehiclesFilter = DynAccessor(125465)
    AlertMessage = DynAccessor(125466)
    Header = DynAccessor(125467)
    LoadoutPanelContainer = DynAccessor(125468)
    Events = DynAccessor(125469)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(125470)
        EventShop = DynAccessor(125471)

    hangarWidget = _hangarWidget(125472)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(125473)
        Commander = DynAccessor(125474)

    loadoutPanelContainer = _loadoutPanelContainer(125475)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(125477)
        Schedule = DynAccessor(125478)
        SeasonModifier = DynAccessor(125479)
        RoleSkillSlot = DynAccessor(125480)
        UserMissions = DynAccessor(125481)
        EntryPoint = DynAccessor(125482)
        WeeklyQuestsWidget = DynAccessor(125483)

    shared = _shared(125484)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(125486)
        SeasonModifier = DynAccessor(125487)
        RoleSkillSlot = DynAccessor(125488)
        UserMissions = DynAccessor(125489)
        EntryPoint = DynAccessor(125490)
        Quests = DynAccessor(125491)

    shared = _shared(125492)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(125494)

    loadout = _loadout(125495)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(125496)
        AlertMessage = DynAccessor(125497)

    shared = _shared(125498)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(125500)
        ProgressionEntryPoint = DynAccessor(125501)

    shared = _shared(125502)


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