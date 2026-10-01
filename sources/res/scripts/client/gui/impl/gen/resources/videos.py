from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(114050)
    _tutorialInitialLoop = DynAccessor(114051)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(114052)
        up_particles = DynAccessor(114053)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(114054)
            crewCommander = DynAccessor(114055)
            crewDriver = DynAccessor(114056)
            crewGunner = DynAccessor(114057)
            crewLoader = DynAccessor(114058)
            crewRadioOperator = DynAccessor(114059)
            skillAdrenalineRush = DynAccessor(114060)
            skillArmorer = DynAccessor(114061)
            skillArtLamp = DynAccessor(114062)
            skillBrothersInArms = DynAccessor(114063)
            skillCallForVengeance = DynAccessor(114064)
            skillClutchBraking = DynAccessor(114065)
            skillCommanderBonus = DynAccessor(114066)
            skillConcealment = DynAccessor(114067)
            skillControlledImpact = DynAccessor(114068)
            skillDeadEye = DynAccessor(114069)
            skillDesignatedTarget = DynAccessor(114070)
            skillEagleEye = DynAccessor(114071)
            skillExpert = DynAccessor(114072)
            skillFirefighting = DynAccessor(114073)
            skillIntuition = DynAccessor(114074)
            skillJackOfAllTrades = DynAccessor(114075)
            skillMentor = DynAccessor(114076)
            skillOffRoadDriving = DynAccessor(114077)
            skillPreventativeMaintenance = DynAccessor(114078)
            skillRelaying = DynAccessor(114079)
            skillRepairs = DynAccessor(114080)
            skillSafeStowage = DynAccessor(114081)
            skillSignalBoosting = DynAccessor(114082)
            skillSituationalAwareness = DynAccessor(114083)
            skillSixthSense = DynAccessor(114084)
            skillSmoothRide = DynAccessor(114085)
            skillSnapShot = DynAccessor(114086)
            skillSniper = DynAccessor(114087)
            skillSoundIntelligence = DynAccessor(114088)
            statConcealment = DynAccessor(114089)
            statFirepower = DynAccessor(114090)
            statMobility = DynAccessor(114091)
            statSpotting = DynAccessor(114092)
            statSurvivability = DynAccessor(114093)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(114094)
        ay_gun = DynAccessor(114095)
        ay_tracks = DynAccessor(114096)
        ay_turret = DynAccessor(114097)
        video_reward = DynAccessor(114098)
        video_reward_min = DynAccessor(114099)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmoTypeAvailable = DynAccessor(114100)
        AmmunitionCrit = DynAccessor(114101)
        FueltankCrit = DynAccessor(114102)
        InSafetyWhileNotObserved = DynAccessor(114103)
        KilledWhileObserved = DynAccessor(114104)
        ModuleDamage = DynAccessor(114105)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_211_0 = DynAccessor(114106)
        v_212_0 = DynAccessor(114107)
        v_213_0 = DynAccessor(114108)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(114109)
        Intro = DynAccessor(114110)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(114111)
            overcharge = DynAccessor(114112)
            power_shot = DynAccessor(114113)
            teleport = DynAccessor(114114)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(114115)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(114116)
        cosmic_intro_vp8_8_256 = DynAccessor(114117)
        cosmic_intro_vp8_8_96 = DynAccessor(114118)
        cosmic_intro_vp9_8_128 = DynAccessor(114119)
        cosmic_intro_vp9_8_256 = DynAccessor(114120)
        cosmic_intro_vp9_8_96 = DynAccessor(114121)
        example = DynAccessor(114122)
        example_2 = DynAccessor(114123)
        example_3 = DynAccessor(114124)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(114125)
        lootbox_prem = DynAccessor(114126)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(114127)
            gold = DynAccessor(114128)
            silver = DynAccessor(114129)
            standart = DynAccessor(114130)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(114131)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114132)
            small = DynAccessor(114133)

        bd2025 = _bd2025()

        class _bd2026(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114134)
            small = DynAccessor(114135)

        bd2026 = _bd2026()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114136)
            standart = DynAccessor(114137)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114138)
            standart = DynAccessor(114139)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114140)
            standart = DynAccessor(114141)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114142)
            standart = DynAccessor(114143)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(114144)
            mtl_1_35 = DynAccessor(114145)
            mtl_1_43 = DynAccessor(114146)
            mt_drops = DynAccessor(114147)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114148)
            medium = DynAccessor(114149)
            small = DynAccessor(114150)
            tanks_6 = DynAccessor(114151)
            tanks_7 = DynAccessor(114152)
            tanks_8 = DynAccessor(114153)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(114154)
            R149_Object_268_4_02 = DynAccessor(114155)
            R177_ISU_152K_BL10_02 = DynAccessor(114156)
            R248_T44_Storm = DynAccessor(114157)
            R45_IS_7_02 = DynAccessor(114158)
            Un24_Vz_68_2_Britva = DynAccessor(114159)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(114160)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(114161)
            intro = DynAccessor(114162)
            R239_ST_Molot_02 = DynAccessor(114163)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(114164)
            GB141_Celestial_2_51 = DynAccessor(114165)
            intro = DynAccessor(114166)
            R239_ST_Molot = DynAccessor(114167)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(114168)
            Ch46_113_140 = DynAccessor(114169)
            G164_Kpz_Pr_68_P = DynAccessor(114170)
            Pl35_CS_57_Sokol = DynAccessor(114171)
            R121_KV4_KTT = DynAccessor(114172)
            S22_Strv_S1 = DynAccessor(114173)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _mt_birthday(DynAccessor):
        __slots__ = ()

        class _tankMail(DynAccessor):
            __slots__ = ()
            sentGift = DynAccessor(114174)

        tankMail = _tankMail()

    mt_birthday = _mt_birthday()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(114175)
        option_2 = DynAccessor(114176)
        option_3 = DynAccessor(114177)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(114178)
        Ch57_BZT_70 = DynAccessor(114179)
        F134_ARL_Projet_F = DynAccessor(114180)
        G184_EisBaer = DynAccessor(114181)
        GB140_Champion = DynAccessor(114182)
        R124_Object_279 = DynAccessor(114183)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(114184)
        operation_10 = DynAccessor(114185)
        operation_8 = DynAccessor(114186)
        operation_9 = DynAccessor(114187)
        operation_99 = DynAccessor(114188)
        video_operations_person = DynAccessor(114189)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(114190)

    platoon = _platoon()

    class _startup(DynAccessor):
        __slots__ = ()
        c_1_45_showreel = DynAccessor(114191)

    startup = _startup()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(114192)

    vehicle = _vehicle()

    class _wt_event(DynAccessor):
        __slots__ = ()
        BOBR_v004 = DynAccessor(114193)
        boss_portal_idle = DynAccessor(114194)
        boss_portal_open = DynAccessor(114195)
        Czolg_P_Wz_46_3dst_Verbesserter_v004 = DynAccessor(114196)
        E_50_GT_Alkett_Prod_02_3d_style_v004 = DynAccessor(114197)
        E_50_GT_Alkett_Prod_v004 = DynAccessor(114198)
        hunter_portal_idle = DynAccessor(114199)
        hunter_portal_open = DynAccessor(114200)
        Main_video_1 = DynAccessor(114201)
        Projet_57_Ampere_v004 = DynAccessor(114202)
        TBT_v004 = DynAccessor(114203)
        wt_intro = DynAccessor(114204)
        wt_outro = DynAccessor(114205)
        ZZT_v004 = DynAccessor(114206)

        class _ability(DynAccessor):
            __slots__ = ()
            wt_ability_stunArea = DynAccessor(114207)
            wt_ability_stunAreaModA = DynAccessor(114208)
            wt_ability_unionStrength = DynAccessor(114209)
            wt_barrier = DynAccessor(114210)
            wt_charged_shot = DynAccessor(114211)
            wt_clone = DynAccessor(114212)
            wt_damage_shield = DynAccessor(114213)
            wt_decrease_reload_time = DynAccessor(114214)
            wt_dome = DynAccessor(114215)
            wt_explosive_damage_shield = DynAccessor(114216)
            wt_explosive_shot = DynAccessor(114217)
            wt_extractor_shot = DynAccessor(114218)
            wt_group_repair = DynAccessor(114219)
            wt_hyperion_mod_a = DynAccessor(114220)
            wt_hyperion_mod_b = DynAccessor(114221)
            wt_impulse_mod_a = DynAccessor(114222)
            wt_increase_damage = DynAccessor(114223)
            wt_invisibility_mod_a = DynAccessor(114224)
            wt_invisibility_mod_b = DynAccessor(114225)
            wt_missile = DynAccessor(114226)
            wt_nitro = DynAccessor(114227)
            wt_passive_heal = DynAccessor(114228)
            wt_plasma_retention = DynAccessor(114229)
            wt_smoke_screen = DynAccessor(114230)
            wt_teleport_mod_a = DynAccessor(114231)
            wt_teleport_mod_b = DynAccessor(114232)
            wt_vampirism = DynAccessor(114233)

        ability = _ability()

    wt_event = _wt_event()