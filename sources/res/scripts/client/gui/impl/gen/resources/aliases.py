from gui.impl.gen_utils import DynAccessor

class battle_modifiers(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Modifiers = DynAccessor(124424)

    shared = _shared(124425)


class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(124427)
    ExtraVideo = DynAccessor(124428)
    Intro = DynAccessor(124429)
    ChapterChoice = DynAccessor(124430)
    Progression = DynAccessor(124431)
    PostProgression = DynAccessor(124432)
    BuyPass = DynAccessor(124433)
    BuyPassConfirm = DynAccessor(124434)
    BuyPassRewards = DynAccessor(124435)
    BuyLevels = DynAccessor(124436)
    BuyLevelsRewards = DynAccessor(124437)
    HolidayFinal = DynAccessor(124438)
    FinalRewardPreview = DynAccessor(124439)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(124441)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(124442)
        Vehicle = DynAccessor(124443)

    contextMenu = _contextMenu(124444)


class battle_results(DynAccessor):
    __slots__ = ()

    class _progression(DynAccessor):
        __slots__ = ()
        DailyMissions = DynAccessor(124446)
        WeeklyMissions = DynAccessor(124447)
        PersonalMissions = DynAccessor(124448)
        BattlePass = DynAccessor(124449)
        Prestige = DynAccessor(124450)
        BattleMatters = DynAccessor(124451)
        ModuleVehicleUnlocks = DynAccessor(124452)
        CommonQuests = DynAccessor(124453)

    progression = _progression(124454)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(124456)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(124457)

    contextMenu = _contextMenu(124458)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(124459)
        Wulf = DynAccessor(124460)
        Param = DynAccessor(124461)

    tooltip = _tooltip(124462)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(124463)

    popOver = _popOver(124464)

    class _shared(DynAccessor):
        __slots__ = ()
        DynamicEconomics = DynAccessor(124465)

    shared = _shared(124466)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(124468)
        VehiclesStatistics = DynAccessor(124469)
        Consumables = DynAccessor(124470)
        Equipments = DynAccessor(124471)
        Instructions = DynAccessor(124472)
        Shells = DynAccessor(124473)
        Loadout = DynAccessor(124474)
        Crew = DynAccessor(124475)
        VehicleParams = DynAccessor(124476)
        ETEVehicleParams = DynAccessor(124477)
        CurrentVehicle = DynAccessor(124478)
        VehiclesInventory = DynAccessor(124479)
        MainMenu = DynAccessor(124480)
        VehicleMenu = DynAccessor(124481)
        LootboxEntryPoint = DynAccessor(124482)
        VehicleFilters = DynAccessor(124483)
        VehiclePlaylists = DynAccessor(124484)
        Teaser = DynAccessor(124485)
        OptionalDevicesAssistant = DynAccessor(124486)
        SpaceInteraction = DynAccessor(124487)
        HeroTank = DynAccessor(124488)
        UserMissions = DynAccessor(124489)
        ModeState = DynAccessor(124490)
        EasyTankEquip = DynAccessor(124491)
        PetEvent = DynAccessor(124492)
        PetObjectTooltip = DynAccessor(124493)
        Settings = DynAccessor(124494)
        KeyBindings = DynAccessor(124495)

    shared = _shared(124496)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(124498)
        ContactsList = DynAccessor(124499)
        SessionStats = DynAccessor(124500)
        VehicleCompare = DynAccessor(124501)
        NotificationsCenter = DynAccessor(124502)
        Chats = DynAccessor(124503)
        ReferralProgram = DynAccessor(124504)
        ServerInfo = DynAccessor(124505)

    default = _default(124506)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(124508)
        NavigationBar = DynAccessor(124509)
        Prebattle = DynAccessor(124510)
        Wallet = DynAccessor(124511)
        AccountDashboard = DynAccessor(124512)
        HeaderState = DynAccessor(124513)
        UserAccount = DynAccessor(124514)
        ReservesEntryPoint = DynAccessor(124515)
        PremShop = DynAccessor(124516)
        CurrentVehicle = DynAccessor(124517)

    default = _default(124518)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(124520)
            Instructions = DynAccessor(124521)
            Shells = DynAccessor(124522)
            Consumables = DynAccessor(124523)

        Loadout = _Loadout(124524)
        Vehicles = DynAccessor(124525)

    Hangar = _Hangar(124526)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(124528)
        Events = DynAccessor(124529)
        Quests = DynAccessor(124530)
        EventMainInfoTip = DynAccessor(124531)

    hangarWidget = _hangarWidget(124532)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(124533)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(124534)
                DailyBlock = DynAccessor(124535)
                PremiumBlock = DynAccessor(124536)
                RewardProgressBlock = DynAccessor(124537)

            DailyMissionsSection = _DailyMissionsSection(124538)
            WeeklyMissions = DynAccessor(124539)
            PersonalMissions = DynAccessor(124540)

        basicMissions = _basicMissions(124541)

    hub = _hub(124542)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(124544)
        Wallet = DynAccessor(124545)

    default = _default(124546)


class battle_royale(DynAccessor):
    __slots__ = ()
    BattleSelector = DynAccessor(124548)
    UserMissions = DynAccessor(124549)
    VehiclesInventory = DynAccessor(124550)
    VehiclesFilter = DynAccessor(124551)
    AlertMessage = DynAccessor(124552)
    Header = DynAccessor(124553)
    LoadoutPanelContainer = DynAccessor(124554)

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        Progression = DynAccessor(124555)
        EventShop = DynAccessor(124556)

    hangarWidget = _hangarWidget(124557)

    class _loadoutPanelContainer(DynAccessor):
        __slots__ = ()
        Loadout = DynAccessor(124558)
        Commander = DynAccessor(124559)

    loadoutPanelContainer = _loadoutPanelContainer(124560)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(124562)
        Schedule = DynAccessor(124563)
        SeasonModifier = DynAccessor(124564)
        RoleSkillSlot = DynAccessor(124565)
        UserMissions = DynAccessor(124566)
        EntryPoint = DynAccessor(124567)
        WeeklyQuestsWidget = DynAccessor(124568)

    shared = _shared(124569)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(124571)
        SeasonModifier = DynAccessor(124572)
        RoleSkillSlot = DynAccessor(124573)
        UserMissions = DynAccessor(124574)
        EntryPoint = DynAccessor(124575)
        Quests = DynAccessor(124576)

    shared = _shared(124577)


class frontline(DynAccessor):
    __slots__ = ()

    class _loadout(DynAccessor):
        __slots__ = ()
        BattleAbilities = DynAccessor(124579)

    loadout = _loadout(124580)

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(124581)
        AlertMessage = DynAccessor(124582)

    shared = _shared(124583)


class fun_random(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        UserMissions = DynAccessor(124585)
        ProgressionEntryPoint = DynAccessor(124586)

    shared = _shared(124587)


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
    states = states()
    user_missions = user_missions()
    vehicle_hub = vehicle_hub()
    battle_royale = battle_royale()
    comp7 = comp7()
    comp7_light = comp7_light()
    frontline = frontline()
    fun_random = fun_random()