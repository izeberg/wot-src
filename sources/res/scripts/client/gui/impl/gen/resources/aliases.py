from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(129717)

    shared = _shared(129718)


class battle_pass(DynAccessor):
    __slots__ = ()
    ChapterChoice = DynAccessor(129720)
    Progression = DynAccessor(129721)
    PostProgression = DynAccessor(129722)
    BuyPass = DynAccessor(129723)
    BuyPassRewards = DynAccessor(129724)
    BuyLevels = DynAccessor(129725)
    BuyLevelsRewards = DynAccessor(129726)
    HolidayFinal = DynAccessor(129727)
    FinalRewardPreview = DynAccessor(129728)
    TankmenScreen = DynAccessor(129729)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129731)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(129732)
        Vehicle = DynAccessor(129733)

    contextMenu = _contextMenu(129734)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(129736)
        WeeklyMissions = DynAccessor(129737)
        PersonalMissions = DynAccessor(129738)
        BattlePass = DynAccessor(129739)
        Prestige = DynAccessor(129740)
        BattleMatters = DynAccessor(129741)
        ModuleVehicleUnlocks = DynAccessor(129742)
        CommonQuests = DynAccessor(129743)

    progression = _progression(129744)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(129746)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129747)

    contextMenu = _contextMenu(129748)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129749)
        Wulf = DynAccessor(129750)
        Param = DynAccessor(129751)

    tooltip = _tooltip(129752)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(129753)

    popOver = _popOver(129754)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(129755)

    shared = _shared(129756)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129758)
        VehiclesStatistics = DynAccessor(129759)
        Consumables = DynAccessor(129760)
        Equipments = DynAccessor(129761)
        Instructions = DynAccessor(129762)
        Shells = DynAccessor(129763)
        Loadout = DynAccessor(129764)
        Crew = DynAccessor(129765)
        VehicleParams = DynAccessor(129766)
        ETEVehicleParams = DynAccessor(129767)
        CurrentVehicle = DynAccessor(129768)
        VehiclesInventory = DynAccessor(129769)
        MainMenu = DynAccessor(129770)
        VehicleMenu = DynAccessor(129771)
        LootboxEntryPoint = DynAccessor(129772)
        VehicleFilters = DynAccessor(129773)
        VehiclePlaylists = DynAccessor(129774)
        Teaser = DynAccessor(129775)
        OptionalDevicesAssistant = DynAccessor(129776)
        SpaceInteraction = DynAccessor(129777)
        HeroTank = DynAccessor(129778)
        UserMissions = DynAccessor(129779)
        ModeState = DynAccessor(129780)
        EasyTankEquip = DynAccessor(129781)
        PetEvent = DynAccessor(129782)
        PetObjectTooltip = DynAccessor(129783)
        Settings = DynAccessor(129784)
        KeyBindings = DynAccessor(129785)
        ManageableVehiclePlaylists = DynAccessor(129786)

    shared = _shared(129787)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(129789)
        ContactsList = DynAccessor(129790)
        SessionStats = DynAccessor(129791)
        VehicleCompare = DynAccessor(129792)
        NotificationsCenter = DynAccessor(129793)
        Chats = DynAccessor(129794)
        ReferralProgram = DynAccessor(129795)
        ServerInfo = DynAccessor(129796)

    default = _default(129797)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(129799)
        NavigationBar = DynAccessor(129800)
        Prebattle = DynAccessor(129801)
        Wallet = DynAccessor(129802)
        AccountDashboard = DynAccessor(129803)
        HeaderState = DynAccessor(129804)
        UserAccount = DynAccessor(129805)
        ReservesEntryPoint = DynAccessor(129806)
        PremShop = DynAccessor(129807)
        CurrentVehicle = DynAccessor(129808)

    default = _default(129809)


