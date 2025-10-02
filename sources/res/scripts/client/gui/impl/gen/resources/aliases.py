from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(119567)

    shared = _shared(119568)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(119570)
    ExtraVideo = DynAccessor(119571)
    Intro = DynAccessor(119572)
    ChapterChoice = DynAccessor(119573)
    Progression = DynAccessor(119574)
    PostProgression = DynAccessor(119575)
    BuyPass = DynAccessor(119576)
    BuyPassConfirm = DynAccessor(119577)
    BuyPassRewards = DynAccessor(119578)
    BuyLevels = DynAccessor(119579)
    BuyLevelsRewards = DynAccessor(119580)
    HolidayFinal = DynAccessor(119581)
    FinalRewardPreview = DynAccessor(119582)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(119584)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(119585)
        Vehicle = DynAccessor(119586)

    contextMenu = _contextMenu(119587)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(119589)
    UserMissions = DynAccessor(119590)
    VehiclesInventory = DynAccessor(119591)
    VehiclesFilter = DynAccessor(119592)
    AlertMessage = DynAccessor(119593)
    Header = DynAccessor(119594)
    LoadoutPanelContainer = DynAccessor(119595)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(119596)
        EventShop = DynAccessor(119597)

    hangarWidget = _hangarWidget(119598)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(119599)
        Commander = DynAccessor(119600)

    loadoutPanelContainer = _loadoutPanelContainer(119601)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(119603)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(119604)

    contextMenu = _contextMenu(119605)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(119606)
        Wulf = DynAccessor(119607)
        Param = DynAccessor(119608)

    tooltip = _tooltip(119609)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(119610)

    popOver = _popOver(119611)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(119612)

    shared = _shared(119613)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(119615)
        Schedule = DynAccessor(119616)
        SeasonModifier = DynAccessor(119617)
        RoleSkillSlot = DynAccessor(119618)
        UserMissions = DynAccessor(119619)
        EntryPoint = DynAccessor(119620)
        WeeklyQuestsWidget = DynAccessor(119621)

    shared = _shared(119622)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(119624)
        SeasonModifier = DynAccessor(119625)
        RoleSkillSlot = DynAccessor(119626)
        UserMissions = DynAccessor(119627)
        EntryPoint = DynAccessor(119628)
        Quests = DynAccessor(119629)

    shared = _shared(119630)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(119632)

    loadout = _loadout(119633)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(119634)
        AlertMessage = DynAccessor(119635)

    shared = _shared(119636)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(119638)
        ProgressionEntryPoint = DynAccessor(119639)

    shared = _shared(119640)


class halloween(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(119642)
        AmmunitionPanel = DynAccessor(119643)
        Difficulty = DynAccessor(119644)
        MoneyBalance = DynAccessor(119645)
        TeamStats = DynAccessor(119646)
        Meta = DynAccessor(119647)
        Keys = DynAccessor(119648)
        Quests = DynAccessor(119649)
        RewardPath = DynAccessor(119650)
        Shop = DynAccessor(119651)
        Gsw = DynAccessor(119652)
        Switcher = DynAccessor(119653)
        CrewMembers = DynAccessor(119654)

    shared = _shared(119655)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(119657)
        VehiclesStatistics = DynAccessor(119658)
        Consumables = DynAccessor(119659)
        Equipments = DynAccessor(119660)
        Instructions = DynAccessor(119661)
        Shells = DynAccessor(119662)
        Loadout = DynAccessor(119663)
        Crew = DynAccessor(119664)
        VehicleParams = DynAccessor(119665)
        CurrentVehicle = DynAccessor(119666)
        VehiclesInventory = DynAccessor(119667)
        MainMenu = DynAccessor(119668)
        VehicleMenu = DynAccessor(119669)
        LootboxEntryPoint = DynAccessor(119670)
        VehicleFilters = DynAccessor(119671)
        VehiclePlaylists = DynAccessor(119672)
        Teaser = DynAccessor(119673)
        OptionalDevicesAssistant = DynAccessor(119674)
        SpaceInteraction = DynAccessor(119675)
        HeroTank = DynAccessor(119676)
        UserMissions = DynAccessor(119677)
        ModeState = DynAccessor(119678)

    shared = _shared(119679)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(119681)
        AmmunitionPanel = DynAccessor(119682)
        Difficulty = DynAccessor(119683)
        MoneyBalance = DynAccessor(119684)
        TeamStats = DynAccessor(119685)
        Meta = DynAccessor(119686)
        Keys = DynAccessor(119687)
        Quests = DynAccessor(119688)
        RewardPath = DynAccessor(119689)
        Shop = DynAccessor(119690)
        Gsw = DynAccessor(119691)
        Switcher = DynAccessor(119692)

    shared = _shared(119693)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(119695)
        ContactsList = DynAccessor(119696)
        SessionStats = DynAccessor(119697)
        VehicleCompare = DynAccessor(119698)
        NotificationsCenter = DynAccessor(119699)
        Chats = DynAccessor(119700)
        ReferralProgram = DynAccessor(119701)
        ServerInfo = DynAccessor(119702)

    default = _default(119703)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(119705)
        NavigationBar = DynAccessor(119706)
        Prebattle = DynAccessor(119707)
        Wallet = DynAccessor(119708)
        AccountDashboard = DynAccessor(119709)
        HeaderState = DynAccessor(119710)
        UserAccount = DynAccessor(119711)
        ReservesEntryPoint = DynAccessor(119712)
        PremShop = DynAccessor(119713)

    default = _default(119714)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(119716)
            Instructions = DynAccessor(119717)
            Shells = DynAccessor(119718)
            Consumables = DynAccessor(119719)

        Loadout = _Loadout(119720)
        Vehicles = DynAccessor(119721)

    Hangar = _Hangar(119722)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(119724)
        Events = DynAccessor(119725)
        Quests = DynAccessor(119726)
        EventMainInfoTip = DynAccessor(119727)

    hangarWidget = _hangarWidget(119728)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(119729)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(119730)
                DailyBlock = DynAccessor(119731)
                PremiumBlock = DynAccessor(119732)
                RewardProgressBlock = DynAccessor(119733)

            DailyMissionsSection = _DailyMissionsSection(119734)
            WeeklyMissions = DynAccessor(119735)
            PersonalMissions = DynAccessor(119736)

        basicMissions = _basicMissions(119737)

    hub = _hub(119738)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(119740)
        Wallet = DynAccessor(119741)

    default = _default(119742)


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