from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(118083)

    shared = _shared(118084)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(118086)
    ExtraVideo = DynAccessor(118087)
    Intro = DynAccessor(118088)
    ChapterChoice = DynAccessor(118089)
    Progression = DynAccessor(118090)
    PostProgression = DynAccessor(118091)
    BuyPass = DynAccessor(118092)
    BuyPassConfirm = DynAccessor(118093)
    BuyPassRewards = DynAccessor(118094)
    BuyLevels = DynAccessor(118095)
    BuyLevelsRewards = DynAccessor(118096)
    HolidayFinal = DynAccessor(118097)
    FinalRewardPreview = DynAccessor(118098)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(118100)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(118101)
        Vehicle = DynAccessor(118102)

    contextMenu = _contextMenu(118103)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(118105)
    UserMissions = DynAccessor(118106)
    VehiclesInventory = DynAccessor(118107)
    VehiclesFilter = DynAccessor(118108)
    AlertMessage = DynAccessor(118109)
    Header = DynAccessor(118110)
    LoadoutPanelContainer = DynAccessor(118111)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(118112)
        EventShop = DynAccessor(118113)

    hangarWidget = _hangarWidget(118114)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(118115)
        Commander = DynAccessor(118116)

    loadoutPanelContainer = _loadoutPanelContainer(118117)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(118119)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(118120)

    contextMenu = _contextMenu(118121)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(118122)
        Wulf = DynAccessor(118123)
        Param = DynAccessor(118124)

    tooltip = _tooltip(118125)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(118126)

    popOver = _popOver(118127)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(118128)

    shared = _shared(118129)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(118131)
        Schedule = DynAccessor(118132)
        SeasonModifier = DynAccessor(118133)
        RoleSkillSlot = DynAccessor(118134)
        UserMissions = DynAccessor(118135)
        EntryPoint = DynAccessor(118136)
        WeeklyQuestsWidget = DynAccessor(118137)

    shared = _shared(118138)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(118140)
        SeasonModifier = DynAccessor(118141)
        RoleSkillSlot = DynAccessor(118142)
        UserMissions = DynAccessor(118143)
        EntryPoint = DynAccessor(118144)
        Quests = DynAccessor(118145)

    shared = _shared(118146)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(118148)

    loadout = _loadout(118149)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(118150)
        AlertMessage = DynAccessor(118151)

    shared = _shared(118152)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(118154)
        ProgressionEntryPoint = DynAccessor(118155)

    shared = _shared(118156)


class halloween(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(118158)
        AmmunitionPanel = DynAccessor(118159)
        Difficulty = DynAccessor(118160)
        MoneyBalance = DynAccessor(118161)
        TeamStats = DynAccessor(118162)
        Meta = DynAccessor(118163)
        Keys = DynAccessor(118164)
        Quests = DynAccessor(118165)
        RewardPath = DynAccessor(118166)
        Shop = DynAccessor(118167)
        Gsw = DynAccessor(118168)
        Switcher = DynAccessor(118169)
        CrewMembers = DynAccessor(118170)

    shared = _shared(118171)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(118173)
        VehiclesStatistics = DynAccessor(118174)
        Consumables = DynAccessor(118175)
        Equipments = DynAccessor(118176)
        Instructions = DynAccessor(118177)
        Shells = DynAccessor(118178)
        Loadout = DynAccessor(118179)
        Crew = DynAccessor(118180)
        VehicleParams = DynAccessor(118181)
        CurrentVehicle = DynAccessor(118182)
        VehiclesInventory = DynAccessor(118183)
        MainMenu = DynAccessor(118184)
        VehicleMenu = DynAccessor(118185)
        LootboxEntryPoint = DynAccessor(118186)
        VehicleFilters = DynAccessor(118187)
        VehiclePlaylists = DynAccessor(118188)
        Teaser = DynAccessor(118189)
        OptionalDevicesAssistant = DynAccessor(118190)
        SpaceInteraction = DynAccessor(118191)
        HeroTank = DynAccessor(118192)
        UserMissions = DynAccessor(118193)
        ModeState = DynAccessor(118194)
        PetEvent = DynAccessor(118195)
        PetObjectTooltip = DynAccessor(118196)
        Settings = DynAccessor(118197)
        KeyBindings = DynAccessor(118198)

    shared = _shared(118199)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(118201)
        AmmunitionPanel = DynAccessor(118202)
        Difficulty = DynAccessor(118203)
        MoneyBalance = DynAccessor(118204)
        TeamStats = DynAccessor(118205)
        Meta = DynAccessor(118206)
        Keys = DynAccessor(118207)
        Quests = DynAccessor(118208)
        RewardPath = DynAccessor(118209)
        Shop = DynAccessor(118210)
        Gsw = DynAccessor(118211)
        Switcher = DynAccessor(118212)

    shared = _shared(118213)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(118215)
        ContactsList = DynAccessor(118216)
        SessionStats = DynAccessor(118217)
        VehicleCompare = DynAccessor(118218)
        NotificationsCenter = DynAccessor(118219)
        Chats = DynAccessor(118220)
        ReferralProgram = DynAccessor(118221)
        ServerInfo = DynAccessor(118222)

    default = _default(118223)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(118225)
        NavigationBar = DynAccessor(118226)
        Prebattle = DynAccessor(118227)
        Wallet = DynAccessor(118228)
        AccountDashboard = DynAccessor(118229)
        HeaderState = DynAccessor(118230)
        UserAccount = DynAccessor(118231)
        ReservesEntryPoint = DynAccessor(118232)
        PremShop = DynAccessor(118233)
        CurrentVehicle = DynAccessor(118234)

    default = _default(118235)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(118237)
            Instructions = DynAccessor(118238)
            Shells = DynAccessor(118239)
            Consumables = DynAccessor(118240)

        Loadout = _Loadout(118241)
        Vehicles = DynAccessor(118242)

    Hangar = _Hangar(118243)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(118245)
        Events = DynAccessor(118246)
        Quests = DynAccessor(118247)
        EventMainInfoTip = DynAccessor(118248)

    hangarWidget = _hangarWidget(118249)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(118250)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(118251)
                DailyBlock = DynAccessor(118252)
                PremiumBlock = DynAccessor(118253)
                RewardProgressBlock = DynAccessor(118254)

            DailyMissionsSection = _DailyMissionsSection(118255)
            WeeklyMissions = DynAccessor(118256)
            PersonalMissions = DynAccessor(118257)

        basicMissions = _basicMissions(118258)

    hub = _hub(118259)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(118261)
        Wallet = DynAccessor(118262)

    default = _default(118263)


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