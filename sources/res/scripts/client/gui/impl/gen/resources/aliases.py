from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(125719)

    shared = _shared(125720)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(125722)
    ExtraVideo = DynAccessor(125723)
    Intro = DynAccessor(125724)
    ChapterChoice = DynAccessor(125725)
    Progression = DynAccessor(125726)
    PostProgression = DynAccessor(125727)
    BuyPass = DynAccessor(125728)
    BuyPassRewards = DynAccessor(125729)
    BuyLevels = DynAccessor(125730)
    BuyLevelsRewards = DynAccessor(125731)
    HolidayFinal = DynAccessor(125732)
    FinalRewardPreview = DynAccessor(125733)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(125735)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(125736)
        Vehicle = DynAccessor(125737)

    contextMenu = _contextMenu(125738)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(125740)
        WeeklyMissions = DynAccessor(125741)
        PersonalMissions = DynAccessor(125742)
        BattlePass = DynAccessor(125743)
        Prestige = DynAccessor(125744)
        BattleMatters = DynAccessor(125745)
        ModuleVehicleUnlocks = DynAccessor(125746)
        CommonQuests = DynAccessor(125747)

    progression = _progression(125748)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(125750)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125751)

    contextMenu = _contextMenu(125752)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125753)
        Wulf = DynAccessor(125754)
        Param = DynAccessor(125755)

    tooltip = _tooltip(125756)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(125757)

    popOver = _popOver(125758)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(125759)

    shared = _shared(125760)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(125762)
        VehiclesStatistics = DynAccessor(125763)
        Consumables = DynAccessor(125764)
        Equipments = DynAccessor(125765)
        Instructions = DynAccessor(125766)
        Shells = DynAccessor(125767)
        Loadout = DynAccessor(125768)
        Crew = DynAccessor(125769)
        VehicleParams = DynAccessor(125770)
        ETEVehicleParams = DynAccessor(125771)
        CurrentVehicle = DynAccessor(125772)
        VehiclesInventory = DynAccessor(125773)
        MainMenu = DynAccessor(125774)
        VehicleMenu = DynAccessor(125775)
        LootboxEntryPoint = DynAccessor(125776)
        VehicleFilters = DynAccessor(125777)
        VehiclePlaylists = DynAccessor(125778)
        Teaser = DynAccessor(125779)
        OptionalDevicesAssistant = DynAccessor(125780)
        SpaceInteraction = DynAccessor(125781)
        HeroTank = DynAccessor(125782)
        UserMissions = DynAccessor(125783)
        ModeState = DynAccessor(125784)
        EasyTankEquip = DynAccessor(125785)
        PetEvent = DynAccessor(125786)
        PetObjectTooltip = DynAccessor(125787)
        Settings = DynAccessor(125788)
        KeyBindings = DynAccessor(125789)
        ManageableVehiclePlaylists = DynAccessor(125790)

    shared = _shared(125791)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(125793)
        ContactsList = DynAccessor(125794)
        SessionStats = DynAccessor(125795)
        VehicleCompare = DynAccessor(125796)
        NotificationsCenter = DynAccessor(125797)
        Chats = DynAccessor(125798)
        ReferralProgram = DynAccessor(125799)
        ServerInfo = DynAccessor(125800)

    default = _default(125801)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(125803)
        NavigationBar = DynAccessor(125804)
        Prebattle = DynAccessor(125805)
        Wallet = DynAccessor(125806)
        AccountDashboard = DynAccessor(125807)
        HeaderState = DynAccessor(125808)
        UserAccount = DynAccessor(125809)
        ReservesEntryPoint = DynAccessor(125810)
        PremShop = DynAccessor(125811)
        CurrentVehicle = DynAccessor(125812)

    default = _default(125813)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(125815)
        VehiclesInventory = DynAccessor(125816)
        VehiclesStatistics = DynAccessor(125817)
        VehicleFilters = DynAccessor(125818)
        VehiclePlaylists = DynAccessor(125819)

    select_vehicle = _select_vehicle(125820)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(125822)
            Instructions = DynAccessor(125823)
            Shells = DynAccessor(125824)
            Consumables = DynAccessor(125825)

        Loadout = _Loadout(125826)
        Vehicles = DynAccessor(125827)

    Hangar = _Hangar(125828)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(125830)
        Events = DynAccessor(125831)
        Quests = DynAccessor(125832)
        EventMainInfoTip = DynAccessor(125833)

    hangarWidget = _hangarWidget(125834)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(125835)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(125836)
                DailyBlock = DynAccessor(125837)
                PremiumBlock = DynAccessor(125838)
                RewardProgressBlock = DynAccessor(125839)

            DailyMissionsSection = _DailyMissionsSection(125840)
            WeeklyMissions = DynAccessor(125841)
            PersonalMissions = DynAccessor(125842)

        basicMissions = _basicMissions(125843)

    hub = _hub(125844)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(125846)
        Wallet = DynAccessor(125847)
        VehicleInfo = DynAccessor(125848)
        ManageableVehiclePlaylists = DynAccessor(125849)
        VehiclesInfo = DynAccessor(125850)
        VehiclesStatistics = DynAccessor(125851)
        VehicleFilters = DynAccessor(125852)
        VehiclePlaylists = DynAccessor(125853)
        VehiclesInventory = DynAccessor(125854)

    default = _default(125855)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(125857)
        CrewAutoReturn = DynAccessor(125858)
        CrewRetrain = DynAccessor(125859)
        QuickTraining = DynAccessor(125860)
        CrewOut = DynAccessor(125861)
        CrewBack = DynAccessor(125862)
        EasyEquip = DynAccessor(125863)
        ArmorInspector = DynAccessor(125864)
        FieldModification = DynAccessor(125865)
        NationChange = DynAccessor(125866)
        Research = DynAccessor(125867)
        AboutVehicle = DynAccessor(125868)
        Compare = DynAccessor(125869)
        Repairs = DynAccessor(125870)
        VehSkillTree = DynAccessor(125871)
        ProBoost = DynAccessor(125872)

    default = _default(125873)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(125875)
        ConsumablesPanel = DynAccessor(125876)
        Progression = DynAccessor(125877)
        Crewman = DynAccessor(125878)
        VehicleStats = DynAccessor(125879)
        ProgressionContent = DynAccessor(125880)
        ProgressionQuests = DynAccessor(125881)
        LootboxEntryPoint = DynAccessor(125882)

    shared = _shared(125883)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(125885)
    UserMissions = DynAccessor(125886)
    VehiclesInventory = DynAccessor(125887)
    VehiclesFilter = DynAccessor(125888)
    AlertMessage = DynAccessor(125889)
    Header = DynAccessor(125890)
    LoadoutPanelContainer = DynAccessor(125891)
    Events = DynAccessor(125892)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(125893)
        EventShop = DynAccessor(125894)

    hangarWidget = _hangarWidget(125895)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(125896)
        Commander = DynAccessor(125897)

    loadoutPanelContainer = _loadoutPanelContainer(125898)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(125900)
        Schedule = DynAccessor(125901)
        SeasonModifier = DynAccessor(125902)
        RoleSkillSlot = DynAccessor(125903)
        UserMissions = DynAccessor(125904)
        EntryPoint = DynAccessor(125905)
        WeeklyQuestsWidget = DynAccessor(125906)

    shared = _shared(125907)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(125909)
        SeasonModifier = DynAccessor(125910)
        RoleSkillSlot = DynAccessor(125911)
        UserMissions = DynAccessor(125912)
        EntryPoint = DynAccessor(125913)
        Quests = DynAccessor(125914)

    shared = _shared(125915)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(125917)

    loadout = _loadout(125918)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(125919)
        AlertMessage = DynAccessor(125920)

    shared = _shared(125921)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(125923)
        ProgressionEntryPoint = DynAccessor(125924)

    shared = _shared(125925)


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