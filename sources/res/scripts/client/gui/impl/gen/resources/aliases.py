from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(124637)

    shared = _shared(124638)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(124640)
    ExtraVideo = DynAccessor(124641)
    Intro = DynAccessor(124642)
    ChapterChoice = DynAccessor(124643)
    Progression = DynAccessor(124644)
    PostProgression = DynAccessor(124645)
    BuyPass = DynAccessor(124646)
    BuyPassConfirm = DynAccessor(124647)
    BuyPassRewards = DynAccessor(124648)
    BuyLevels = DynAccessor(124649)
    BuyLevelsRewards = DynAccessor(124650)
    HolidayFinal = DynAccessor(124651)
    FinalRewardPreview = DynAccessor(124652)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(124654)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(124655)
        Vehicle = DynAccessor(124656)

    contextMenu = _contextMenu(124657)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(124659)
    UserMissions = DynAccessor(124660)
    VehiclesInventory = DynAccessor(124661)
    VehiclesFilter = DynAccessor(124662)
    AlertMessage = DynAccessor(124663)
    Header = DynAccessor(124664)
    LoadoutPanelContainer = DynAccessor(124665)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(124666)
        EventShop = DynAccessor(124667)

    hangarWidget = _hangarWidget(124668)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(124669)
        Commander = DynAccessor(124670)

    loadoutPanelContainer = _loadoutPanelContainer(124671)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(124673)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(124674)

    contextMenu = _contextMenu(124675)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(124676)
        Wulf = DynAccessor(124677)
        Param = DynAccessor(124678)

    tooltip = _tooltip(124679)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(124680)

    popOver = _popOver(124681)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(124682)

    shared = _shared(124683)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(124685)
        Schedule = DynAccessor(124686)
        SeasonModifier = DynAccessor(124687)
        RoleSkillSlot = DynAccessor(124688)
        UserMissions = DynAccessor(124689)
        EntryPoint = DynAccessor(124690)
        WeeklyQuestsWidget = DynAccessor(124691)

    shared = _shared(124692)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(124694)
        SeasonModifier = DynAccessor(124695)
        RoleSkillSlot = DynAccessor(124696)
        UserMissions = DynAccessor(124697)
        EntryPoint = DynAccessor(124698)
        Quests = DynAccessor(124699)

    shared = _shared(124700)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(124702)

    loadout = _loadout(124703)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(124704)
        AlertMessage = DynAccessor(124705)

    shared = _shared(124706)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(124708)
        ProgressionEntryPoint = DynAccessor(124709)

    shared = _shared(124710)


class halloween(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(124712)
        AmmunitionPanel = DynAccessor(124713)
        Difficulty = DynAccessor(124714)
        MoneyBalance = DynAccessor(124715)
        TeamStats = DynAccessor(124716)
        Meta = DynAccessor(124717)
        Keys = DynAccessor(124718)
        Quests = DynAccessor(124719)
        RewardPath = DynAccessor(124720)
        Shop = DynAccessor(124721)
        Gsw = DynAccessor(124722)
        Switcher = DynAccessor(124723)
        CrewMembers = DynAccessor(124724)

    shared = _shared(124725)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(124727)
        VehiclesStatistics = DynAccessor(124728)
        Consumables = DynAccessor(124729)
        Equipments = DynAccessor(124730)
        Instructions = DynAccessor(124731)
        Shells = DynAccessor(124732)
        Loadout = DynAccessor(124733)
        Crew = DynAccessor(124734)
        VehicleParams = DynAccessor(124735)
        CurrentVehicle = DynAccessor(124736)
        VehiclesInventory = DynAccessor(124737)
        MainMenu = DynAccessor(124738)
        VehicleMenu = DynAccessor(124739)
        LootboxEntryPoint = DynAccessor(124740)
        VehicleFilters = DynAccessor(124741)
        VehiclePlaylists = DynAccessor(124742)
        Teaser = DynAccessor(124743)
        OptionalDevicesAssistant = DynAccessor(124744)
        SpaceInteraction = DynAccessor(124745)
        HeroTank = DynAccessor(124746)
        UserMissions = DynAccessor(124747)
        ModeState = DynAccessor(124748)
        PetEvent = DynAccessor(124749)
        PetObjectTooltip = DynAccessor(124750)
        Settings = DynAccessor(124751)
        KeyBindings = DynAccessor(124752)
        HolidayOpsWidget = DynAccessor(124753)
        Vignette = DynAccessor(124754)

    shared = _shared(124755)


class holiday_ops(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        MainMenu = DynAccessor(124757)
        Sidebar = DynAccessor(124758)
        BalancePanel = DynAccessor(124759)
        EconomicBonusPanel = DynAccessor(124760)

    default = _default(124761)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(124763)
        AmmunitionPanel = DynAccessor(124764)
        Difficulty = DynAccessor(124765)
        MoneyBalance = DynAccessor(124766)
        TeamStats = DynAccessor(124767)
        Meta = DynAccessor(124768)
        Keys = DynAccessor(124769)
        Quests = DynAccessor(124770)
        RewardPath = DynAccessor(124771)
        Shop = DynAccessor(124772)
        Gsw = DynAccessor(124773)
        Switcher = DynAccessor(124774)

    shared = _shared(124775)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(124777)
        ContactsList = DynAccessor(124778)
        SessionStats = DynAccessor(124779)
        VehicleCompare = DynAccessor(124780)
        NotificationsCenter = DynAccessor(124781)
        Chats = DynAccessor(124782)
        ReferralProgram = DynAccessor(124783)
        ServerInfo = DynAccessor(124784)

    default = _default(124785)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(124787)
        NavigationBar = DynAccessor(124788)
        Prebattle = DynAccessor(124789)
        Wallet = DynAccessor(124790)
        AccountDashboard = DynAccessor(124791)
        HeaderState = DynAccessor(124792)
        UserAccount = DynAccessor(124793)
        ReservesEntryPoint = DynAccessor(124794)
        PremShop = DynAccessor(124795)
        CurrentVehicle = DynAccessor(124796)

    default = _default(124797)


class one_time_gift(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        NavigationBar = DynAccessor(124799)
        EquipmentSetTooltip = DynAccessor(124800)

    default = _default(124801)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(124803)
            Instructions = DynAccessor(124804)
            Shells = DynAccessor(124805)
            Consumables = DynAccessor(124806)

        Loadout = _Loadout(124807)
        Vehicles = DynAccessor(124808)

    Hangar = _Hangar(124809)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(124811)
        Events = DynAccessor(124812)
        Quests = DynAccessor(124813)
        EventMainInfoTip = DynAccessor(124814)

    hangarWidget = _hangarWidget(124815)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(124816)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(124817)
                DailyBlock = DynAccessor(124818)
                PremiumBlock = DynAccessor(124819)
                RewardProgressBlock = DynAccessor(124820)

            DailyMissionsSection = _DailyMissionsSection(124821)
            WeeklyMissions = DynAccessor(124822)
            PersonalMissions = DynAccessor(124823)

        basicMissions = _basicMissions(124824)

    hub = _hub(124825)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(124827)
        Wallet = DynAccessor(124828)

    default = _default(124829)


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
    holiday_ops = holiday_ops()
    last_stand = last_stand()
    lobby_footer = lobby_footer()
    lobby_header = lobby_header()
    one_time_gift = one_time_gift()
    states = states()
    user_missions = user_missions()
    vehicle_hub = vehicle_hub()