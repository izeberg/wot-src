from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(119500)

    shared = _shared(119501)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(119503)
    ExtraVideo = DynAccessor(119504)
    Intro = DynAccessor(119505)
    ChapterChoice = DynAccessor(119506)
    Progression = DynAccessor(119507)
    PostProgression = DynAccessor(119508)
    BuyPass = DynAccessor(119509)
    BuyPassConfirm = DynAccessor(119510)
    BuyPassRewards = DynAccessor(119511)
    BuyLevels = DynAccessor(119512)
    BuyLevelsRewards = DynAccessor(119513)
    HolidayFinal = DynAccessor(119514)
    FinalRewardPreview = DynAccessor(119515)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(119517)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(119518)
        Vehicle = DynAccessor(119519)

    contextMenu = _contextMenu(119520)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(119522)
    UserMissions = DynAccessor(119523)
    VehiclesInventory = DynAccessor(119524)
    VehiclesFilter = DynAccessor(119525)
    AlertMessage = DynAccessor(119526)
    Header = DynAccessor(119527)
    LoadoutPanelContainer = DynAccessor(119528)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(119529)
        EventShop = DynAccessor(119530)

    hangarWidget = _hangarWidget(119531)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(119532)
        Commander = DynAccessor(119533)

    loadoutPanelContainer = _loadoutPanelContainer(119534)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(119536)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(119537)

    contextMenu = _contextMenu(119538)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(119539)
        Wulf = DynAccessor(119540)
        Param = DynAccessor(119541)

    tooltip = _tooltip(119542)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(119543)

    popOver = _popOver(119544)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(119545)

    shared = _shared(119546)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(119548)
        Schedule = DynAccessor(119549)
        SeasonModifier = DynAccessor(119550)
        RoleSkillSlot = DynAccessor(119551)
        UserMissions = DynAccessor(119552)
        EntryPoint = DynAccessor(119553)
        WeeklyQuestsWidget = DynAccessor(119554)

    shared = _shared(119555)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(119557)
        SeasonModifier = DynAccessor(119558)
        RoleSkillSlot = DynAccessor(119559)
        UserMissions = DynAccessor(119560)
        EntryPoint = DynAccessor(119561)
        Quests = DynAccessor(119562)

    shared = _shared(119563)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(119565)

    loadout = _loadout(119566)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(119567)
        AlertMessage = DynAccessor(119568)

    shared = _shared(119569)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(119571)
        ProgressionEntryPoint = DynAccessor(119572)

    shared = _shared(119573)


class halloween(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(119575)
        AmmunitionPanel = DynAccessor(119576)
        Difficulty = DynAccessor(119577)
        MoneyBalance = DynAccessor(119578)
        TeamStats = DynAccessor(119579)
        Meta = DynAccessor(119580)
        Keys = DynAccessor(119581)
        Quests = DynAccessor(119582)
        RewardPath = DynAccessor(119583)
        Shop = DynAccessor(119584)
        Gsw = DynAccessor(119585)
        Switcher = DynAccessor(119586)
        CrewMembers = DynAccessor(119587)

    shared = _shared(119588)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(119590)
        VehiclesStatistics = DynAccessor(119591)
        Consumables = DynAccessor(119592)
        Equipments = DynAccessor(119593)
        Instructions = DynAccessor(119594)
        Shells = DynAccessor(119595)
        Loadout = DynAccessor(119596)
        Crew = DynAccessor(119597)
        VehicleParams = DynAccessor(119598)
        CurrentVehicle = DynAccessor(119599)
        VehiclesInventory = DynAccessor(119600)
        MainMenu = DynAccessor(119601)
        VehicleMenu = DynAccessor(119602)
        LootboxEntryPoint = DynAccessor(119603)
        VehicleFilters = DynAccessor(119604)
        VehiclePlaylists = DynAccessor(119605)
        Teaser = DynAccessor(119606)
        OptionalDevicesAssistant = DynAccessor(119607)
        SpaceInteraction = DynAccessor(119608)
        HeroTank = DynAccessor(119609)
        UserMissions = DynAccessor(119610)
        ModeState = DynAccessor(119611)

    shared = _shared(119612)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(119614)
        AmmunitionPanel = DynAccessor(119615)
        Difficulty = DynAccessor(119616)
        MoneyBalance = DynAccessor(119617)
        TeamStats = DynAccessor(119618)
        Meta = DynAccessor(119619)
        Keys = DynAccessor(119620)
        Quests = DynAccessor(119621)
        RewardPath = DynAccessor(119622)
        Shop = DynAccessor(119623)
        Gsw = DynAccessor(119624)
        Switcher = DynAccessor(119625)

    shared = _shared(119626)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(119628)
        ContactsList = DynAccessor(119629)
        SessionStats = DynAccessor(119630)
        VehicleCompare = DynAccessor(119631)
        NotificationsCenter = DynAccessor(119632)
        Chats = DynAccessor(119633)
        ReferralProgram = DynAccessor(119634)
        ServerInfo = DynAccessor(119635)

    default = _default(119636)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(119638)
        NavigationBar = DynAccessor(119639)
        Prebattle = DynAccessor(119640)
        Wallet = DynAccessor(119641)
        AccountDashboard = DynAccessor(119642)
        HeaderState = DynAccessor(119643)
        UserAccount = DynAccessor(119644)
        ReservesEntryPoint = DynAccessor(119645)
        PremShop = DynAccessor(119646)

    default = _default(119647)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(119649)
            Instructions = DynAccessor(119650)
            Shells = DynAccessor(119651)
            Consumables = DynAccessor(119652)

        Loadout = _Loadout(119653)
        Vehicles = DynAccessor(119654)

    Hangar = _Hangar(119655)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(119657)
        Events = DynAccessor(119658)
        Quests = DynAccessor(119659)
        EventMainInfoTip = DynAccessor(119660)

    hangarWidget = _hangarWidget(119661)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(119662)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(119663)
                DailyBlock = DynAccessor(119664)
                PremiumBlock = DynAccessor(119665)
                RewardProgressBlock = DynAccessor(119666)

            DailyMissionsSection = _DailyMissionsSection(119667)
            WeeklyMissions = DynAccessor(119668)
            PersonalMissions = DynAccessor(119669)

        basicMissions = _basicMissions(119670)

    hub = _hub(119671)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(119673)
        Wallet = DynAccessor(119674)

    default = _default(119675)


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