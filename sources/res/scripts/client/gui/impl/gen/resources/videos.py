from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(114041)
    _tutorialInitialLoop = DynAccessor(114042)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(114043)
        up_particles = DynAccessor(114044)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(114045)
            crewCommander = DynAccessor(114046)
            crewDriver = DynAccessor(114047)
            crewGunner = DynAccessor(114048)
            crewLoader = DynAccessor(114049)
            crewRadioOperator = DynAccessor(114050)
            skillAdrenalineRush = DynAccessor(114051)
            skillArmorer = DynAccessor(114052)
            skillArtLamp = DynAccessor(114053)
            skillBrothersInArms = DynAccessor(114054)
            skillCallForVengeance = DynAccessor(114055)
            skillClutchBraking = DynAccessor(114056)
            skillCommanderBonus = DynAccessor(114057)
            skillConcealment = DynAccessor(114058)
            skillControlledImpact = DynAccessor(114059)
            skillDeadEye = DynAccessor(114060)
            skillDesignatedTarget = DynAccessor(114061)
            skillEagleEye = DynAccessor(114062)
            skillExpert = DynAccessor(114063)
            skillFirefighting = DynAccessor(114064)
            skillIntuition = DynAccessor(114065)
            skillJackOfAllTrades = DynAccessor(114066)
            skillMentor = DynAccessor(114067)
            skillOffRoadDriving = DynAccessor(114068)
            skillPreventativeMaintenance = DynAccessor(114069)
            skillRelaying = DynAccessor(114070)
            skillRepairs = DynAccessor(114071)
            skillSafeStowage = DynAccessor(114072)
            skillSignalBoosting = DynAccessor(114073)
            skillSituationalAwareness = DynAccessor(114074)
            skillSixthSense = DynAccessor(114075)
            skillSmoothRide = DynAccessor(114076)
            skillSnapShot = DynAccessor(114077)
            skillSniper = DynAccessor(114078)
            skillSoundIntelligence = DynAccessor(114079)
            statConcealment = DynAccessor(114080)
            statFirepower = DynAccessor(114081)
            statMobility = DynAccessor(114082)
            statSpotting = DynAccessor(114083)
            statSurvivability = DynAccessor(114084)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(114085)
        ay_gun = DynAccessor(114086)
        ay_tracks = DynAccessor(114087)
        ay_turret = DynAccessor(114088)
        video_reward = DynAccessor(114089)
        video_reward_min = DynAccessor(114090)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmoTypeAvailable = DynAccessor(114091)
        AmmunitionCrit = DynAccessor(114092)
        FueltankCrit = DynAccessor(114093)
        InSafetyWhileNotObserved = DynAccessor(114094)
        KilledWhileObserved = DynAccessor(114095)
        ModuleDamage = DynAccessor(114096)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_211_0 = DynAccessor(114097)
        v_212_0 = DynAccessor(114098)
        v_213_0 = DynAccessor(114099)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(114100)
        Intro = DynAccessor(114101)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(114102)
            overcharge = DynAccessor(114103)
            power_shot = DynAccessor(114104)
            teleport = DynAccessor(114105)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(114106)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(114107)
        cosmic_intro_vp8_8_256 = DynAccessor(114108)
        cosmic_intro_vp8_8_96 = DynAccessor(114109)
        cosmic_intro_vp9_8_128 = DynAccessor(114110)
        cosmic_intro_vp9_8_256 = DynAccessor(114111)
        cosmic_intro_vp9_8_96 = DynAccessor(114112)
        example = DynAccessor(114113)
        example_2 = DynAccessor(114114)
        example_3 = DynAccessor(114115)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(114116)
        lootbox_prem = DynAccessor(114117)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(114118)
            gold = DynAccessor(114119)
            silver = DynAccessor(114120)
            standart = DynAccessor(114121)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(114122)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114123)
            small = DynAccessor(114124)

        bd2025 = _bd2025()

        class _bd2026(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114125)
            small = DynAccessor(114126)

        bd2026 = _bd2026()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114127)
            standart = DynAccessor(114128)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114129)
            standart = DynAccessor(114130)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114131)
            standart = DynAccessor(114132)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114133)
            standart = DynAccessor(114134)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(114135)
            mtl_1_35 = DynAccessor(114136)
            mtl_1_43 = DynAccessor(114137)
            mt_drops = DynAccessor(114138)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114139)
            medium = DynAccessor(114140)
            small = DynAccessor(114141)
            tanks_6 = DynAccessor(114142)
            tanks_7 = DynAccessor(114143)
            tanks_8 = DynAccessor(114144)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(114145)
            R149_Object_268_4_02 = DynAccessor(114146)
            R177_ISU_152K_BL10_02 = DynAccessor(114147)
            R248_T44_Storm = DynAccessor(114148)
            R45_IS_7_02 = DynAccessor(114149)
            Un24_Vz_68_2_Britva = DynAccessor(114150)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(114151)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(114152)
            intro = DynAccessor(114153)
            R239_ST_Molot_02 = DynAccessor(114154)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(114155)
            GB141_Celestial_2_51 = DynAccessor(114156)
            intro = DynAccessor(114157)
            R239_ST_Molot = DynAccessor(114158)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(114159)
            Ch46_113_140 = DynAccessor(114160)
            G164_Kpz_Pr_68_P = DynAccessor(114161)
            Pl35_CS_57_Sokol = DynAccessor(114162)
            R121_KV4_KTT = DynAccessor(114163)
            S22_Strv_S1 = DynAccessor(114164)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _mt_birthday(DynAccessor):
        __slots__ = ()

        class _tankMail(DynAccessor):
            __slots__ = ()
            sentGift = DynAccessor(114165)

        tankMail = _tankMail()

    mt_birthday = _mt_birthday()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(114166)
        option_2 = DynAccessor(114167)
        option_3 = DynAccessor(114168)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(114169)
        Ch57_BZT_70 = DynAccessor(114170)
        F134_ARL_Projet_F = DynAccessor(114171)
        G184_EisBaer = DynAccessor(114172)
        GB140_Champion = DynAccessor(114173)
        R124_Object_279 = DynAccessor(114174)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(114175)
        operation_10 = DynAccessor(114176)
        operation_8 = DynAccessor(114177)
        operation_9 = DynAccessor(114178)
        operation_99 = DynAccessor(114179)
        video_operations_person = DynAccessor(114180)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(114181)

    platoon = _platoon()

    class _startup(DynAccessor):
        __slots__ = ()
        c_1_45_showreel = DynAccessor(114182)

    startup = _startup()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(114183)

    vehicle = _vehicle()

    class _wt_event(DynAccessor):
        __slots__ = ()
        BOBR_v004 = DynAccessor(114184)
        boss_portal_idle = DynAccessor(114185)
        boss_portal_open = DynAccessor(114186)
        Czolg_P_Wz_46_3dst_Verbesserter_v004 = DynAccessor(114187)
        E_50_GT_Alkett_Prod_02_3d_style_v004 = DynAccessor(114188)
        E_50_GT_Alkett_Prod_v004 = DynAccessor(114189)
        hunter_portal_idle = DynAccessor(114190)
        hunter_portal_open = DynAccessor(114191)
        Main_video_1 = DynAccessor(114192)
        Projet_57_Ampere_v004 = DynAccessor(114193)
        TBT_v004 = DynAccessor(114194)
        wt_intro = DynAccessor(114195)
        wt_outro = DynAccessor(114196)
        ZZT_v004 = DynAccessor(114197)

        class _ability(DynAccessor):
            __slots__ = ()
            wt_ability_stunArea = DynAccessor(114198)
            wt_ability_stunAreaModA = DynAccessor(114199)
            wt_ability_unionStrength = DynAccessor(114200)
            wt_barrier = DynAccessor(114201)
            wt_charged_shot = DynAccessor(114202)
            wt_clone = DynAccessor(114203)
            wt_damage_shield = DynAccessor(114204)
            wt_decrease_reload_time = DynAccessor(114205)
            wt_dome = DynAccessor(114206)
            wt_explosive_damage_shield = DynAccessor(114207)
            wt_explosive_shot = DynAccessor(114208)
            wt_extractor_shot = DynAccessor(114209)
            wt_group_repair = DynAccessor(114210)
            wt_hyperion_mod_a = DynAccessor(114211)
            wt_hyperion_mod_b = DynAccessor(114212)
            wt_impulse_mod_a = DynAccessor(114213)
            wt_increase_damage = DynAccessor(114214)
            wt_invisibility_mod_a = DynAccessor(114215)
            wt_invisibility_mod_b = DynAccessor(114216)
            wt_missile = DynAccessor(114217)
            wt_nitro = DynAccessor(114218)
            wt_passive_heal = DynAccessor(114219)
            wt_plasma_retention = DynAccessor(114220)
            wt_smoke_screen = DynAccessor(114221)
            wt_teleport_mod_a = DynAccessor(114222)
            wt_teleport_mod_b = DynAccessor(114223)
            wt_vampirism = DynAccessor(114224)

        ability = _ability()

    wt_event = _wt_event()