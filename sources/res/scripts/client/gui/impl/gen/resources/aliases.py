from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(119755)

    shared = _shared(119756)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(119758)
    ExtraVideo = DynAccessor(119759)
    Intro = DynAccessor(119760)
    ChapterChoice = DynAccessor(119761)
    Progression = DynAccessor(119762)
    PostProgression = DynAccessor(119763)
    BuyPass = DynAccessor(119764)
    BuyPassConfirm = DynAccessor(119765)
    BuyPassRewards = DynAccessor(119766)
    BuyLevels = DynAccessor(119767)
    BuyLevelsRewards = DynAccessor(119768)
    HolidayFinal = DynAccessor(119769)
    FinalRewardPreview = DynAccessor(119770)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(119772)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(119773)
        Vehicle = DynAccessor(119774)

    contextMenu = _contextMenu(119775)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(119777)
    UserMissions = DynAccessor(119778)
    VehiclesInventory = DynAccessor(119779)
    VehiclesFilter = DynAccessor(119780)
    AlertMessage = DynAccessor(119781)
    Header = DynAccessor(119782)
    LoadoutPanelContainer = DynAccessor(119783)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(119784)
        EventShop = DynAccessor(119785)

    hangarWidget = _hangarWidget(119786)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(119787)
        Commander = DynAccessor(119788)

    loadoutPanelContainer = _loadoutPanelContainer(119789)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(119791)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(119792)

    contextMenu = _contextMenu(119793)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(119794)
        Wulf = DynAccessor(119795)
        Param = DynAccessor(119796)

    tooltip = _tooltip(119797)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(119798)

    popOver = _popOver(119799)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(119800)

    shared = _shared(119801)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(119803)
        Schedule = DynAccessor(119804)
        SeasonModifier = DynAccessor(119805)
        RoleSkillSlot = DynAccessor(119806)
        UserMissions = DynAccessor(119807)
        EntryPoint = DynAccessor(119808)
        WeeklyQuestsWidget = DynAccessor(119809)

    shared = _shared(119810)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(119812)
        SeasonModifier = DynAccessor(119813)
        RoleSkillSlot = DynAccessor(119814)
        UserMissions = DynAccessor(119815)
        EntryPoint = DynAccessor(119816)
        Quests = DynAccessor(119817)

    shared = _shared(119818)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(119820)

    loadout = _loadout(119821)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(119822)
        AlertMessage = DynAccessor(119823)

    shared = _shared(119824)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(119826)
        ProgressionEntryPoint = DynAccessor(119827)

    shared = _shared(119828)


class halloween(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(119830)
        AmmunitionPanel = DynAccessor(119831)
        Difficulty = DynAccessor(119832)
        MoneyBalance = DynAccessor(119833)
        TeamStats = DynAccessor(119834)
        Meta = DynAccessor(119835)
        Keys = DynAccessor(119836)
        Quests = DynAccessor(119837)
        RewardPath = DynAccessor(119838)
        Shop = DynAccessor(119839)
        Gsw = DynAccessor(119840)
        Switcher = DynAccessor(119841)
        CrewMembers = DynAccessor(119842)

    shared = _shared(119843)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(119845)
        VehiclesStatistics = DynAccessor(119846)
        Consumables = DynAccessor(119847)
        Equipments = DynAccessor(119848)
        Instructions = DynAccessor(119849)
        Shells = DynAccessor(119850)
        Loadout = DynAccessor(119851)
        Crew = DynAccessor(119852)
        VehicleParams = DynAccessor(119853)
        CurrentVehicle = DynAccessor(119854)
        VehiclesInventory = DynAccessor(119855)
        MainMenu = DynAccessor(119856)
        VehicleMenu = DynAccessor(119857)
        LootboxEntryPoint = DynAccessor(119858)
        VehicleFilters = DynAccessor(119859)
        VehiclePlaylists = DynAccessor(119860)
        Teaser = DynAccessor(119861)
        OptionalDevicesAssistant = DynAccessor(119862)
        SpaceInteraction = DynAccessor(119863)
        HeroTank = DynAccessor(119864)
        UserMissions = DynAccessor(119865)
        ModeState = DynAccessor(119866)

    shared = _shared(119867)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(119869)
        AmmunitionPanel = DynAccessor(119870)
        Difficulty = DynAccessor(119871)
        MoneyBalance = DynAccessor(119872)
        TeamStats = DynAccessor(119873)
        Meta = DynAccessor(119874)
        Keys = DynAccessor(119875)
        Quests = DynAccessor(119876)
        RewardPath = DynAccessor(119877)
        Shop = DynAccessor(119878)
        Gsw = DynAccessor(119879)
        Switcher = DynAccessor(119880)

    shared = _shared(119881)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(119883)
        ContactsList = DynAccessor(119884)
        SessionStats = DynAccessor(119885)
        VehicleCompare = DynAccessor(119886)
        NotificationsCenter = DynAccessor(119887)
        Chats = DynAccessor(119888)
        ReferralProgram = DynAccessor(119889)
        ServerInfo = DynAccessor(119890)

    default = _default(119891)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(119893)
        NavigationBar = DynAccessor(119894)
        Prebattle = DynAccessor(119895)
        Wallet = DynAccessor(119896)
        AccountDashboard = DynAccessor(119897)
        HeaderState = DynAccessor(119898)
        UserAccount = DynAccessor(119899)
        ReservesEntryPoint = DynAccessor(119900)
        PremShop = DynAccessor(119901)

    default = _default(119902)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(119904)
            Instructions = DynAccessor(119905)
            Shells = DynAccessor(119906)
            Consumables = DynAccessor(119907)

        Loadout = _Loadout(119908)
        Vehicles = DynAccessor(119909)

    Hangar = _Hangar(119910)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(119912)
        Events = DynAccessor(119913)
        Quests = DynAccessor(119914)
        EventMainInfoTip = DynAccessor(119915)

    hangarWidget = _hangarWidget(119916)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(119917)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(119918)
                DailyBlock = DynAccessor(119919)
                PremiumBlock = DynAccessor(119920)
                RewardProgressBlock = DynAccessor(119921)

            DailyMissionsSection = _DailyMissionsSection(119922)
            WeeklyMissions = DynAccessor(119923)
            PersonalMissions = DynAccessor(119924)

        basicMissions = _basicMissions(119925)

    hub = _hub(119926)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(119928)
        Wallet = DynAccessor(119929)

    default = _default(119930)


class Aliases(DynAccessor):
    __slots__ = ()
    battle_modifiers = battle_modifiers()
    battle_pass = battle_pass()
    battle_result = battle_result()
    battle_royale = battle_royale()
    common = common()
    comp7 = comp7()
    comp7_light = comp7_light()
    frontline = frontline()
    fun_random = fun_random()
    halloween = halloween()
    hangar = hangar()
    last_stand = last_stand()
    lobby_footer = lobby_footer()
    lobby_header = lobby_header()
    states = states()
    user_missions = user_missions()
    vehicle_hub = vehicle_hub()