class select_vehicle(DynAccessor):
    __slots__ = ()

    class _select_vehicle(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(129811)
        VehiclesInventory = DynAccessor(129812)
        VehiclesStatistics = DynAccessor(129813)
        VehicleFilters = DynAccessor(129814)
        VehiclePlaylists = DynAccessor(129815)

    select_vehicle = _select_vehicle(129816)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(129818)
            Instructions = DynAccessor(129819)
            Shells = DynAccessor(129820)
            Consumables = DynAccessor(129821)

        Loadout = _Loadout(129822)
        Vehicles = DynAccessor(129823)

    Hangar = _Hangar(129824)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(129826)
        Events = DynAccessor(129827)
        Quests = DynAccessor(129828)
        EventMainInfoTip = DynAccessor(129829)

    hangarWidget = _hangarWidget(129830)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(129831)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(129832)
                DailyBlock = DynAccessor(129833)
                PremiumBlock = DynAccessor(129834)
                RewardProgressBlock = DynAccessor(129835)

            DailyMissionsSection = _DailyMissionsSection(129836)
            WeeklyMissions = DynAccessor(129837)
            PersonalMissions = DynAccessor(129838)

        basicMissions = _basicMissions(129839)

    hub = _hub(129840)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(129842)
        Wallet = DynAccessor(129843)
        VehicleInfo = DynAccessor(129844)
        ManageableVehiclePlaylists = DynAccessor(129845)
        VehiclesInfo = DynAccessor(129846)
        VehiclesStatistics = DynAccessor(129847)
        VehicleFilters = DynAccessor(129848)
        VehiclePlaylists = DynAccessor(129849)
        VehiclesInventory = DynAccessor(129850)

    default = _default(129851)


class vehicle_menu(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Customization = DynAccessor(129853)
        CrewAutoReturn = DynAccessor(129854)
        CrewRetrain = DynAccessor(129855)
        QuickTraining = DynAccessor(129856)
        CrewOut = DynAccessor(129857)
        CrewBack = DynAccessor(129858)
        EasyEquip = DynAccessor(129859)
        ArmorInspector = DynAccessor(129860)
        FieldModification = DynAccessor(129861)
        NationChange = DynAccessor(129862)
        Research = DynAccessor(129863)
        AboutVehicle = DynAccessor(129864)
        Compare = DynAccessor(129865)
        Repairs = DynAccessor(129866)
        VehSkillTree = DynAccessor(129867)
        ProBoost = DynAccessor(129868)

    default = _default(129869)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129871)
        ConsumablesPanel = DynAccessor(129872)
        Progression = DynAccessor(129873)
        Crewman = DynAccessor(129874)
        VehicleStats = DynAccessor(129875)
        ProgressionContent = DynAccessor(129876)
        ProgressionQuests = DynAccessor(129877)
        LootboxEntryPoint = DynAccessor(129878)

    shared = _shared(129879)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(129881)
    UserMissions = DynAccessor(129882)
    VehiclesInventory = DynAccessor(129883)
    VehiclesFilter = DynAccessor(129884)
    AlertMessage = DynAccessor(129885)
    Header = DynAccessor(129886)
    LoadoutPanelContainer = DynAccessor(129887)
    Events = DynAccessor(129888)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(129889)
        EventShop = DynAccessor(129890)

    hangarWidget = _hangarWidget(129891)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(129892)
        Commander = DynAccessor(129893)

    loadoutPanelContainer = _loadoutPanelContainer(129894)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129896)
        Schedule = DynAccessor(129897)
        SeasonModifier = DynAccessor(129898)
        RoleSkillSlot = DynAccessor(129899)
        UserMissions = DynAccessor(129900)
        EntryPoint = DynAccessor(129901)
        WeeklyQuestsWidget = DynAccessor(129902)
        BattleResultsWeeklyQuests = DynAccessor(129903)
        BattleResultsCustomizationQuests = DynAccessor(129904)

    shared = _shared(129905)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(129907)
        SeasonModifier = DynAccessor(129908)
        RoleSkillSlot = DynAccessor(129909)
        UserMissions = DynAccessor(129910)
        EntryPoint = DynAccessor(129911)
        Quests = DynAccessor(129912)

    shared = _shared(129913)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(129915)

    loadout = _loadout(129916)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129917)
        AlertMessage = DynAccessor(129918)

    shared = _shared(129919)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(129921)
        ProgressionEntryPoint = DynAccessor(129922)
        ProgressionQuests = DynAccessor(129923)

    shared = _shared(129924)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(129926)
        Difficulty = DynAccessor(129927)
        MoneyBalance = DynAccessor(129928)
        TeamStats = DynAccessor(129929)
        Meta = DynAccessor(129930)
        Keys = DynAccessor(129931)
        Quests = DynAccessor(129932)
        RewardPath = DynAccessor(129933)
        Shop = DynAccessor(129934)
        Gsw = DynAccessor(129935)
        Switcher = DynAccessor(129936)
        PresetsSwitcher = DynAccessor(129937)
        VehiclesDaily = DynAccessor(129938)
        BundleCard = DynAccessor(129939)
        DailyCard = DynAccessor(129940)
        Parallax = DynAccessor(129941)

    shared = _shared(129942)


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