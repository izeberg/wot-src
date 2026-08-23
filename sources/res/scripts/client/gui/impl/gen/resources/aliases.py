from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(131339)

    shared = _shared(131340)


class battle_pass(DynAccessor):
    __slots__ = ()
    ChapterChoice = DynAccessor(131342)
    Progression = DynAccessor(131343)
    PostProgression = DynAccessor(131344)
    BuyPass = DynAccessor(131345)
    BuyPassRewards = DynAccessor(131346)
    BuyLevels = DynAccessor(131347)
    BuyLevelsRewards = DynAccessor(131348)
    HolidayFinal = DynAccessor(131349)
    FinalRewardPreview = DynAccessor(131350)
    TankmenScreen = DynAccessor(131351)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(131353)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(131354)
        Vehicle = DynAccessor(131355)

    contextMenu = _contextMenu(131356)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(131358)
        WeeklyMissions = DynAccessor(131359)
        PersonalMissions = DynAccessor(131360)
        BattlePass = DynAccessor(131361)
        Prestige = DynAccessor(131362)
        BattleMatters = DynAccessor(131363)
        ModuleVehicleUnlocks = DynAccessor(131364)
        CommonQuests = DynAccessor(131365)
        Challenges = DynAccessor(131366)

    progression = _progression(131367)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(131369)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(131370)

    contextMenu = _contextMenu(131371)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(131372)
        Wulf = DynAccessor(131373)
        Param = DynAccessor(131374)

    tooltip = _tooltip(131375)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(131376)

    popOver = _popOver(131377)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(131378)

    shared = _shared(131379)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(131381)
        VehiclesStatistics = DynAccessor(131382)
        Consumables = DynAccessor(131383)
        Equipments = DynAccessor(131384)
        Instructions = DynAccessor(131385)
        Shells = DynAccessor(131386)
        Loadout = DynAccessor(131387)
        Crew = DynAccessor(131388)
        VehicleParams = DynAccessor(131389)
        ETEVehicleParams = DynAccessor(131390)
        CurrentVehicle = DynAccessor(131391)
        VehiclesInventory = DynAccessor(131392)
        MainMenu = DynAccessor(131393)
        VehicleMenu = DynAccessor(131394)
        LootboxEntryPoint = DynAccessor(131395)
        VehicleFilters = DynAccessor(131396)
        VehiclePlaylists = DynAccessor(131397)
        Teaser = DynAccessor(131398)
        OptionalDevicesAssistant = DynAccessor(131399)
        SpaceInteraction = DynAccessor(131400)
        HeroTank = DynAccessor(131401)
        UserMissions = DynAccessor(131402)
        ModeState = DynAccessor(131403)
        EasyTankEquip = DynAccessor(131404)
        PetEvent = DynAccessor(131405)
        PetObjectTooltip = DynAccessor(131406)
        Settings = DynAccessor(131407)
        KeyBindings = DynAccessor(131408)
        ManageableVehiclePlaylists = DynAccessor(131409)

    shared = _shared(131410)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(131412)
        ContactsList = DynAccessor(131413)
        SessionStats = DynAccessor(131414)
        VehicleCompare = DynAccessor(131415)
        NotificationsCenter = DynAccessor(131416)
        Chats = DynAccessor(131417)
        ReferralProgram = DynAccessor(131418)
        ServerInfo = DynAccessor(131419)

    default = _default(131420)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(131422)
        NavigationBar = DynAccessor(131423)
        Prebattle = DynAccessor(131424)
        Wallet = DynAccessor(131425)
        AccountDashboard = DynAccessor(131426)
        HeaderState = DynAccessor(131427)
        UserAccount = DynAccessor(131428)
        ReservesEntryPoint = DynAccessor(131429)
        PremShop = DynAccessor(131430)
        CurrentVehicle = DynAccessor(131431)

    default = _default(131432)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(131434)
        VehiclesInventory = DynAccessor(131435)
        VehiclesStatistics = DynAccessor(131436)
        VehicleFilters = DynAccessor(131437)
        VehiclePlaylists = DynAccessor(131438)

    select_vehicle = _select_vehicle(131439)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(131441)
            Instructions = DynAccessor(131442)
            Shells = DynAccessor(131443)
            Consumables = DynAccessor(131444)

        Loadout = _Loadout(131445)
        Vehicles = DynAccessor(131446)

    Hangar = _Hangar(131447)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(131449)
        Events = DynAccessor(131450)
        Quests = DynAccessor(131451)
        EventMainInfoTip = DynAccessor(131452)

    hangarWidget = _hangarWidget(131453)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(131454)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(131455)
                DailyBlock = DynAccessor(131456)
                PremiumBlock = DynAccessor(131457)
                RewardProgressBlock = DynAccessor(131458)

            DailyMissionsSection = _DailyMissionsSection(131459)
            WeeklyMissions = DynAccessor(131460)
            PersonalMissions = DynAccessor(131461)

        basicMissions = _basicMissions(131462)

        class _challengeMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(131463)

        challengeMissions = _challengeMissions(131464)

    hub = _hub(131465)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(131467)
        Wallet = DynAccessor(131468)
        VehicleInfo = DynAccessor(131469)
        ManageableVehiclePlaylists = DynAccessor(131470)
        VehiclesInfo = DynAccessor(131471)
        VehiclesStatistics = DynAccessor(131472)
        VehicleFilters = DynAccessor(131473)
        VehiclePlaylists = DynAccessor(131474)
        VehiclesInventory = DynAccessor(131475)

    default = _default(131476)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(131478)
        CrewAutoReturn = DynAccessor(131479)
        CrewRetrain = DynAccessor(131480)
        QuickTraining = DynAccessor(131481)
        CrewOut = DynAccessor(131482)
        CrewBack = DynAccessor(131483)
        EasyEquip = DynAccessor(131484)
        ArmorInspector = DynAccessor(131485)
        FieldModification = DynAccessor(131486)
        NationChange = DynAccessor(131487)
        Research = DynAccessor(131488)
        AboutVehicle = DynAccessor(131489)
        Compare = DynAccessor(131490)
        Repairs = DynAccessor(131491)
        VehSkillTree = DynAccessor(131492)
        ProBoost = DynAccessor(131493)

    default = _default(131494)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(131496)
        ConsumablesPanel = DynAccessor(131497)
        Progression = DynAccessor(131498)
        Crewman = DynAccessor(131499)
        VehicleStats = DynAccessor(131500)
        ProgressionContent = DynAccessor(131501)
        ProgressionQuests = DynAccessor(131502)
        LootboxEntryPoint = DynAccessor(131503)

    shared = _shared(131504)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(131506)
    UserMissions = DynAccessor(131507)
    VehiclesInventory = DynAccessor(131508)
    VehiclesFilter = DynAccessor(131509)
    AlertMessage = DynAccessor(131510)
    Header = DynAccessor(131511)
    LoadoutPanelContainer = DynAccessor(131512)
    Events = DynAccessor(131513)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(131514)
        EventShop = DynAccessor(131515)

    hangarWidget = _hangarWidget(131516)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(131517)
        Commander = DynAccessor(131518)

    loadoutPanelContainer = _loadoutPanelContainer(131519)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(131521)
        Schedule = DynAccessor(131522)
        SeasonModifier = DynAccessor(131523)
        RoleSkillSlot = DynAccessor(131524)
        UserMissions = DynAccessor(131525)
        EntryPoint = DynAccessor(131526)
        WeeklyQuestsWidget = DynAccessor(131527)
        BattleResultsWeeklyQuests = DynAccessor(131528)
        BattleResultsCustomizationQuests = DynAccessor(131529)

    shared = _shared(131530)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(131532)
        SeasonModifier = DynAccessor(131533)
        RoleSkillSlot = DynAccessor(131534)
        UserMissions = DynAccessor(131535)
        EntryPoint = DynAccessor(131536)
        Quests = DynAccessor(131537)
        BattleResultsProgressionQuests = DynAccessor(131538)

    shared = _shared(131539)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(131541)

    loadout = _loadout(131542)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(131543)
        AlertMessage = DynAccessor(131544)

    shared = _shared(131545)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(131547)
        ProgressionEntryPoint = DynAccessor(131548)
        ProgressionQuests = DynAccessor(131549)

    shared = _shared(131550)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(131552)
        Difficulty = DynAccessor(131553)
        MoneyBalance = DynAccessor(131554)
        TeamStats = DynAccessor(131555)
        Meta = DynAccessor(131556)
        Keys = DynAccessor(131557)
        Quests = DynAccessor(131558)
        RewardPath = DynAccessor(131559)
        Shop = DynAccessor(131560)
        Gsw = DynAccessor(131561)
        Switcher = DynAccessor(131562)
        PresetsSwitcher = DynAccessor(131563)
        VehiclesDaily = DynAccessor(131564)
        BundleCard = DynAccessor(131565)
        DailyCard = DynAccessor(131566)
        Parallax = DynAccessor(131567)

    shared = _shared(131568)


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