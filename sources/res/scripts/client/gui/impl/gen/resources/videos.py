from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(111452)
    _tutorialInitialLoop = DynAccessor(111453)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(111454)
        up_particles = DynAccessor(111455)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(111456)
            crewCommander = DynAccessor(111457)
            crewDriver = DynAccessor(111458)
            crewGunner = DynAccessor(111459)
            crewLoader = DynAccessor(111460)
            crewRadioOperator = DynAccessor(111461)
            skillAdrenalineRush = DynAccessor(111462)
            skillArmorer = DynAccessor(111463)
            skillArtLamp = DynAccessor(111464)
            skillBrothersInArms = DynAccessor(111465)
            skillCallForVengeance = DynAccessor(111466)
            skillClutchBraking = DynAccessor(111467)
            skillCommanderBonus = DynAccessor(111468)
            skillConcealment = DynAccessor(111469)
            skillControlledImpact = DynAccessor(111470)
            skillDeadEye = DynAccessor(111471)
            skillDesignatedTarget = DynAccessor(111472)
            skillEagleEye = DynAccessor(111473)
            skillExpert = DynAccessor(111474)
            skillFirefighting = DynAccessor(111475)
            skillIntuition = DynAccessor(111476)
            skillJackOfAllTrades = DynAccessor(111477)
            skillMentor = DynAccessor(111478)
            skillOffRoadDriving = DynAccessor(111479)
            skillPreventativeMaintenance = DynAccessor(111480)
            skillRelaying = DynAccessor(111481)
            skillRepairs = DynAccessor(111482)
            skillSafeStowage = DynAccessor(111483)
            skillSignalBoosting = DynAccessor(111484)
            skillSituationalAwareness = DynAccessor(111485)
            skillSixthSense = DynAccessor(111486)
            skillSmoothRide = DynAccessor(111487)
            skillSnapShot = DynAccessor(111488)
            skillSniper = DynAccessor(111489)
            skillSoundIntelligence = DynAccessor(111490)
            statConcealment = DynAccessor(111491)
            statFirepower = DynAccessor(111492)
            statMobility = DynAccessor(111493)
            statSpotting = DynAccessor(111494)
            statSurvivability = DynAccessor(111495)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(111496)
        ay_gun = DynAccessor(111497)
        ay_tracks = DynAccessor(111498)
        ay_turret = DynAccessor(111499)
        video_reward = DynAccessor(111500)
        video_reward_min = DynAccessor(111501)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmunitionCrit = DynAccessor(111502)
        FueltankCrit = DynAccessor(111503)
        InSafetyWhileNotObserved = DynAccessor(111504)
        KilledWhileObserved = DynAccessor(111505)
        ModuleDamage = DynAccessor(111506)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_191_0 = DynAccessor(111507)
        v_192_0 = DynAccessor(111508)
        v_193_0 = DynAccessor(111509)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(111510)
        Intro = DynAccessor(111511)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(111512)
            overcharge = DynAccessor(111513)
            power_shot = DynAccessor(111514)
            teleport = DynAccessor(111515)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(111516)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(111517)
        example_2 = DynAccessor(111518)
        example_3 = DynAccessor(111519)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(111520)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(111521)
            gold = DynAccessor(111522)
            silver = DynAccessor(111523)
            standart = DynAccessor(111524)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(111525)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(111526)
            small = DynAccessor(111527)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(111528)
            standart = DynAccessor(111529)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(111530)
            standart = DynAccessor(111531)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(111532)
            standart = DynAccessor(111533)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(111534)
            standart = DynAccessor(111535)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(111536)
            mtl_1_35 = DynAccessor(111537)
            mt_drops = DynAccessor(111538)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(111539)
            medium = DynAccessor(111540)
            small = DynAccessor(111541)
            tanks_6 = DynAccessor(111542)
            tanks_7 = DynAccessor(111543)
            tanks_8 = DynAccessor(111544)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _historicalBattles(DynAccessor):
        __slots__ = ()
        godrays = DynAccessor(111545)
        v_mainTake_loop = DynAccessor(111546)
        v_mainTake_start = DynAccessor(111547)

        class _progression_videos(DynAccessor):
            __slots__ = ()
            progression_defence_1 = DynAccessor(111548)
            progression_defence_2 = DynAccessor(111549)
            progression_offence_1 = DynAccessor(111550)

        progression_videos = _progression_videos()

    historicalBattles = _historicalBattles()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(111551)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(111552)
            intro = DynAccessor(111553)
            R239_ST_Molot_02 = DynAccessor(111554)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(111555)
            GB141_Celestial_2_51 = DynAccessor(111556)
            intro = DynAccessor(111557)
            R239_ST_Molot = DynAccessor(111558)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(111559)
            Pl35_CS_57_Sokol = DynAccessor(111560)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(111561)
        option_2 = DynAccessor(111562)
        option_3 = DynAccessor(111563)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(111564)
        Ch57_BZT_70 = DynAccessor(111565)
        F134_ARL_Projet_F = DynAccessor(111566)
        G184_EisBaer = DynAccessor(111567)
        GB140_Champion = DynAccessor(111568)
        R124_Object_279 = DynAccessor(111569)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(111570)
        operation_10 = DynAccessor(111571)
        operation_8 = DynAccessor(111572)
        operation_9 = DynAccessor(111573)
        operation_99 = DynAccessor(111574)
        video_operations_person = DynAccessor(111575)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(111576)

    platoon = _platoon()

    class _startup(DynAccessor):
        __slots__ = ()
        c_1_42_showreel = DynAccessor(111577)

    startup = _startup()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(111578)

    vehicle = _vehicle()