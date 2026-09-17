from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(135415)

    shared = _shared(135416)


class battle_pass(DynAccessor):
    __slots__ = ()
    ChapterChoice = DynAccessor(135418)
    Progression = DynAccessor(135419)
    PostProgression = DynAccessor(135420)
    BuyPass = DynAccessor(135421)
    BuyPassRewards = DynAccessor(135422)
    BuyLevels = DynAccessor(135423)
    BuyLevelsRewards = DynAccessor(135424)
    HolidayFinal = DynAccessor(135425)
    FinalRewardPreview = DynAccessor(135426)
    TankmenScreen = DynAccessor(135427)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(135429)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(135430)
        Vehicle = DynAccessor(135431)

    contextMenu = _contextMenu(135432)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(135434)
        WeeklyMissions = DynAccessor(135435)
        PersonalMissions = DynAccessor(135436)
        BattlePass = DynAccessor(135437)
        Prestige = DynAccessor(135438)
        BattleMatters = DynAccessor(135439)
        ModuleVehicleUnlocks = DynAccessor(135440)
        CommonQuests = DynAccessor(135441)
        Challenges = DynAccessor(135442)

    progression = _progression(135443)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(135445)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(135446)

    contextMenu = _contextMenu(135447)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(135448)
        Wulf = DynAccessor(135449)
        Param = DynAccessor(135450)

    tooltip = _tooltip(135451)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(135452)

    popOver = _popOver(135453)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(135454)

    shared = _shared(135455)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(135457)
        VehiclesStatistics = DynAccessor(135458)
        Consumables = DynAccessor(135459)
        Equipments = DynAccessor(135460)
        Instructions = DynAccessor(135461)
        Shells = DynAccessor(135462)
        Loadout = DynAccessor(135463)
        Crew = DynAccessor(135464)
        VehicleParams = DynAccessor(135465)
        ETEVehicleParams = DynAccessor(135466)
        CurrentVehicle = DynAccessor(135467)
        VehiclesInventory = DynAccessor(135468)
        MainMenu = DynAccessor(135469)
        VehicleMenu = DynAccessor(135470)
        LootboxEntryPoint = DynAccessor(135471)
        VehicleFilters = DynAccessor(135472)
        VehiclePlaylists = DynAccessor(135473)
        Teaser = DynAccessor(135474)
        OptionalDevicesAssistant = DynAccessor(135475)
        SpaceInteraction = DynAccessor(135476)
        HeroTank = DynAccessor(135477)
        UserMissions = DynAccessor(135478)
        ModeState = DynAccessor(135479)
        EasyTankEquip = DynAccessor(135480)
        PetEvent = DynAccessor(135481)
        PetObjectTooltip = DynAccessor(135482)
        Settings = DynAccessor(135483)
        KeyBindings = DynAccessor(135484)
        ManageableVehiclePlaylists = DynAccessor(135485)
        MainPlugins = DynAccessor(135486)

    shared = _shared(135487)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(135489)
        ContactsList = DynAccessor(135490)
        SessionStats = DynAccessor(135491)
        VehicleCompare = DynAccessor(135492)
        NotificationsCenter = DynAccessor(135493)
        Chats = DynAccessor(135494)
        ReferralProgram = DynAccessor(135495)
        ServerInfo = DynAccessor(135496)

    default = _default(135497)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(135499)
        NavigationBar = DynAccessor(135500)
        Prebattle = DynAccessor(135501)
        Wallet = DynAccessor(135502)
        AccountDashboard = DynAccessor(135503)
        HeaderState = DynAccessor(135504)
        UserAccount = DynAccessor(135505)
        ReservesEntryPoint = DynAccessor(135506)
        PremShop = DynAccessor(135507)
        CurrentVehicle = DynAccessor(135508)

    default = _default(135509)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(135511)
        VehiclesInventory = DynAccessor(135512)
        VehiclesStatistics = DynAccessor(135513)
        VehicleFilters = DynAccessor(135514)
        VehiclePlaylists = DynAccessor(135515)

    select_vehicle = _select_vehicle(135516)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(135518)
            Instructions = DynAccessor(135519)
            Shells = DynAccessor(135520)
            Consumables = DynAccessor(135521)

        Loadout = _Loadout(135522)
        Vehicles = DynAccessor(135523)

    Hangar = _Hangar(135524)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(135526)
        Events = DynAccessor(135527)
        Quests = DynAccessor(135528)
        PersonalMissions = DynAccessor(135529)
        EventMainInfoTip = DynAccessor(135530)

    hangarWidget = _hangarWidget(135531)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(135532)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(135533)
                DailyBlock = DynAccessor(135534)
                PremiumBlock = DynAccessor(135535)
                RewardProgressBlock = DynAccessor(135536)

            DailyMissionsSection = _DailyMissionsSection(135537)
            WeeklyMissions = DynAccessor(135538)
            PersonalMissions = DynAccessor(135539)

        basicMissions = _basicMissions(135540)

        class _challengeMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(135541)

        challengeMissions = _challengeMissions(135542)

    hub = _hub(135543)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(135545)
        Wallet = DynAccessor(135546)
        VehicleInfo = DynAccessor(135547)
        ManageableVehiclePlaylists = DynAccessor(135548)
        VehiclesInfo = DynAccessor(135549)
        VehiclesStatistics = DynAccessor(135550)
        VehicleFilters = DynAccessor(135551)
        VehiclePlaylists = DynAccessor(135552)
        VehiclesInventory = DynAccessor(135553)

    default = _default(135554)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(135556)
        CrewAutoReturn = DynAccessor(135557)
        CrewRetrain = DynAccessor(135558)
        QuickTraining = DynAccessor(135559)
        CrewOut = DynAccessor(135560)
        CrewBack = DynAccessor(135561)
        EasyEquip = DynAccessor(135562)
        ArmorInspector = DynAccessor(135563)
        FieldModification = DynAccessor(135564)
        NationChange = DynAccessor(135565)
        Research = DynAccessor(135566)
        AboutVehicle = DynAccessor(135567)
        Compare = DynAccessor(135568)
        Repairs = DynAccessor(135569)
        VehSkillTree = DynAccessor(135570)
        ProBoost = DynAccessor(135571)

    default = _default(135572)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(135574)
        ConsumablesPanel = DynAccessor(135575)
        Progression = DynAccessor(135576)
        Crewman = DynAccessor(135577)
        VehicleStats = DynAccessor(135578)
        ProgressionContent = DynAccessor(135579)
        ProgressionQuests = DynAccessor(135580)
        LootboxEntryPoint = DynAccessor(135581)

    shared = _shared(135582)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(135584)
    UserMissions = DynAccessor(135585)
    VehiclesInventory = DynAccessor(135586)
    VehiclesFilter = DynAccessor(135587)
    AlertMessage = DynAccessor(135588)
    Header = DynAccessor(135589)
    LoadoutPanelContainer = DynAccessor(135590)
    Events = DynAccessor(135591)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(135592)
        EventShop = DynAccessor(135593)

    hangarWidget = _hangarWidget(135594)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(135595)
        Commander = DynAccessor(135596)

    loadoutPanelContainer = _loadoutPanelContainer(135597)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(135599)
        Schedule = DynAccessor(135600)
        SeasonModifier = DynAccessor(135601)
        RoleSkillSlot = DynAccessor(135602)
        UserMissions = DynAccessor(135603)
        EntryPoint = DynAccessor(135604)
        WeeklyQuestsWidget = DynAccessor(135605)
        BattleResultsWeeklyQuests = DynAccessor(135606)
        BattleResultsCustomizationQuests = DynAccessor(135607)

    shared = _shared(135608)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(135610)
        SeasonModifier = DynAccessor(135611)
        RoleSkillSlot = DynAccessor(135612)
        UserMissions = DynAccessor(135613)
        EntryPoint = DynAccessor(135614)
        Quests = DynAccessor(135615)
        BattleResultsProgressionQuests = DynAccessor(135616)

    shared = _shared(135617)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(135619)

    loadout = _loadout(135620)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(135621)
        AlertMessage = DynAccessor(135622)

    shared = _shared(135623)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(135625)
        ProgressionEntryPoint = DynAccessor(135626)
        ProgressionQuests = DynAccessor(135627)

    shared = _shared(135628)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(135630)
        Difficulty = DynAccessor(135631)
        MoneyBalance = DynAccessor(135632)
        TeamStats = DynAccessor(135633)
        Meta = DynAccessor(135634)
        Keys = DynAccessor(135635)
        Quests = DynAccessor(135636)
        RewardPath = DynAccessor(135637)
        Shop = DynAccessor(135638)
        Gsw = DynAccessor(135639)
        Switcher = DynAccessor(135640)
        PresetsSwitcher = DynAccessor(135641)
        VehiclesDaily = DynAccessor(135642)
        BundleCard = DynAccessor(135643)
        DailyCard = DynAccessor(135644)
        Parallax = DynAccessor(135645)

    shared = _shared(135646)


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