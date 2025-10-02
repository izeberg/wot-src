from gui.impl.gen_utils import DynAccessor

class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(120447)
    ExtraVideo = DynAccessor(120448)
    Intro = DynAccessor(120449)
    ChapterChoice = DynAccessor(120450)
    Progression = DynAccessor(120451)
    PostProgression = DynAccessor(120452)
    BuyPass = DynAccessor(120453)
    BuyPassConfirm = DynAccessor(120454)
    BuyPassRewards = DynAccessor(120455)
    BuyLevels = DynAccessor(120456)
    BuyLevelsRewards = DynAccessor(120457)
    HolidayFinal = DynAccessor(120458)
    FinalRewardPreview = DynAccessor(120459)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(120461)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(120462)
        Vehicle = DynAccessor(120463)

    contextMenu = _contextMenu(120464)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(120466)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(120467)

    contextMenu = _contextMenu(120468)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(120469)
        Wulf = DynAccessor(120470)
        Param = DynAccessor(120471)

    tooltip = _tooltip(120472)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(120473)

    popOver = _popOver(120474)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(120476)
        Schedule = DynAccessor(120477)
        SeasonModifier = DynAccessor(120478)
        RoleSkillSlot = DynAccessor(120479)
        UserMissions = DynAccessor(120480)
        EntryPoint = DynAccessor(120481)
        WeeklyQuestsWidget = DynAccessor(120482)

    shared = _shared(120483)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(120485)
        SeasonModifier = DynAccessor(120486)
        RoleSkillSlot = DynAccessor(120487)
        UserMissions = DynAccessor(120488)
        EntryPoint = DynAccessor(120489)
        Quests = DynAccessor(120490)

    shared = _shared(120491)


class halloween(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(120493)
        Keys = DynAccessor(120494)
        AmmunitionPanel = DynAccessor(120495)
        Difficulty = DynAccessor(120496)
        Meta = DynAccessor(120497)
        MoneyBalance = DynAccessor(120498)
        TeamStats = DynAccessor(120499)

    shared = _shared(120500)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(120502)
        VehiclesStatistics = DynAccessor(120503)
        Consumables = DynAccessor(120504)
        Equipments = DynAccessor(120505)
        Instructions = DynAccessor(120506)
        Shells = DynAccessor(120507)
        Loadout = DynAccessor(120508)
        Crew = DynAccessor(120509)
        VehicleParams = DynAccessor(120510)
        CurrentVehicle = DynAccessor(120511)
        VehiclesInventory = DynAccessor(120512)
        MainMenu = DynAccessor(120513)
        VehicleMenu = DynAccessor(120514)
        LootboxEntryPoint = DynAccessor(120515)
        VehicleFilters = DynAccessor(120516)
        VehiclePlaylists = DynAccessor(120517)
        Teaser = DynAccessor(120518)
        OptionalDevicesAssistant = DynAccessor(120519)
        SpaceInteraction = DynAccessor(120520)
        HeroTank = DynAccessor(120521)
        UserMissions = DynAccessor(120522)

    shared = _shared(120523)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(120525)
        AmmunitionPanel = DynAccessor(120526)
        Difficulty = DynAccessor(120527)
        MoneyBalance = DynAccessor(120528)
        TeamStats = DynAccessor(120529)
        Meta = DynAccessor(120530)
        Keys = DynAccessor(120531)
        Quests = DynAccessor(120532)
        RewardPath = DynAccessor(120533)
        Shop = DynAccessor(120534)
        Gsw = DynAccessor(120535)
        Switcher = DynAccessor(120536)

    shared = _shared(120537)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(120539)
        ContactsList = DynAccessor(120540)
        SessionStats = DynAccessor(120541)
        VehicleCompare = DynAccessor(120542)
        NotificationsCenter = DynAccessor(120543)
        Chats = DynAccessor(120544)
        ReferralProgram = DynAccessor(120545)
        ServerInfo = DynAccessor(120546)

    default = _default(120547)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(120549)
        NavigationBar = DynAccessor(120550)
        Prebattle = DynAccessor(120551)
        Wallet = DynAccessor(120552)
        AccountDashboard = DynAccessor(120553)
        HeaderState = DynAccessor(120554)
        UserAccount = DynAccessor(120555)
        ReservesEntryPoint = DynAccessor(120556)
        PremShop = DynAccessor(120557)

    default = _default(120558)


class one_time_gift(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        NavigationBar = DynAccessor(120560)
        EquipmentSetTooltip = DynAccessor(120561)

    default = _default(120562)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(120564)
            Instructions = DynAccessor(120565)
            Shells = DynAccessor(120566)
            Consumables = DynAccessor(120567)

        Loadout = _Loadout(120568)
        Vehicles = DynAccessor(120569)

    Hangar = _Hangar(120570)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(120572)
        Events = DynAccessor(120573)
        Quests = DynAccessor(120574)
        EventMainInfoTip = DynAccessor(120575)

    hangarWidget = _hangarWidget(120576)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(120577)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(120578)
                DailyBlock = DynAccessor(120579)
                PremiumBlock = DynAccessor(120580)
                RewardProgressBlock = DynAccessor(120581)

            DailyMissionsSection = _DailyMissionsSection(120582)
            WeeklyMissions = DynAccessor(120583)
            PersonalMissions = DynAccessor(120584)

        basicMissions = _basicMissions(120585)

    hub = _hub(120586)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(120588)
        Wallet = DynAccessor(120589)

    default = _default(120590)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(120592)
        ConsumablesPanel = DynAccessor(120593)
        Progression = DynAccessor(120594)
        Crewman = DynAccessor(120595)
        VehicleStats = DynAccessor(120596)
        ProgressionContent = DynAccessor(120597)
        ProgressionQuests = DynAccessor(120598)
        LootboxEntryPoint = DynAccessor(120599)

    shared = _shared(120600)


class Aliases(DynAccessor):
    __slots__ = ()
    battle_pass = battle_pass()
    battle_result = battle_result()
    common = common()
    comp7 = comp7()
    comp7_light = comp7_light()
    halloween = halloween()
    hangar = hangar()
    last_stand = last_stand()
    lobby_footer = lobby_footer()
    lobby_header = lobby_header()
    one_time_gift = one_time_gift()
    states = states()
    user_missions = user_missions()
    vehicle_hub = vehicle_hub()
    white_tiger = white_tiger()