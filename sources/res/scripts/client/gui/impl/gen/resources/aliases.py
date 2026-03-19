from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(125633)

    shared = _shared(125634)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(125636)
    ExtraVideo = DynAccessor(125637)
    Intro = DynAccessor(125638)
    ChapterChoice = DynAccessor(125639)
    Progression = DynAccessor(125640)
    PostProgression = DynAccessor(125641)
    BuyPass = DynAccessor(125642)
    BuyPassRewards = DynAccessor(125643)
    BuyLevels = DynAccessor(125644)
    BuyLevelsRewards = DynAccessor(125645)
    HolidayFinal = DynAccessor(125646)
    FinalRewardPreview = DynAccessor(125647)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(125649)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(125650)
        Vehicle = DynAccessor(125651)

    contextMenu = _contextMenu(125652)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(125654)
        WeeklyMissions = DynAccessor(125655)
        PersonalMissions = DynAccessor(125656)
        BattlePass = DynAccessor(125657)
        Prestige = DynAccessor(125658)
        BattleMatters = DynAccessor(125659)
        ModuleVehicleUnlocks = DynAccessor(125660)
        CommonQuests = DynAccessor(125661)

    progression = _progression(125662)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(125664)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125665)

    contextMenu = _contextMenu(125666)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125667)
        Wulf = DynAccessor(125668)
        Param = DynAccessor(125669)

    tooltip = _tooltip(125670)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125671)

    popOver = _popOver(125672)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(125673)

    shared = _shared(125674)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(125676)
        VehiclesStatistics = DynAccessor(125677)
        Consumables = DynAccessor(125678)
        Equipments = DynAccessor(125679)
        Instructions = DynAccessor(125680)
        Shells = DynAccessor(125681)
        Loadout = DynAccessor(125682)
        Crew = DynAccessor(125683)
        VehicleParams = DynAccessor(125684)
        ETEVehicleParams = DynAccessor(125685)
        CurrentVehicle = DynAccessor(125686)
        VehiclesInventory = DynAccessor(125687)
        MainMenu = DynAccessor(125688)
        VehicleMenu = DynAccessor(125689)
        LootboxEntryPoint = DynAccessor(125690)
        VehicleFilters = DynAccessor(125691)
        VehiclePlaylists = DynAccessor(125692)
        Teaser = DynAccessor(125693)
        OptionalDevicesAssistant = DynAccessor(125694)
        SpaceInteraction = DynAccessor(125695)
        HeroTank = DynAccessor(125696)
        UserMissions = DynAccessor(125697)
        ModeState = DynAccessor(125698)
        EasyTankEquip = DynAccessor(125699)
        PetEvent = DynAccessor(125700)
        PetObjectTooltip = DynAccessor(125701)
        Settings = DynAccessor(125702)
        KeyBindings = DynAccessor(125703)
        ManageableVehiclePlaylists = DynAccessor(125704)

    shared = _shared(125705)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(125707)
        ContactsList = DynAccessor(125708)
        SessionStats = DynAccessor(125709)
        VehicleCompare = DynAccessor(125710)
        NotificationsCenter = DynAccessor(125711)
        Chats = DynAccessor(125712)
        ReferralProgram = DynAccessor(125713)
        ServerInfo = DynAccessor(125714)

    default = _default(125715)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(125717)
        NavigationBar = DynAccessor(125718)
        Prebattle = DynAccessor(125719)
        Wallet = DynAccessor(125720)
        AccountDashboard = DynAccessor(125721)
        HeaderState = DynAccessor(125722)
        UserAccount = DynAccessor(125723)
        ReservesEntryPoint = DynAccessor(125724)
        PremShop = DynAccessor(125725)
        CurrentVehicle = DynAccessor(125726)

    default = _default(125727)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(125729)
        VehiclesInventory = DynAccessor(125730)
        VehiclesStatistics = DynAccessor(125731)
        VehicleFilters = DynAccessor(125732)
        VehiclePlaylists = DynAccessor(125733)

    select_vehicle = _select_vehicle(125734)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(125736)
            Instructions = DynAccessor(125737)
            Shells = DynAccessor(125738)
            Consumables = DynAccessor(125739)

        Loadout = _Loadout(125740)
        Vehicles = DynAccessor(125741)

    Hangar = _Hangar(125742)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(125744)
        Events = DynAccessor(125745)
        Quests = DynAccessor(125746)
        EventMainInfoTip = DynAccessor(125747)

    hangarWidget = _hangarWidget(125748)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(125749)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(125750)
                DailyBlock = DynAccessor(125751)
                PremiumBlock = DynAccessor(125752)
                RewardProgressBlock = DynAccessor(125753)

            DailyMissionsSection = _DailyMissionsSection(125754)
            WeeklyMissions = DynAccessor(125755)
            PersonalMissions = DynAccessor(125756)

        basicMissions = _basicMissions(125757)

    hub = _hub(125758)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(125760)
        Wallet = DynAccessor(125761)
        VehicleInfo = DynAccessor(125762)
        ManageableVehiclePlaylists = DynAccessor(125763)
        VehiclesInfo = DynAccessor(125764)
        VehiclesStatistics = DynAccessor(125765)
        VehicleFilters = DynAccessor(125766)
        VehiclePlaylists = DynAccessor(125767)
        VehiclesInventory = DynAccessor(125768)

    default = _default(125769)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(125771)
        CrewAutoReturn = DynAccessor(125772)
        CrewRetrain = DynAccessor(125773)
        QuickTraining = DynAccessor(125774)
        CrewOut = DynAccessor(125775)
        CrewBack = DynAccessor(125776)
        EasyEquip = DynAccessor(125777)
        ArmorInspector = DynAccessor(125778)
        FieldModification = DynAccessor(125779)
        NationChange = DynAccessor(125780)
        Research = DynAccessor(125781)
        AboutVehicle = DynAccessor(125782)
        Compare = DynAccessor(125783)
        Repairs = DynAccessor(125784)
        VehSkillTree = DynAccessor(125785)
        ProBoost = DynAccessor(125786)

    default = _default(125787)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(125789)
        ConsumablesPanel = DynAccessor(125790)
        Progression = DynAccessor(125791)
        Crewman = DynAccessor(125792)
        VehicleStats = DynAccessor(125793)
        ProgressionContent = DynAccessor(125794)
        ProgressionQuests = DynAccessor(125795)
        LootboxEntryPoint = DynAccessor(125796)

    shared = _shared(125797)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(125799)
    UserMissions = DynAccessor(125800)
    VehiclesInventory = DynAccessor(125801)
    VehiclesFilter = DynAccessor(125802)
    AlertMessage = DynAccessor(125803)
    Header = DynAccessor(125804)
    LoadoutPanelContainer = DynAccessor(125805)
    Events = DynAccessor(125806)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(125807)
        EventShop = DynAccessor(125808)

    hangarWidget = _hangarWidget(125809)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(125810)
        Commander = DynAccessor(125811)

    loadoutPanelContainer = _loadoutPanelContainer(125812)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(125814)
        Schedule = DynAccessor(125815)
        SeasonModifier = DynAccessor(125816)
        RoleSkillSlot = DynAccessor(125817)
        UserMissions = DynAccessor(125818)
        EntryPoint = DynAccessor(125819)
        WeeklyQuestsWidget = DynAccessor(125820)

    shared = _shared(125821)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(125823)
        SeasonModifier = DynAccessor(125824)
        RoleSkillSlot = DynAccessor(125825)
        UserMissions = DynAccessor(125826)
        EntryPoint = DynAccessor(125827)
        Quests = DynAccessor(125828)

    shared = _shared(125829)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(125831)

    loadout = _loadout(125832)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(125833)
        AlertMessage = DynAccessor(125834)

    shared = _shared(125835)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(125837)
        ProgressionEntryPoint = DynAccessor(125838)

    shared = _shared(125839)


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