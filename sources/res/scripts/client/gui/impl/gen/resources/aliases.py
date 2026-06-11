from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(129707)

    shared = _shared(129708)


class battle_pass(DynAccessor):
    __slots__ = ()
    ChapterChoice = DynAccessor(129710)
    Progression = DynAccessor(129711)
    PostProgression = DynAccessor(129712)
    BuyPass = DynAccessor(129713)
    BuyPassRewards = DynAccessor(129714)
    BuyLevels = DynAccessor(129715)
    BuyLevelsRewards = DynAccessor(129716)
    HolidayFinal = DynAccessor(129717)
    FinalRewardPreview = DynAccessor(129718)
    TankmenScreen = DynAccessor(129719)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129721)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(129722)
        Vehicle = DynAccessor(129723)

    contextMenu = _contextMenu(129724)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(129726)
        WeeklyMissions = DynAccessor(129727)
        PersonalMissions = DynAccessor(129728)
        BattlePass = DynAccessor(129729)
        Prestige = DynAccessor(129730)
        BattleMatters = DynAccessor(129731)
        ModuleVehicleUnlocks = DynAccessor(129732)
        CommonQuests = DynAccessor(129733)

    progression = _progression(129734)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129736)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129737)

    contextMenu = _contextMenu(129738)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129739)
        Wulf = DynAccessor(129740)
        Param = DynAccessor(129741)

    tooltip = _tooltip(129742)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129743)

    popOver = _popOver(129744)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(129745)

    shared = _shared(129746)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129748)
        VehiclesStatistics = DynAccessor(129749)
        Consumables = DynAccessor(129750)
        Equipments = DynAccessor(129751)
        Instructions = DynAccessor(129752)
        Shells = DynAccessor(129753)
        Loadout = DynAccessor(129754)
        Crew = DynAccessor(129755)
        VehicleParams = DynAccessor(129756)
        ETEVehicleParams = DynAccessor(129757)
        CurrentVehicle = DynAccessor(129758)
        VehiclesInventory = DynAccessor(129759)
        MainMenu = DynAccessor(129760)
        VehicleMenu = DynAccessor(129761)
        LootboxEntryPoint = DynAccessor(129762)
        VehicleFilters = DynAccessor(129763)
        VehiclePlaylists = DynAccessor(129764)
        Teaser = DynAccessor(129765)
        OptionalDevicesAssistant = DynAccessor(129766)
        SpaceInteraction = DynAccessor(129767)
        HeroTank = DynAccessor(129768)
        UserMissions = DynAccessor(129769)
        ModeState = DynAccessor(129770)
        EasyTankEquip = DynAccessor(129771)
        PetEvent = DynAccessor(129772)
        PetObjectTooltip = DynAccessor(129773)
        Settings = DynAccessor(129774)
        KeyBindings = DynAccessor(129775)
        ManageableVehiclePlaylists = DynAccessor(129776)

    shared = _shared(129777)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(129779)
        ContactsList = DynAccessor(129780)
        SessionStats = DynAccessor(129781)
        VehicleCompare = DynAccessor(129782)
        NotificationsCenter = DynAccessor(129783)
        Chats = DynAccessor(129784)
        ReferralProgram = DynAccessor(129785)
        ServerInfo = DynAccessor(129786)

    default = _default(129787)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(129789)
        NavigationBar = DynAccessor(129790)
        Prebattle = DynAccessor(129791)
        Wallet = DynAccessor(129792)
        AccountDashboard = DynAccessor(129793)
        HeaderState = DynAccessor(129794)
        UserAccount = DynAccessor(129795)
        ReservesEntryPoint = DynAccessor(129796)
        PremShop = DynAccessor(129797)
        CurrentVehicle = DynAccessor(129798)

    default = _default(129799)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129801)
        VehiclesInventory = DynAccessor(129802)
        VehiclesStatistics = DynAccessor(129803)
        VehicleFilters = DynAccessor(129804)
        VehiclePlaylists = DynAccessor(129805)

    select_vehicle = _select_vehicle(129806)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(129808)
            Instructions = DynAccessor(129809)
            Shells = DynAccessor(129810)
            Consumables = DynAccessor(129811)

        Loadout = _Loadout(129812)
        Vehicles = DynAccessor(129813)

    Hangar = _Hangar(129814)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(129816)
        Events = DynAccessor(129817)
        Quests = DynAccessor(129818)
        EventMainInfoTip = DynAccessor(129819)

    hangarWidget = _hangarWidget(129820)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(129821)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(129822)
                DailyBlock = DynAccessor(129823)
                PremiumBlock = DynAccessor(129824)
                RewardProgressBlock = DynAccessor(129825)

            DailyMissionsSection = _DailyMissionsSection(129826)
            WeeklyMissions = DynAccessor(129827)
            PersonalMissions = DynAccessor(129828)

        basicMissions = _basicMissions(129829)

    hub = _hub(129830)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(129832)
        Wallet = DynAccessor(129833)
        VehicleInfo = DynAccessor(129834)
        ManageableVehiclePlaylists = DynAccessor(129835)
        VehiclesInfo = DynAccessor(129836)
        VehiclesStatistics = DynAccessor(129837)
        VehicleFilters = DynAccessor(129838)
        VehiclePlaylists = DynAccessor(129839)
        VehiclesInventory = DynAccessor(129840)

    default = _default(129841)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(129843)
        CrewAutoReturn = DynAccessor(129844)
        CrewRetrain = DynAccessor(129845)
        QuickTraining = DynAccessor(129846)
        CrewOut = DynAccessor(129847)
        CrewBack = DynAccessor(129848)
        EasyEquip = DynAccessor(129849)
        ArmorInspector = DynAccessor(129850)
        FieldModification = DynAccessor(129851)
        NationChange = DynAccessor(129852)
        Research = DynAccessor(129853)
        AboutVehicle = DynAccessor(129854)
        Compare = DynAccessor(129855)
        Repairs = DynAccessor(129856)
        VehSkillTree = DynAccessor(129857)
        ProBoost = DynAccessor(129858)

    default = _default(129859)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129861)
        ConsumablesPanel = DynAccessor(129862)
        Progression = DynAccessor(129863)
        Crewman = DynAccessor(129864)
        VehicleStats = DynAccessor(129865)
        ProgressionContent = DynAccessor(129866)
        ProgressionQuests = DynAccessor(129867)
        LootboxEntryPoint = DynAccessor(129868)

    shared = _shared(129869)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(129871)
    UserMissions = DynAccessor(129872)
    VehiclesInventory = DynAccessor(129873)
    VehiclesFilter = DynAccessor(129874)
    AlertMessage = DynAccessor(129875)
    Header = DynAccessor(129876)
    LoadoutPanelContainer = DynAccessor(129877)
    Events = DynAccessor(129878)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(129879)
        EventShop = DynAccessor(129880)

    hangarWidget = _hangarWidget(129881)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(129882)
        Commander = DynAccessor(129883)

    loadoutPanelContainer = _loadoutPanelContainer(129884)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129886)
        Schedule = DynAccessor(129887)
        SeasonModifier = DynAccessor(129888)
        RoleSkillSlot = DynAccessor(129889)
        UserMissions = DynAccessor(129890)
        EntryPoint = DynAccessor(129891)
        WeeklyQuestsWidget = DynAccessor(129892)
        BattleResultsWeeklyQuests = DynAccessor(129893)
        BattleResultsCustomizationQuests = DynAccessor(129894)

    shared = _shared(129895)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129897)
        SeasonModifier = DynAccessor(129898)
        RoleSkillSlot = DynAccessor(129899)
        UserMissions = DynAccessor(129900)
        EntryPoint = DynAccessor(129901)
        Quests = DynAccessor(129902)

    shared = _shared(129903)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(129905)

    loadout = _loadout(129906)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129907)
        AlertMessage = DynAccessor(129908)

    shared = _shared(129909)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129911)
        ProgressionEntryPoint = DynAccessor(129912)
        ProgressionQuests = DynAccessor(129913)

    shared = _shared(129914)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129916)
        Difficulty = DynAccessor(129917)
        MoneyBalance = DynAccessor(129918)
        TeamStats = DynAccessor(129919)
        Meta = DynAccessor(129920)
        Keys = DynAccessor(129921)
        Quests = DynAccessor(129922)
        RewardPath = DynAccessor(129923)
        Shop = DynAccessor(129924)
        Gsw = DynAccessor(129925)
        Switcher = DynAccessor(129926)
        PresetsSwitcher = DynAccessor(129927)
        VehiclesDaily = DynAccessor(129928)
        BundleCard = DynAccessor(129929)
        DailyCard = DynAccessor(129930)
        Parallax = DynAccessor(129931)

    shared = _shared(129932)


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