from gui.impl.gen_utils import DynAccessor

class battle_pass(DynAccessor):
    __slots__ = ()
    IntroVideo = DynAccessor(120290)
    ExtraVideo = DynAccessor(120291)
    Intro = DynAccessor(120292)
    ChapterChoice = DynAccessor(120293)
    Progression = DynAccessor(120294)
    PostProgression = DynAccessor(120295)
    BuyPass = DynAccessor(120296)
    BuyPassConfirm = DynAccessor(120297)
    BuyPassRewards = DynAccessor(120298)
    BuyLevels = DynAccessor(120299)
    BuyLevelsRewards = DynAccessor(120300)
    HolidayFinal = DynAccessor(120301)
    FinalRewardPreview = DynAccessor(120302)


class battle_result(DynAccessor):
    __slots__ = ()
    none = DynAccessor(120304)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        User = DynAccessor(120305)
        Vehicle = DynAccessor(120306)

    contextMenu = _contextMenu(120307)


class common(DynAccessor):
    __slots__ = ()
    none = DynAccessor(120309)

    class _contextMenu(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(120310)

    contextMenu = _contextMenu(120311)

    class _tooltip(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(120312)
        Wulf = DynAccessor(120313)
        Param = DynAccessor(120314)

    tooltip = _tooltip(120315)

    class _popOver(DynAccessor):
        __slots__ = ()
        Backport = DynAccessor(120316)

    popOver = _popOver(120317)


class comp7(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(120319)
        Schedule = DynAccessor(120320)
        SeasonModifier = DynAccessor(120321)
        RoleSkillSlot = DynAccessor(120322)
        UserMissions = DynAccessor(120323)
        EntryPoint = DynAccessor(120324)
        WeeklyQuestsWidget = DynAccessor(120325)

    shared = _shared(120326)


class comp7_light(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        AlertMessage = DynAccessor(120328)
        SeasonModifier = DynAccessor(120329)
        RoleSkillSlot = DynAccessor(120330)
        UserMissions = DynAccessor(120331)
        EntryPoint = DynAccessor(120332)
        Quests = DynAccessor(120333)

    shared = _shared(120334)


class halloween(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(120336)
        Keys = DynAccessor(120337)
        AmmunitionPanel = DynAccessor(120338)
        Difficulty = DynAccessor(120339)
        Meta = DynAccessor(120340)
        MoneyBalance = DynAccessor(120341)
        TeamStats = DynAccessor(120342)

    shared = _shared(120343)


class hangar(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        VehiclesInfo = DynAccessor(120345)
        VehiclesStatistics = DynAccessor(120346)
        Consumables = DynAccessor(120347)
        Equipments = DynAccessor(120348)
        Instructions = DynAccessor(120349)
        Shells = DynAccessor(120350)
        Loadout = DynAccessor(120351)
        Crew = DynAccessor(120352)
        VehicleParams = DynAccessor(120353)
        CurrentVehicle = DynAccessor(120354)
        VehiclesInventory = DynAccessor(120355)
        MainMenu = DynAccessor(120356)
        VehicleMenu = DynAccessor(120357)
        LootboxEntryPoint = DynAccessor(120358)
        VehicleFilters = DynAccessor(120359)
        VehiclePlaylists = DynAccessor(120360)
        Teaser = DynAccessor(120361)
        OptionalDevicesAssistant = DynAccessor(120362)
        SpaceInteraction = DynAccessor(120363)
        HeroTank = DynAccessor(120364)
        UserMissions = DynAccessor(120365)

    shared = _shared(120366)


class last_stand(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(120368)
        AmmunitionPanel = DynAccessor(120369)
        Difficulty = DynAccessor(120370)
        MoneyBalance = DynAccessor(120371)
        TeamStats = DynAccessor(120372)
        Meta = DynAccessor(120373)
        Keys = DynAccessor(120374)
        Quests = DynAccessor(120375)
        RewardPath = DynAccessor(120376)
        Shop = DynAccessor(120377)
        Gsw = DynAccessor(120378)
        Switcher = DynAccessor(120379)

    shared = _shared(120380)


class lobby_footer(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        Platoon = DynAccessor(120382)
        ContactsList = DynAccessor(120383)
        SessionStats = DynAccessor(120384)
        VehicleCompare = DynAccessor(120385)
        NotificationsCenter = DynAccessor(120386)
        Chats = DynAccessor(120387)
        ReferralProgram = DynAccessor(120388)
        ServerInfo = DynAccessor(120389)

    default = _default(120390)


class lobby_header(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        FightStart = DynAccessor(120392)
        NavigationBar = DynAccessor(120393)
        Prebattle = DynAccessor(120394)
        Wallet = DynAccessor(120395)
        AccountDashboard = DynAccessor(120396)
        HeaderState = DynAccessor(120397)
        UserAccount = DynAccessor(120398)
        ReservesEntryPoint = DynAccessor(120399)
        PremShop = DynAccessor(120400)

    default = _default(120401)


class one_time_gift(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        NavigationBar = DynAccessor(120403)
        EquipmentSetTooltip = DynAccessor(120404)

    default = _default(120405)


class states(DynAccessor):
    __slots__ = ()

    class _Hangar(DynAccessor):
        __slots__ = ()

        class _Loadout(DynAccessor):
            __slots__ = ()
            Equipment = DynAccessor(120407)
            Instructions = DynAccessor(120408)
            Shells = DynAccessor(120409)
            Consumables = DynAccessor(120410)

        Loadout = _Loadout(120411)
        Vehicles = DynAccessor(120412)

    Hangar = _Hangar(120413)


class user_missions(DynAccessor):
    __slots__ = ()

    class _hangarWidget(DynAccessor):
        __slots__ = ()
        BattlePass = DynAccessor(120415)
        Events = DynAccessor(120416)
        Quests = DynAccessor(120417)
        EventMainInfoTip = DynAccessor(120418)

    hangarWidget = _hangarWidget(120419)

    class _hub(DynAccessor):
        __slots__ = ()

        class _basicMissions(DynAccessor):
            __slots__ = ()
            MainView = DynAccessor(120420)

            class _DailyMissionsSection(DynAccessor):
                __slots__ = ()
                MainView = DynAccessor(120421)
                DailyBlock = DynAccessor(120422)
                PremiumBlock = DynAccessor(120423)
                RewardProgressBlock = DynAccessor(120424)

            DailyMissionsSection = _DailyMissionsSection(120425)
            WeeklyMissions = DynAccessor(120426)
            PersonalMissions = DynAccessor(120427)

        basicMissions = _basicMissions(120428)

    hub = _hub(120429)


class vehicle_hub(DynAccessor):
    __slots__ = ()

    class _default(DynAccessor):
        __slots__ = ()
        VehicleParams = DynAccessor(120431)
        Wallet = DynAccessor(120432)

    default = _default(120433)


class white_tiger(DynAccessor):
    __slots__ = ()

    class _shared(DynAccessor):
        __slots__ = ()
        Carousel = DynAccessor(120435)
        ConsumablesPanel = DynAccessor(120436)
        Progression = DynAccessor(120437)
        Crewman = DynAccessor(120438)
        VehicleStats = DynAccessor(120439)
        ProgressionContent = DynAccessor(120440)
        ProgressionQuests = DynAccessor(120441)
        LootboxEntryPoint = DynAccessor(120442)

    shared = _shared(120443)


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