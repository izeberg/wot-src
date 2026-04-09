from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(111450)
    _tutorialInitialLoop = DynAccessor(111451)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(111452)
        up_particles = DynAccessor(111453)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(111454)
            crewCommander = DynAccessor(111455)
            crewDriver = DynAccessor(111456)
            crewGunner = DynAccessor(111457)
            crewLoader = DynAccessor(111458)
            crewRadioOperator = DynAccessor(111459)
            skillAdrenalineRush = DynAccessor(111460)
            skillArmorer = DynAccessor(111461)
            skillArtLamp = DynAccessor(111462)
            skillBrothersInArms = DynAccessor(111463)
            skillCallForVengeance = DynAccessor(111464)
            skillClutchBraking = DynAccessor(111465)
            skillCommanderBonus = DynAccessor(111466)
            skillConcealment = DynAccessor(111467)
            skillControlledImpact = DynAccessor(111468)
            skillDeadEye = DynAccessor(111469)
            skillDesignatedTarget = DynAccessor(111470)
            skillEagleEye = DynAccessor(111471)
            skillExpert = DynAccessor(111472)
            skillFirefighting = DynAccessor(111473)
            skillIntuition = DynAccessor(111474)
            skillJackOfAllTrades = DynAccessor(111475)
            skillMentor = DynAccessor(111476)
            skillOffRoadDriving = DynAccessor(111477)
            skillPreventativeMaintenance = DynAccessor(111478)
            skillRelaying = DynAccessor(111479)
            skillRepairs = DynAccessor(111480)
            skillSafeStowage = DynAccessor(111481)
            skillSignalBoosting = DynAccessor(111482)
            skillSituationalAwareness = DynAccessor(111483)
            skillSixthSense = DynAccessor(111484)
            skillSmoothRide = DynAccessor(111485)
            skillSnapShot = DynAccessor(111486)
            skillSniper = DynAccessor(111487)
            skillSoundIntelligence = DynAccessor(111488)
            statConcealment = DynAccessor(111489)
            statFirepower = DynAccessor(111490)
            statMobility = DynAccessor(111491)
            statSpotting = DynAccessor(111492)
            statSurvivability = DynAccessor(111493)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(111494)
        ay_gun = DynAccessor(111495)
        ay_tracks = DynAccessor(111496)
        ay_turret = DynAccessor(111497)
        video_reward = DynAccessor(111498)
        video_reward_min = DynAccessor(111499)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmunitionCrit = DynAccessor(111500)
        FueltankCrit = DynAccessor(111501)
        InSafetyWhileNotObserved = DynAccessor(111502)
        KilledWhileObserved = DynAccessor(111503)
        ModuleDamage = DynAccessor(111504)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_191_0 = DynAccessor(111505)
        v_192_0 = DynAccessor(111506)
        v_193_0 = DynAccessor(111507)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(111508)
        Intro = DynAccessor(111509)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(111510)
            overcharge = DynAccessor(111511)
            power_shot = DynAccessor(111512)
            teleport = DynAccessor(111513)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(111514)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(111515)
        example_2 = DynAccessor(111516)
        example_3 = DynAccessor(111517)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(111518)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(111519)
            gold = DynAccessor(111520)
            silver = DynAccessor(111521)
            standart = DynAccessor(111522)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(111523)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(111524)
            small = DynAccessor(111525)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(111526)
            standart = DynAccessor(111527)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(111528)
            standart = DynAccessor(111529)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(111530)
            standart = DynAccessor(111531)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(111532)
            standart = DynAccessor(111533)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(111534)
            mtl_1_35 = DynAccessor(111535)
            mt_drops = DynAccessor(111536)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(111537)
            medium = DynAccessor(111538)
            small = DynAccessor(111539)
            tanks_6 = DynAccessor(111540)
            tanks_7 = DynAccessor(111541)
            tanks_8 = DynAccessor(111542)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _historicalBattles(DynAccessor):
        __slots__ = ()
        godrays = DynAccessor(111543)
        v_mainTake_loop = DynAccessor(111544)
        v_mainTake_start = DynAccessor(111545)

        class _progression_videos(DynAccessor):
            __slots__ = ()
            progression_defence_1 = DynAccessor(111546)
            progression_defence_2 = DynAccessor(111547)
            progression_offence_1 = DynAccessor(111548)

        progression_videos = _progression_videos()

    historicalBattles = _historicalBattles()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(111549)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(111550)
            intro = DynAccessor(111551)
            R239_ST_Molot_02 = DynAccessor(111552)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(111553)
            GB141_Celestial_2_51 = DynAccessor(111554)
            intro = DynAccessor(111555)
            R239_ST_Molot = DynAccessor(111556)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(111557)
            Pl35_CS_57_Sokol = DynAccessor(111558)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(111559)
        option_2 = DynAccessor(111560)
        option_3 = DynAccessor(111561)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(111562)
        Ch57_BZT_70 = DynAccessor(111563)
        F134_ARL_Projet_F = DynAccessor(111564)
        G184_EisBaer = DynAccessor(111565)
        GB140_Champion = DynAccessor(111566)
        R124_Object_279 = DynAccessor(111567)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(111568)
        operation_10 = DynAccessor(111569)
        operation_8 = DynAccessor(111570)
        operation_9 = DynAccessor(111571)
        operation_99 = DynAccessor(111572)
        video_operations_person = DynAccessor(111573)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(111574)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(111575)

    vehicle = _vehicle()