from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(124601)

    shared = _shared(124602)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(124604)
    ExtraVideo = DynAccessor(124605)
    Intro = DynAccessor(124606)
    ChapterChoice = DynAccessor(124607)
    Progression = DynAccessor(124608)
    PostProgression = DynAccessor(124609)
    BuyPass = DynAccessor(124610)
    BuyPassConfirm = DynAccessor(124611)
    BuyPassRewards = DynAccessor(124612)
    BuyLevels = DynAccessor(124613)
    BuyLevelsRewards = DynAccessor(124614)
    HolidayFinal = DynAccessor(124615)
    FinalRewardPreview = DynAccessor(124616)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(124618)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(124619)
        Vehicle = DynAccessor(124620)

    contextMenu = _contextMenu(124621)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(124623)
    UserMissions = DynAccessor(124624)
    VehiclesInventory = DynAccessor(124625)
    VehiclesFilter = DynAccessor(124626)
    AlertMessage = DynAccessor(124627)
    Header = DynAccessor(124628)
    LoadoutPanelContainer = DynAccessor(124629)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(124630)
        EventShop = DynAccessor(124631)

    hangarWidget = _hangarWidget(124632)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(124633)
        Commander = DynAccessor(124634)

    loadoutPanelContainer = _loadoutPanelContainer(124635)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(124637)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(124638)

    contextMenu = _contextMenu(124639)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(124640)
        Wulf = DynAccessor(124641)
        Param = DynAccessor(124642)

    tooltip = _tooltip(124643)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(124644)

    popOver = _popOver(124645)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(124646)

    shared = _shared(124647)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(124649)
        Schedule = DynAccessor(124650)
        SeasonModifier = DynAccessor(124651)
        RoleSkillSlot = DynAccessor(124652)
        UserMissions = DynAccessor(124653)
        EntryPoint = DynAccessor(124654)
        WeeklyQuestsWidget = DynAccessor(124655)

    shared = _shared(124656)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(124658)
        SeasonModifier = DynAccessor(124659)
        RoleSkillSlot = DynAccessor(124660)
        UserMissions = DynAccessor(124661)
        EntryPoint = DynAccessor(124662)
        Quests = DynAccessor(124663)

    shared = _shared(124664)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(124666)

    loadout = _loadout(124667)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(124668)
        AlertMessage = DynAccessor(124669)

    shared = _shared(124670)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(124672)
        ProgressionEntryPoint = DynAccessor(124673)

    shared = _shared(124674)


class halloween(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(124676)
        AmmunitionPanel = DynAccessor(124677)
        Difficulty = DynAccessor(124678)
        MoneyBalance = DynAccessor(124679)
        TeamStats = DynAccessor(124680)
        Meta = DynAccessor(124681)
        Keys = DynAccessor(124682)
        Quests = DynAccessor(124683)
        RewardPath = DynAccessor(124684)
        Shop = DynAccessor(124685)
        Gsw = DynAccessor(124686)
        Switcher = DynAccessor(124687)
        CrewMembers = DynAccessor(124688)

    shared = _shared(124689)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(124691)
        VehiclesStatistics = DynAccessor(124692)
        Consumables = DynAccessor(124693)
        Equipments = DynAccessor(124694)
        Instructions = DynAccessor(124695)
        Shells = DynAccessor(124696)
        Loadout = DynAccessor(124697)
        Crew = DynAccessor(124698)
        VehicleParams = DynAccessor(124699)
        CurrentVehicle = DynAccessor(124700)
        VehiclesInventory = DynAccessor(124701)
        MainMenu = DynAccessor(124702)
        VehicleMenu = DynAccessor(124703)
        LootboxEntryPoint = DynAccessor(124704)
        VehicleFilters = DynAccessor(124705)
        VehiclePlaylists = DynAccessor(124706)
        Teaser = DynAccessor(124707)
        OptionalDevicesAssistant = DynAccessor(124708)
        SpaceInteraction = DynAccessor(124709)
        HeroTank = DynAccessor(124710)
        UserMissions = DynAccessor(124711)
        ModeState = DynAccessor(124712)
        PetEvent = DynAccessor(124713)
        PetObjectTooltip = DynAccessor(124714)
        Settings = DynAccessor(124715)
        KeyBindings = DynAccessor(124716)
        HolidayOpsWidget = DynAccessor(124717)
        Vignette = DynAccessor(124718)

    shared = _shared(124719)


class holiday_ops(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        MainMenu = DynAccessor(124721)
        Sidebar = DynAccessor(124722)
        BalancePanel = DynAccessor(124723)
        EconomicBonusPanel = DynAccessor(124724)

    default = _default(124725)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(124727)
        AmmunitionPanel = DynAccessor(124728)
        Difficulty = DynAccessor(124729)
        MoneyBalance = DynAccessor(124730)
        TeamStats = DynAccessor(124731)
        Meta = DynAccessor(124732)
        Keys = DynAccessor(124733)
        Quests = DynAccessor(124734)
        RewardPath = DynAccessor(124735)
        Shop = DynAccessor(124736)
        Gsw = DynAccessor(124737)
        Switcher = DynAccessor(124738)

    shared = _shared(124739)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(124741)
        ContactsList = DynAccessor(124742)
        SessionStats = DynAccessor(124743)
        VehicleCompare = DynAccessor(124744)
        NotificationsCenter = DynAccessor(124745)
        Chats = DynAccessor(124746)
        ReferralProgram = DynAccessor(124747)
        ServerInfo = DynAccessor(124748)

    default = _default(124749)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(124751)
        NavigationBar = DynAccessor(124752)
        Prebattle = DynAccessor(124753)
        Wallet = DynAccessor(124754)
        AccountDashboard = DynAccessor(124755)
        HeaderState = DynAccessor(124756)
        UserAccount = DynAccessor(124757)
        ReservesEntryPoint = DynAccessor(124758)
        PremShop = DynAccessor(124759)
        CurrentVehicle = DynAccessor(124760)

    default = _default(124761)


class one_time_gift(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        NavigationBar = DynAccessor(124763)
        EquipmentSetTooltip = DynAccessor(124764)

    default = _default(124765)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(124767)
            Instructions = DynAccessor(124768)
            Shells = DynAccessor(124769)
            Consumables = DynAccessor(124770)

        Loadout = _Loadout(124771)
        Vehicles = DynAccessor(124772)

    Hangar = _Hangar(124773)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(124775)
        Events = DynAccessor(124776)
        Quests = DynAccessor(124777)
        EventMainInfoTip = DynAccessor(124778)

    hangarWidget = _hangarWidget(124779)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(124780)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(124781)
                DailyBlock = DynAccessor(124782)
                PremiumBlock = DynAccessor(124783)
                RewardProgressBlock = DynAccessor(124784)

            DailyMissionsSection = _DailyMissionsSection(124785)
            WeeklyMissions = DynAccessor(124786)
            PersonalMissions = DynAccessor(124787)

        basicMissions = _basicMissions(124788)

    hub = _hub(124789)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(124791)
        Wallet = DynAccessor(124792)

    default = _default(124793)


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