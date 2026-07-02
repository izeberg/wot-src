from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(110390)
    _tutorialInitialLoop = DynAccessor(110391)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(110392)
        up_particles = DynAccessor(110393)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(110394)
            crewCommander = DynAccessor(110395)
            crewDriver = DynAccessor(110396)
            crewGunner = DynAccessor(110397)
            crewLoader = DynAccessor(110398)
            crewRadioOperator = DynAccessor(110399)
            skillAdrenalineRush = DynAccessor(110400)
            skillArmorer = DynAccessor(110401)
            skillArtLamp = DynAccessor(110402)
            skillBrothersInArms = DynAccessor(110403)
            skillCallForVengeance = DynAccessor(110404)
            skillClutchBraking = DynAccessor(110405)
            skillCommanderBonus = DynAccessor(110406)
            skillConcealment = DynAccessor(110407)
            skillControlledImpact = DynAccessor(110408)
            skillDeadEye = DynAccessor(110409)
            skillDesignatedTarget = DynAccessor(110410)
            skillEagleEye = DynAccessor(110411)
            skillExpert = DynAccessor(110412)
            skillFirefighting = DynAccessor(110413)
            skillIntuition = DynAccessor(110414)
            skillJackOfAllTrades = DynAccessor(110415)
            skillMentor = DynAccessor(110416)
            skillOffRoadDriving = DynAccessor(110417)
            skillPreventativeMaintenance = DynAccessor(110418)
            skillRelaying = DynAccessor(110419)
            skillRepairs = DynAccessor(110420)
            skillSafeStowage = DynAccessor(110421)
            skillSignalBoosting = DynAccessor(110422)
            skillSituationalAwareness = DynAccessor(110423)
            skillSixthSense = DynAccessor(110424)
            skillSmoothRide = DynAccessor(110425)
            skillSnapShot = DynAccessor(110426)
            skillSniper = DynAccessor(110427)
            skillSoundIntelligence = DynAccessor(110428)
            statConcealment = DynAccessor(110429)
            statFirepower = DynAccessor(110430)
            statMobility = DynAccessor(110431)
            statSpotting = DynAccessor(110432)
            statSurvivability = DynAccessor(110433)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(110434)
        ay_gun = DynAccessor(110435)
        ay_tracks = DynAccessor(110436)
        ay_turret = DynAccessor(110437)
        video_reward = DynAccessor(110438)
        video_reward_min = DynAccessor(110439)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmunitionCrit = DynAccessor(110440)
        FueltankCrit = DynAccessor(110441)
        InSafetyWhileNotObserved = DynAccessor(110442)
        KilledWhileObserved = DynAccessor(110443)
        ModuleDamage = DynAccessor(110444)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_201_0 = DynAccessor(110445)
        v_202_0 = DynAccessor(110446)
        v_203_0 = DynAccessor(110447)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(110448)
        Intro = DynAccessor(110449)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(110450)
            overcharge = DynAccessor(110451)
            power_shot = DynAccessor(110452)
            teleport = DynAccessor(110453)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(110454)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(110455)
        cosmic_intro_vp8_8_256 = DynAccessor(110456)
        cosmic_intro_vp8_8_96 = DynAccessor(110457)
        cosmic_intro_vp9_8_128 = DynAccessor(110458)
        cosmic_intro_vp9_8_256 = DynAccessor(110459)
        cosmic_intro_vp9_8_96 = DynAccessor(110460)
        example = DynAccessor(110461)
        example_2 = DynAccessor(110462)
        example_3 = DynAccessor(110463)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(110464)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(110465)
            gold = DynAccessor(110466)
            silver = DynAccessor(110467)
            standart = DynAccessor(110468)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(110469)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(110470)
            small = DynAccessor(110471)

        bd2025 = _bd2025()

        class _bd2026(DynAccessor):
            __slots__ = ()
            large = DynAccessor(110472)
            small = DynAccessor(110473)

        bd2026 = _bd2026()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(110474)
            standart = DynAccessor(110475)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(110476)
            standart = DynAccessor(110477)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(110478)
            standart = DynAccessor(110479)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(110480)
            standart = DynAccessor(110481)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(110482)
            mtl_1_35 = DynAccessor(110483)
            mtl_1_43 = DynAccessor(110484)
            mt_drops = DynAccessor(110485)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(110486)
            medium = DynAccessor(110487)
            small = DynAccessor(110488)
            tanks_6 = DynAccessor(110489)
            tanks_7 = DynAccessor(110490)
            tanks_8 = DynAccessor(110491)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(110492)
            R149_Object_268_4_02 = DynAccessor(110493)
            R177_ISU_152K_BL10_02 = DynAccessor(110494)
            R248_T44_Storm = DynAccessor(110495)
            R45_IS_7_02 = DynAccessor(110496)
            Un24_Vz_68_2_Britva = DynAccessor(110497)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(110498)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(110499)
            intro = DynAccessor(110500)
            R239_ST_Molot_02 = DynAccessor(110501)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(110502)
            GB141_Celestial_2_51 = DynAccessor(110503)
            intro = DynAccessor(110504)
            R239_ST_Molot = DynAccessor(110505)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(110506)
            Ch46_113_140 = DynAccessor(110507)
            G164_Kpz_Pr_68_P = DynAccessor(110508)
            Pl35_CS_57_Sokol = DynAccessor(110509)
            R121_KV4_KTT = DynAccessor(110510)
            S22_Strv_S1 = DynAccessor(110511)

        mtl_universal = _mtl_universal()

        class _tanks_birthday_2026(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(110512)
            A124_T54E2 = DynAccessor(110513)
            A149_AMBT = DynAccessor(110514)
            Ch43_WZ_122_2 = DynAccessor(110515)
            F130_AMX_Tracteur_D = DynAccessor(110516)
            G168_KJpz_T_III = DynAccessor(110517)
            GB110_FV4201_Chieftain_Prototype = DynAccessor(110518)
            GB112_Caliban = DynAccessor(110519)
            intro = DynAccessor(110520)
            It18_Progetto_C45_mod_71 = DynAccessor(110521)
            Pl19_CS_52_LIS = DynAccessor(110522)
            R188_Object_259A = DynAccessor(110523)
            R227_Object_407_MZ = DynAccessor(110524)

        tanks_birthday_2026 = _tanks_birthday_2026()

    lootbox_reward_video = _lootbox_reward_video()

    class _mt_birthday(DynAccessor):
        __slots__ = ()

        class _tankMail(DynAccessor):
            __slots__ = ()
            sentGift = DynAccessor(110525)

        tankMail = _tankMail()

    mt_birthday = _mt_birthday()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(110526)
        option_2 = DynAccessor(110527)
        option_3 = DynAccessor(110528)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(110529)
        Ch57_BZT_70 = DynAccessor(110530)
        F134_ARL_Projet_F = DynAccessor(110531)
        G184_EisBaer = DynAccessor(110532)
        GB140_Champion = DynAccessor(110533)
        R124_Object_279 = DynAccessor(110534)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(110535)
        operation_10 = DynAccessor(110536)
        operation_8 = DynAccessor(110537)
        operation_9 = DynAccessor(110538)
        operation_99 = DynAccessor(110539)
        video_operations_person = DynAccessor(110540)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(110541)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(110542)

    vehicle = _vehicle()