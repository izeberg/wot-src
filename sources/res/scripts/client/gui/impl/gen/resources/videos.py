from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(114013)
    _tutorialInitialLoop = DynAccessor(114014)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(114015)
        up_particles = DynAccessor(114016)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(114017)
            crewCommander = DynAccessor(114018)
            crewDriver = DynAccessor(114019)
            crewGunner = DynAccessor(114020)
            crewLoader = DynAccessor(114021)
            crewRadioOperator = DynAccessor(114022)
            skillAdrenalineRush = DynAccessor(114023)
            skillArmorer = DynAccessor(114024)
            skillArtLamp = DynAccessor(114025)
            skillBrothersInArms = DynAccessor(114026)
            skillCallForVengeance = DynAccessor(114027)
            skillClutchBraking = DynAccessor(114028)
            skillCommanderBonus = DynAccessor(114029)
            skillConcealment = DynAccessor(114030)
            skillControlledImpact = DynAccessor(114031)
            skillDeadEye = DynAccessor(114032)
            skillDesignatedTarget = DynAccessor(114033)
            skillEagleEye = DynAccessor(114034)
            skillExpert = DynAccessor(114035)
            skillFirefighting = DynAccessor(114036)
            skillIntuition = DynAccessor(114037)
            skillJackOfAllTrades = DynAccessor(114038)
            skillMentor = DynAccessor(114039)
            skillOffRoadDriving = DynAccessor(114040)
            skillPreventativeMaintenance = DynAccessor(114041)
            skillRelaying = DynAccessor(114042)
            skillRepairs = DynAccessor(114043)
            skillSafeStowage = DynAccessor(114044)
            skillSignalBoosting = DynAccessor(114045)
            skillSituationalAwareness = DynAccessor(114046)
            skillSixthSense = DynAccessor(114047)
            skillSmoothRide = DynAccessor(114048)
            skillSnapShot = DynAccessor(114049)
            skillSniper = DynAccessor(114050)
            skillSoundIntelligence = DynAccessor(114051)
            statConcealment = DynAccessor(114052)
            statFirepower = DynAccessor(114053)
            statMobility = DynAccessor(114054)
            statSpotting = DynAccessor(114055)
            statSurvivability = DynAccessor(114056)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(114057)
        ay_gun = DynAccessor(114058)
        ay_tracks = DynAccessor(114059)
        ay_turret = DynAccessor(114060)
        video_reward = DynAccessor(114061)
        video_reward_min = DynAccessor(114062)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmoTypeAvailable = DynAccessor(114063)
        AmmunitionCrit = DynAccessor(114064)
        FueltankCrit = DynAccessor(114065)
        InSafetyWhileNotObserved = DynAccessor(114066)
        KilledWhileObserved = DynAccessor(114067)
        ModuleDamage = DynAccessor(114068)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_211_0 = DynAccessor(114069)
        v_212_0 = DynAccessor(114070)
        v_213_0 = DynAccessor(114071)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(114072)
        Intro = DynAccessor(114073)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(114074)
            overcharge = DynAccessor(114075)
            power_shot = DynAccessor(114076)
            teleport = DynAccessor(114077)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(114078)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(114079)
        cosmic_intro_vp8_8_256 = DynAccessor(114080)
        cosmic_intro_vp8_8_96 = DynAccessor(114081)
        cosmic_intro_vp9_8_128 = DynAccessor(114082)
        cosmic_intro_vp9_8_256 = DynAccessor(114083)
        cosmic_intro_vp9_8_96 = DynAccessor(114084)
        example = DynAccessor(114085)
        example_2 = DynAccessor(114086)
        example_3 = DynAccessor(114087)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(114088)
        lootbox_prem = DynAccessor(114089)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(114090)
            gold = DynAccessor(114091)
            silver = DynAccessor(114092)
            standart = DynAccessor(114093)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(114094)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114095)
            small = DynAccessor(114096)

        bd2025 = _bd2025()

        class _bd2026(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114097)
            small = DynAccessor(114098)

        bd2026 = _bd2026()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114099)
            standart = DynAccessor(114100)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114101)
            standart = DynAccessor(114102)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114103)
            standart = DynAccessor(114104)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114105)
            standart = DynAccessor(114106)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(114107)
            mtl_1_35 = DynAccessor(114108)
            mtl_1_43 = DynAccessor(114109)
            mt_drops = DynAccessor(114110)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114111)
            medium = DynAccessor(114112)
            small = DynAccessor(114113)
            tanks_6 = DynAccessor(114114)
            tanks_7 = DynAccessor(114115)
            tanks_8 = DynAccessor(114116)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(114117)
            R149_Object_268_4_02 = DynAccessor(114118)
            R177_ISU_152K_BL10_02 = DynAccessor(114119)
            R248_T44_Storm = DynAccessor(114120)
            R45_IS_7_02 = DynAccessor(114121)
            Un24_Vz_68_2_Britva = DynAccessor(114122)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(114123)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(114124)
            intro = DynAccessor(114125)
            R239_ST_Molot_02 = DynAccessor(114126)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(114127)
            GB141_Celestial_2_51 = DynAccessor(114128)
            intro = DynAccessor(114129)
            R239_ST_Molot = DynAccessor(114130)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(114131)
            Ch46_113_140 = DynAccessor(114132)
            G164_Kpz_Pr_68_P = DynAccessor(114133)
            Pl35_CS_57_Sokol = DynAccessor(114134)
            R121_KV4_KTT = DynAccessor(114135)
            S22_Strv_S1 = DynAccessor(114136)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _mt_birthday(DynAccessor):
        __slots__ = ()

        class _tankMail(DynAccessor):
            __slots__ = ()
            sentGift = DynAccessor(114137)

        tankMail = _tankMail()

    mt_birthday = _mt_birthday()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(114138)
        option_2 = DynAccessor(114139)
        option_3 = DynAccessor(114140)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(114141)
        Ch57_BZT_70 = DynAccessor(114142)
        F134_ARL_Projet_F = DynAccessor(114143)
        G184_EisBaer = DynAccessor(114144)
        GB140_Champion = DynAccessor(114145)
        R124_Object_279 = DynAccessor(114146)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(114147)
        operation_10 = DynAccessor(114148)
        operation_8 = DynAccessor(114149)
        operation_9 = DynAccessor(114150)
        operation_99 = DynAccessor(114151)
        video_operations_person = DynAccessor(114152)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(114153)

    platoon = _platoon()

    class _startup(DynAccessor):
        __slots__ = ()
        c_1_45_showreel = DynAccessor(114154)

    startup = _startup()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(114155)

    vehicle = _vehicle()

    class _wt_event(DynAccessor):
        __slots__ = ()
        BOBR_v004 = DynAccessor(114156)
        boss_portal_idle = DynAccessor(114157)
        boss_portal_open = DynAccessor(114158)
        Czolg_P_Wz_46_3dst_Verbesserter_v004 = DynAccessor(114159)
        E_50_GT_Alkett_Prod_02_3d_style_v004 = DynAccessor(114160)
        E_50_GT_Alkett_Prod_v004 = DynAccessor(114161)
        hunter_portal_idle = DynAccessor(114162)
        hunter_portal_open = DynAccessor(114163)
        Main_video_1 = DynAccessor(114164)
        Projet_57_Ampere_v004 = DynAccessor(114165)
        TBT_v004 = DynAccessor(114166)
        wt_intro = DynAccessor(114167)
        wt_outro = DynAccessor(114168)
        ZZT_v004 = DynAccessor(114169)

        class _ability(DynAccessor):
            __slots__ = ()
            wt_ability_stunArea = DynAccessor(114170)
            wt_ability_stunAreaModA = DynAccessor(114171)
            wt_ability_unionStrength = DynAccessor(114172)
            wt_barrier = DynAccessor(114173)
            wt_charged_shot = DynAccessor(114174)
            wt_clone = DynAccessor(114175)
            wt_damage_shield = DynAccessor(114176)
            wt_decrease_reload_time = DynAccessor(114177)
            wt_dome = DynAccessor(114178)
            wt_explosive_damage_shield = DynAccessor(114179)
            wt_explosive_shot = DynAccessor(114180)
            wt_extractor_shot = DynAccessor(114181)
            wt_group_repair = DynAccessor(114182)
            wt_hyperion_mod_a = DynAccessor(114183)
            wt_hyperion_mod_b = DynAccessor(114184)
            wt_impulse_mod_a = DynAccessor(114185)
            wt_increase_damage = DynAccessor(114186)
            wt_invisibility_mod_a = DynAccessor(114187)
            wt_invisibility_mod_b = DynAccessor(114188)
            wt_missile = DynAccessor(114189)
            wt_nitro = DynAccessor(114190)
            wt_passive_heal = DynAccessor(114191)
            wt_plasma_retention = DynAccessor(114192)
            wt_smoke_screen = DynAccessor(114193)
            wt_teleport_mod_a = DynAccessor(114194)
            wt_teleport_mod_b = DynAccessor(114195)
            wt_vampirism = DynAccessor(114196)

        ability = _ability()

    wt_event = _wt_event()