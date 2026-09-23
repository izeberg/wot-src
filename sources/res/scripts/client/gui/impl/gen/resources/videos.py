from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(114010)
    _tutorialInitialLoop = DynAccessor(114011)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(114012)
        up_particles = DynAccessor(114013)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(114014)
            crewCommander = DynAccessor(114015)
            crewDriver = DynAccessor(114016)
            crewGunner = DynAccessor(114017)
            crewLoader = DynAccessor(114018)
            crewRadioOperator = DynAccessor(114019)
            skillAdrenalineRush = DynAccessor(114020)
            skillArmorer = DynAccessor(114021)
            skillArtLamp = DynAccessor(114022)
            skillBrothersInArms = DynAccessor(114023)
            skillCallForVengeance = DynAccessor(114024)
            skillClutchBraking = DynAccessor(114025)
            skillCommanderBonus = DynAccessor(114026)
            skillConcealment = DynAccessor(114027)
            skillControlledImpact = DynAccessor(114028)
            skillDeadEye = DynAccessor(114029)
            skillDesignatedTarget = DynAccessor(114030)
            skillEagleEye = DynAccessor(114031)
            skillExpert = DynAccessor(114032)
            skillFirefighting = DynAccessor(114033)
            skillIntuition = DynAccessor(114034)
            skillJackOfAllTrades = DynAccessor(114035)
            skillMentor = DynAccessor(114036)
            skillOffRoadDriving = DynAccessor(114037)
            skillPreventativeMaintenance = DynAccessor(114038)
            skillRelaying = DynAccessor(114039)
            skillRepairs = DynAccessor(114040)
            skillSafeStowage = DynAccessor(114041)
            skillSignalBoosting = DynAccessor(114042)
            skillSituationalAwareness = DynAccessor(114043)
            skillSixthSense = DynAccessor(114044)
            skillSmoothRide = DynAccessor(114045)
            skillSnapShot = DynAccessor(114046)
            skillSniper = DynAccessor(114047)
            skillSoundIntelligence = DynAccessor(114048)
            statConcealment = DynAccessor(114049)
            statFirepower = DynAccessor(114050)
            statMobility = DynAccessor(114051)
            statSpotting = DynAccessor(114052)
            statSurvivability = DynAccessor(114053)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(114054)
        ay_gun = DynAccessor(114055)
        ay_tracks = DynAccessor(114056)
        ay_turret = DynAccessor(114057)
        video_reward = DynAccessor(114058)
        video_reward_min = DynAccessor(114059)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmoTypeAvailable = DynAccessor(114060)
        AmmunitionCrit = DynAccessor(114061)
        FueltankCrit = DynAccessor(114062)
        InSafetyWhileNotObserved = DynAccessor(114063)
        KilledWhileObserved = DynAccessor(114064)
        ModuleDamage = DynAccessor(114065)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_211_0 = DynAccessor(114066)
        v_212_0 = DynAccessor(114067)
        v_213_0 = DynAccessor(114068)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(114069)
        Intro = DynAccessor(114070)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(114071)
            overcharge = DynAccessor(114072)
            power_shot = DynAccessor(114073)
            teleport = DynAccessor(114074)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(114075)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(114076)
        cosmic_intro_vp8_8_256 = DynAccessor(114077)
        cosmic_intro_vp8_8_96 = DynAccessor(114078)
        cosmic_intro_vp9_8_128 = DynAccessor(114079)
        cosmic_intro_vp9_8_256 = DynAccessor(114080)
        cosmic_intro_vp9_8_96 = DynAccessor(114081)
        example = DynAccessor(114082)
        example_2 = DynAccessor(114083)
        example_3 = DynAccessor(114084)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(114085)
        lootbox_prem = DynAccessor(114086)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(114087)
            gold = DynAccessor(114088)
            silver = DynAccessor(114089)
            standart = DynAccessor(114090)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(114091)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114092)
            small = DynAccessor(114093)

        bd2025 = _bd2025()

        class _bd2026(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114094)
            small = DynAccessor(114095)

        bd2026 = _bd2026()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114096)
            standart = DynAccessor(114097)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114098)
            standart = DynAccessor(114099)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114100)
            standart = DynAccessor(114101)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114102)
            standart = DynAccessor(114103)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(114104)
            mtl_1_35 = DynAccessor(114105)
            mtl_1_43 = DynAccessor(114106)
            mt_drops = DynAccessor(114107)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114108)
            medium = DynAccessor(114109)
            small = DynAccessor(114110)
            tanks_6 = DynAccessor(114111)
            tanks_7 = DynAccessor(114112)
            tanks_8 = DynAccessor(114113)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(114114)
            R149_Object_268_4_02 = DynAccessor(114115)
            R177_ISU_152K_BL10_02 = DynAccessor(114116)
            R248_T44_Storm = DynAccessor(114117)
            R45_IS_7_02 = DynAccessor(114118)
            Un24_Vz_68_2_Britva = DynAccessor(114119)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(114120)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(114121)
            intro = DynAccessor(114122)
            R239_ST_Molot_02 = DynAccessor(114123)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(114124)
            GB141_Celestial_2_51 = DynAccessor(114125)
            intro = DynAccessor(114126)
            R239_ST_Molot = DynAccessor(114127)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(114128)
            Ch46_113_140 = DynAccessor(114129)
            G164_Kpz_Pr_68_P = DynAccessor(114130)
            Pl35_CS_57_Sokol = DynAccessor(114131)
            R121_KV4_KTT = DynAccessor(114132)
            S22_Strv_S1 = DynAccessor(114133)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _mt_birthday(DynAccessor):
        __slots__ = ()

        class _tankMail(DynAccessor):
            __slots__ = ()
            sentGift = DynAccessor(114134)

        tankMail = _tankMail()

    mt_birthday = _mt_birthday()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(114135)
        option_2 = DynAccessor(114136)
        option_3 = DynAccessor(114137)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(114138)
        Ch57_BZT_70 = DynAccessor(114139)
        F134_ARL_Projet_F = DynAccessor(114140)
        G184_EisBaer = DynAccessor(114141)
        GB140_Champion = DynAccessor(114142)
        R124_Object_279 = DynAccessor(114143)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(114144)
        operation_10 = DynAccessor(114145)
        operation_8 = DynAccessor(114146)
        operation_9 = DynAccessor(114147)
        operation_99 = DynAccessor(114148)
        video_operations_person = DynAccessor(114149)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(114150)

    platoon = _platoon()

    class _startup(DynAccessor):
        __slots__ = ()
        c_1_45_showreel = DynAccessor(114151)

    startup = _startup()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(114152)

    vehicle = _vehicle()

    class _wt_event(DynAccessor):
        __slots__ = ()
        BOBR_v004 = DynAccessor(114153)
        boss_portal_idle = DynAccessor(114154)
        boss_portal_open = DynAccessor(114155)
        Czolg_P_Wz_46_3dst_Verbesserter_v004 = DynAccessor(114156)
        E_50_GT_Alkett_Prod_02_3d_style_v004 = DynAccessor(114157)
        E_50_GT_Alkett_Prod_v004 = DynAccessor(114158)
        hunter_portal_idle = DynAccessor(114159)
        hunter_portal_open = DynAccessor(114160)
        Main_video_1 = DynAccessor(114161)
        Projet_57_Ampere_v004 = DynAccessor(114162)
        TBT_v004 = DynAccessor(114163)
        wt_intro = DynAccessor(114164)
        wt_outro = DynAccessor(114165)
        ZZT_v004 = DynAccessor(114166)

        class _ability(DynAccessor):
            __slots__ = ()
            wt_ability_stunArea = DynAccessor(114167)
            wt_ability_stunAreaModA = DynAccessor(114168)
            wt_ability_unionStrength = DynAccessor(114169)
            wt_barrier = DynAccessor(114170)
            wt_charged_shot = DynAccessor(114171)
            wt_clone = DynAccessor(114172)
            wt_damage_shield = DynAccessor(114173)
            wt_decrease_reload_time = DynAccessor(114174)
            wt_dome = DynAccessor(114175)
            wt_explosive_damage_shield = DynAccessor(114176)
            wt_explosive_shot = DynAccessor(114177)
            wt_extractor_shot = DynAccessor(114178)
            wt_group_repair = DynAccessor(114179)
            wt_hyperion_mod_a = DynAccessor(114180)
            wt_hyperion_mod_b = DynAccessor(114181)
            wt_impulse_mod_a = DynAccessor(114182)
            wt_increase_damage = DynAccessor(114183)
            wt_invisibility_mod_a = DynAccessor(114184)
            wt_invisibility_mod_b = DynAccessor(114185)
            wt_missile = DynAccessor(114186)
            wt_nitro = DynAccessor(114187)
            wt_passive_heal = DynAccessor(114188)
            wt_plasma_retention = DynAccessor(114189)
            wt_smoke_screen = DynAccessor(114190)
            wt_teleport_mod_a = DynAccessor(114191)
            wt_teleport_mod_b = DynAccessor(114192)
            wt_vampirism = DynAccessor(114193)

        ability = _ability()

    wt_event = _wt_event()