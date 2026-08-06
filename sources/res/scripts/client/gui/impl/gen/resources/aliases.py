from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(130452)

    shared = _shared(130453)


class battle_pass(DynAccessor):
    __slots__ = ()
    ChapterChoice = DynAccessor(130455)
    Progression = DynAccessor(130456)
    PostProgression = DynAccessor(130457)
    BuyPass = DynAccessor(130458)
    BuyPassRewards = DynAccessor(130459)
    BuyLevels = DynAccessor(130460)
    BuyLevelsRewards = DynAccessor(130461)
    HolidayFinal = DynAccessor(130462)
    FinalRewardPreview = DynAccessor(130463)
    TankmenScreen = DynAccessor(130464)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(130466)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(130467)
        Vehicle = DynAccessor(130468)

    contextMenu = _contextMenu(130469)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(130471)
        WeeklyMissions = DynAccessor(130472)
        PersonalMissions = DynAccessor(130473)
        BattlePass = DynAccessor(130474)
        Prestige = DynAccessor(130475)
        BattleMatters = DynAccessor(130476)
        ModuleVehicleUnlocks = DynAccessor(130477)
        CommonQuests = DynAccessor(130478)
        Challenges = DynAccessor(130479)

    progression = _progression(130480)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(130482)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(130483)

    contextMenu = _contextMenu(130484)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(130485)
        Wulf = DynAccessor(130486)
        Param = DynAccessor(130487)

    tooltip = _tooltip(130488)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(130489)

    popOver = _popOver(130490)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(130491)

    shared = _shared(130492)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(130494)
        VehiclesStatistics = DynAccessor(130495)
        Consumables = DynAccessor(130496)
        Equipments = DynAccessor(130497)
        Instructions = DynAccessor(130498)
        Shells = DynAccessor(130499)
        Loadout = DynAccessor(130500)
        Crew = DynAccessor(130501)
        VehicleParams = DynAccessor(130502)
        ETEVehicleParams = DynAccessor(130503)
        CurrentVehicle = DynAccessor(130504)
        VehiclesInventory = DynAccessor(130505)
        MainMenu = DynAccessor(130506)
        VehicleMenu = DynAccessor(130507)
        LootboxEntryPoint = DynAccessor(130508)
        VehicleFilters = DynAccessor(130509)
        VehiclePlaylists = DynAccessor(130510)
        Teaser = DynAccessor(130511)
        OptionalDevicesAssistant = DynAccessor(130512)
        SpaceInteraction = DynAccessor(130513)
        HeroTank = DynAccessor(130514)
        UserMissions = DynAccessor(130515)
        ModeState = DynAccessor(130516)
        EasyTankEquip = DynAccessor(130517)
        PetEvent = DynAccessor(130518)
        PetObjectTooltip = DynAccessor(130519)
        Settings = DynAccessor(130520)
        KeyBindings = DynAccessor(130521)
        ManageableVehiclePlaylists = DynAccessor(130522)

    shared = _shared(130523)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(130525)
        ContactsList = DynAccessor(130526)
        SessionStats = DynAccessor(130527)
        VehicleCompare = DynAccessor(130528)
        NotificationsCenter = DynAccessor(130529)
        Chats = DynAccessor(130530)
        ReferralProgram = DynAccessor(130531)
        ServerInfo = DynAccessor(130532)

    default = _default(130533)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(130535)
        NavigationBar = DynAccessor(130536)
        Prebattle = DynAccessor(130537)
        Wallet = DynAccessor(130538)
        AccountDashboard = DynAccessor(130539)
        HeaderState = DynAccessor(130540)
        UserAccount = DynAccessor(130541)
        ReservesEntryPoint = DynAccessor(130542)
        PremShop = DynAccessor(130543)
        CurrentVehicle = DynAccessor(130544)

    default = _default(130545)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(130547)
        VehiclesInventory = DynAccessor(130548)
        VehiclesStatistics = DynAccessor(130549)
        VehicleFilters = DynAccessor(130550)
        VehiclePlaylists = DynAccessor(130551)

    select_vehicle = _select_vehicle(130552)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(130554)
            Instructions = DynAccessor(130555)
            Shells = DynAccessor(130556)
            Consumables = DynAccessor(130557)

        Loadout = _Loadout(130558)
        Vehicles = DynAccessor(130559)

    Hangar = _Hangar(130560)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(130562)
        Events = DynAccessor(130563)
        Quests = DynAccessor(130564)
        EventMainInfoTip = DynAccessor(130565)

    hangarWidget = _hangarWidget(130566)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(130567)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(130568)
                DailyBlock = DynAccessor(130569)
                PremiumBlock = DynAccessor(130570)
                RewardProgressBlock = DynAccessor(130571)

            DailyMissionsSection = _DailyMissionsSection(130572)
            WeeklyMissions = DynAccessor(130573)
            PersonalMissions = DynAccessor(130574)

        basicMissions = _basicMissions(130575)

        class _challengeMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(130576)

        challengeMissions = _challengeMissions(130577)

    hub = _hub(130578)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(130580)
        Wallet = DynAccessor(130581)
        VehicleInfo = DynAccessor(130582)
        ManageableVehiclePlaylists = DynAccessor(130583)
        VehiclesInfo = DynAccessor(130584)
        VehiclesStatistics = DynAccessor(130585)
        VehicleFilters = DynAccessor(130586)
        VehiclePlaylists = DynAccessor(130587)
        VehiclesInventory = DynAccessor(130588)

    default = _default(130589)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(130591)
        CrewAutoReturn = DynAccessor(130592)
        CrewRetrain = DynAccessor(130593)
        QuickTraining = DynAccessor(130594)
        CrewOut = DynAccessor(130595)
        CrewBack = DynAccessor(130596)
        EasyEquip = DynAccessor(130597)
        ArmorInspector = DynAccessor(130598)
        FieldModification = DynAccessor(130599)
        NationChange = DynAccessor(130600)
        Research = DynAccessor(130601)
        AboutVehicle = DynAccessor(130602)
        Compare = DynAccessor(130603)
        Repairs = DynAccessor(130604)
        VehSkillTree = DynAccessor(130605)
        ProBoost = DynAccessor(130606)

    default = _default(130607)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(130609)
        ConsumablesPanel = DynAccessor(130610)
        Progression = DynAccessor(130611)
        Crewman = DynAccessor(130612)
        VehicleStats = DynAccessor(130613)
        ProgressionContent = DynAccessor(130614)
        ProgressionQuests = DynAccessor(130615)
        LootboxEntryPoint = DynAccessor(130616)

    shared = _shared(130617)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(130619)
    UserMissions = DynAccessor(130620)
    VehiclesInventory = DynAccessor(130621)
    VehiclesFilter = DynAccessor(130622)
    AlertMessage = DynAccessor(130623)
    Header = DynAccessor(130624)
    LoadoutPanelContainer = DynAccessor(130625)
    Events = DynAccessor(130626)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(130627)
        EventShop = DynAccessor(130628)

    hangarWidget = _hangarWidget(130629)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(130630)
        Commander = DynAccessor(130631)

    loadoutPanelContainer = _loadoutPanelContainer(130632)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(130634)
        Schedule = DynAccessor(130635)
        SeasonModifier = DynAccessor(130636)
        RoleSkillSlot = DynAccessor(130637)
        UserMissions = DynAccessor(130638)
        EntryPoint = DynAccessor(130639)
        WeeklyQuestsWidget = DynAccessor(130640)
        BattleResultsWeeklyQuests = DynAccessor(130641)
        BattleResultsCustomizationQuests = DynAccessor(130642)

    shared = _shared(130643)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(130645)
        SeasonModifier = DynAccessor(130646)
        RoleSkillSlot = DynAccessor(130647)
        UserMissions = DynAccessor(130648)
        EntryPoint = DynAccessor(130649)
        Quests = DynAccessor(130650)
        BattleResultsProgressionQuests = DynAccessor(130651)

    shared = _shared(130652)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(130654)

    loadout = _loadout(130655)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(130656)
        AlertMessage = DynAccessor(130657)

    shared = _shared(130658)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(130660)
        ProgressionEntryPoint = DynAccessor(130661)
        ProgressionQuests = DynAccessor(130662)

    shared = _shared(130663)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(130665)
        Difficulty = DynAccessor(130666)
        MoneyBalance = DynAccessor(130667)
        TeamStats = DynAccessor(130668)
        Meta = DynAccessor(130669)
        Keys = DynAccessor(130670)
        Quests = DynAccessor(130671)
        RewardPath = DynAccessor(130672)
        Shop = DynAccessor(130673)
        Gsw = DynAccessor(130674)
        Switcher = DynAccessor(130675)
        PresetsSwitcher = DynAccessor(130676)
        VehiclesDaily = DynAccessor(130677)
        BundleCard = DynAccessor(130678)
        DailyCard = DynAccessor(130679)
        Parallax = DynAccessor(130680)

    shared = _shared(130681)


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