from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(109308)
    _tutorialInitialLoop = DynAccessor(109309)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(109310)
        up_particles = DynAccessor(109311)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(109312)
            crewCommander = DynAccessor(109313)
            crewDriver = DynAccessor(109314)
            crewGunner = DynAccessor(109315)
            crewLoader = DynAccessor(109316)
            crewRadioOperator = DynAccessor(109317)
            skillAdrenalineRush = DynAccessor(109318)
            skillArmorer = DynAccessor(109319)
            skillArtLamp = DynAccessor(109320)
            skillBrothersInArms = DynAccessor(109321)
            skillCallForVengeance = DynAccessor(109322)
            skillClutchBraking = DynAccessor(109323)
            skillCommanderBonus = DynAccessor(109324)
            skillConcealment = DynAccessor(109325)
            skillControlledImpact = DynAccessor(109326)
            skillDeadEye = DynAccessor(109327)
            skillDesignatedTarget = DynAccessor(109328)
            skillEagleEye = DynAccessor(109329)
            skillExpert = DynAccessor(109330)
            skillFirefighting = DynAccessor(109331)
            skillIntuition = DynAccessor(109332)
            skillJackOfAllTrades = DynAccessor(109333)
            skillMentor = DynAccessor(109334)
            skillOffRoadDriving = DynAccessor(109335)
            skillPreventativeMaintenance = DynAccessor(109336)
            skillRelaying = DynAccessor(109337)
            skillRepairs = DynAccessor(109338)
            skillSafeStowage = DynAccessor(109339)
            skillSignalBoosting = DynAccessor(109340)
            skillSituationalAwareness = DynAccessor(109341)
            skillSixthSense = DynAccessor(109342)
            skillSmoothRide = DynAccessor(109343)
            skillSnapShot = DynAccessor(109344)
            skillSniper = DynAccessor(109345)
            skillSoundIntelligence = DynAccessor(109346)
            statConcealment = DynAccessor(109347)
            statFirepower = DynAccessor(109348)
            statMobility = DynAccessor(109349)
            statSpotting = DynAccessor(109350)
            statSurvivability = DynAccessor(109351)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(109352)
        ay_gun = DynAccessor(109353)
        ay_tracks = DynAccessor(109354)
        ay_turret = DynAccessor(109355)
        video_reward = DynAccessor(109356)
        video_reward_min = DynAccessor(109357)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmunitionCrit = DynAccessor(109358)
        FueltankCrit = DynAccessor(109359)
        InSafetyWhileNotObserved = DynAccessor(109360)
        KilledWhileObserved = DynAccessor(109361)
        ModuleDamage = DynAccessor(109362)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_201_0 = DynAccessor(109363)
        v_202_0 = DynAccessor(109364)
        v_203_0 = DynAccessor(109365)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(109366)
        Intro = DynAccessor(109367)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(109368)
            overcharge = DynAccessor(109369)
            power_shot = DynAccessor(109370)
            teleport = DynAccessor(109371)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(109372)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(109373)
        example_2 = DynAccessor(109374)
        example_3 = DynAccessor(109375)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(109376)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(109377)
            gold = DynAccessor(109378)
            silver = DynAccessor(109379)
            standart = DynAccessor(109380)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(109381)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(109382)
            small = DynAccessor(109383)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(109384)
            standart = DynAccessor(109385)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(109386)
            standart = DynAccessor(109387)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(109388)
            standart = DynAccessor(109389)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(109390)
            standart = DynAccessor(109391)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(109392)
            mtl_1_35 = DynAccessor(109393)
            mtl_1_43 = DynAccessor(109394)
            mt_drops = DynAccessor(109395)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(109396)
            medium = DynAccessor(109397)
            small = DynAccessor(109398)
            tanks_6 = DynAccessor(109399)
            tanks_7 = DynAccessor(109400)
            tanks_8 = DynAccessor(109401)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(109402)
            R149_Object_268_4_02 = DynAccessor(109403)
            R177_ISU_152K_BL10_02 = DynAccessor(109404)
            R248_T44_Storm = DynAccessor(109405)
            R45_IS_7_02 = DynAccessor(109406)
            Un24_Vz_68_2_Britva = DynAccessor(109407)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(109408)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(109409)
            intro = DynAccessor(109410)
            R239_ST_Molot_02 = DynAccessor(109411)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(109412)
            GB141_Celestial_2_51 = DynAccessor(109413)
            intro = DynAccessor(109414)
            R239_ST_Molot = DynAccessor(109415)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(109416)
            Ch46_113_140 = DynAccessor(109417)
            G164_Kpz_Pr_68_P = DynAccessor(109418)
            Pl35_CS_57_Sokol = DynAccessor(109419)
            R121_KV4_KTT = DynAccessor(109420)
            S22_Strv_S1 = DynAccessor(109421)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(109422)
        option_2 = DynAccessor(109423)
        option_3 = DynAccessor(109424)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(109425)
        Ch57_BZT_70 = DynAccessor(109426)
        F134_ARL_Projet_F = DynAccessor(109427)
        G184_EisBaer = DynAccessor(109428)
        GB140_Champion = DynAccessor(109429)
        R124_Object_279 = DynAccessor(109430)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(109431)
        operation_10 = DynAccessor(109432)
        operation_8 = DynAccessor(109433)
        operation_9 = DynAccessor(109434)
        operation_99 = DynAccessor(109435)
        video_operations_person = DynAccessor(109436)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(109437)

    platoon = _platoon()

    class _startup(DynAccessor):
        __slots__ = ()
        c_1_43_showreel = DynAccessor(109438)

    startup = _startup()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(109439)

    vehicle = _vehicle()