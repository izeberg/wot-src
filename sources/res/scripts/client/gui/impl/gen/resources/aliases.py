from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(125397)

    shared = _shared(125398)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(125400)
    ExtraVideo = DynAccessor(125401)
    Intro = DynAccessor(125402)
    ChapterChoice = DynAccessor(125403)
    Progression = DynAccessor(125404)
    PostProgression = DynAccessor(125405)
    BuyPass = DynAccessor(125406)
    BuyPassRewards = DynAccessor(125407)
    BuyLevels = DynAccessor(125408)
    BuyLevelsRewards = DynAccessor(125409)
    HolidayFinal = DynAccessor(125410)
    FinalRewardPreview = DynAccessor(125411)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(125413)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(125414)
        Vehicle = DynAccessor(125415)

    contextMenu = _contextMenu(125416)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(125418)
        WeeklyMissions = DynAccessor(125419)
        PersonalMissions = DynAccessor(125420)
        BattlePass = DynAccessor(125421)
        Prestige = DynAccessor(125422)
        BattleMatters = DynAccessor(125423)
        ModuleVehicleUnlocks = DynAccessor(125424)
        CommonQuests = DynAccessor(125425)

    progression = _progression(125426)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(125428)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125429)

    contextMenu = _contextMenu(125430)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125431)
        Wulf = DynAccessor(125432)
        Param = DynAccessor(125433)

    tooltip = _tooltip(125434)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125435)

    popOver = _popOver(125436)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(125437)

    shared = _shared(125438)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(125440)
        VehiclesStatistics = DynAccessor(125441)
        Consumables = DynAccessor(125442)
        Equipments = DynAccessor(125443)
        Instructions = DynAccessor(125444)
        Shells = DynAccessor(125445)
        Loadout = DynAccessor(125446)
        Crew = DynAccessor(125447)
        VehicleParams = DynAccessor(125448)
        ETEVehicleParams = DynAccessor(125449)
        CurrentVehicle = DynAccessor(125450)
        VehiclesInventory = DynAccessor(125451)
        MainMenu = DynAccessor(125452)
        VehicleMenu = DynAccessor(125453)
        LootboxEntryPoint = DynAccessor(125454)
        VehicleFilters = DynAccessor(125455)
        VehiclePlaylists = DynAccessor(125456)
        Teaser = DynAccessor(125457)
        OptionalDevicesAssistant = DynAccessor(125458)
        SpaceInteraction = DynAccessor(125459)
        HeroTank = DynAccessor(125460)
        UserMissions = DynAccessor(125461)
        ModeState = DynAccessor(125462)
        EasyTankEquip = DynAccessor(125463)
        PetEvent = DynAccessor(125464)
        PetObjectTooltip = DynAccessor(125465)
        Settings = DynAccessor(125466)
        KeyBindings = DynAccessor(125467)
        ManageableVehiclePlaylists = DynAccessor(125468)

    shared = _shared(125469)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(125471)
        ContactsList = DynAccessor(125472)
        SessionStats = DynAccessor(125473)
        VehicleCompare = DynAccessor(125474)
        NotificationsCenter = DynAccessor(125475)
        Chats = DynAccessor(125476)
        ReferralProgram = DynAccessor(125477)
        ServerInfo = DynAccessor(125478)

    default = _default(125479)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(125481)
        NavigationBar = DynAccessor(125482)
        Prebattle = DynAccessor(125483)
        Wallet = DynAccessor(125484)
        AccountDashboard = DynAccessor(125485)
        HeaderState = DynAccessor(125486)
        UserAccount = DynAccessor(125487)
        ReservesEntryPoint = DynAccessor(125488)
        PremShop = DynAccessor(125489)
        CurrentVehicle = DynAccessor(125490)

    default = _default(125491)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(125493)
        VehiclesInventory = DynAccessor(125494)
        VehiclesStatistics = DynAccessor(125495)
        VehicleFilters = DynAccessor(125496)
        VehiclePlaylists = DynAccessor(125497)

    select_vehicle = _select_vehicle(125498)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(125500)
            Instructions = DynAccessor(125501)
            Shells = DynAccessor(125502)
            Consumables = DynAccessor(125503)

        Loadout = _Loadout(125504)
        Vehicles = DynAccessor(125505)

    Hangar = _Hangar(125506)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(125508)
        Events = DynAccessor(125509)
        Quests = DynAccessor(125510)
        EventMainInfoTip = DynAccessor(125511)

    hangarWidget = _hangarWidget(125512)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(125513)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(125514)
                DailyBlock = DynAccessor(125515)
                PremiumBlock = DynAccessor(125516)
                RewardProgressBlock = DynAccessor(125517)

            DailyMissionsSection = _DailyMissionsSection(125518)
            WeeklyMissions = DynAccessor(125519)
            PersonalMissions = DynAccessor(125520)

        basicMissions = _basicMissions(125521)

    hub = _hub(125522)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(125524)
        Wallet = DynAccessor(125525)
        VehicleInfo = DynAccessor(125526)
        ManageableVehiclePlaylists = DynAccessor(125527)
        VehiclesInfo = DynAccessor(125528)
        VehiclesStatistics = DynAccessor(125529)
        VehicleFilters = DynAccessor(125530)
        VehiclePlaylists = DynAccessor(125531)
        VehiclesInventory = DynAccessor(125532)

    default = _default(125533)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(125535)
        CrewAutoReturn = DynAccessor(125536)
        CrewRetrain = DynAccessor(125537)
        QuickTraining = DynAccessor(125538)
        CrewOut = DynAccessor(125539)
        CrewBack = DynAccessor(125540)
        EasyEquip = DynAccessor(125541)
        ArmorInspector = DynAccessor(125542)
        FieldModification = DynAccessor(125543)
        NationChange = DynAccessor(125544)
        Research = DynAccessor(125545)
        AboutVehicle = DynAccessor(125546)
        Compare = DynAccessor(125547)
        Repairs = DynAccessor(125548)
        VehSkillTree = DynAccessor(125549)
        ProBoost = DynAccessor(125550)

    default = _default(125551)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(125553)
        ConsumablesPanel = DynAccessor(125554)
        Progression = DynAccessor(125555)
        Crewman = DynAccessor(125556)
        VehicleStats = DynAccessor(125557)
        ProgressionContent = DynAccessor(125558)
        ProgressionQuests = DynAccessor(125559)
        LootboxEntryPoint = DynAccessor(125560)

    shared = _shared(125561)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(125563)
    UserMissions = DynAccessor(125564)
    VehiclesInventory = DynAccessor(125565)
    VehiclesFilter = DynAccessor(125566)
    AlertMessage = DynAccessor(125567)
    Header = DynAccessor(125568)
    LoadoutPanelContainer = DynAccessor(125569)
    Events = DynAccessor(125570)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(125571)
        EventShop = DynAccessor(125572)

    hangarWidget = _hangarWidget(125573)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(125574)
        Commander = DynAccessor(125575)

    loadoutPanelContainer = _loadoutPanelContainer(125576)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(125578)
        Schedule = DynAccessor(125579)
        SeasonModifier = DynAccessor(125580)
        RoleSkillSlot = DynAccessor(125581)
        UserMissions = DynAccessor(125582)
        EntryPoint = DynAccessor(125583)
        WeeklyQuestsWidget = DynAccessor(125584)

    shared = _shared(125585)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(125587)
        SeasonModifier = DynAccessor(125588)
        RoleSkillSlot = DynAccessor(125589)
        UserMissions = DynAccessor(125590)
        EntryPoint = DynAccessor(125591)
        Quests = DynAccessor(125592)

    shared = _shared(125593)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(125595)

    loadout = _loadout(125596)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(125597)
        AlertMessage = DynAccessor(125598)

    shared = _shared(125599)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(125601)
        ProgressionEntryPoint = DynAccessor(125602)

    shared = _shared(125603)


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