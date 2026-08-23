from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(113999)
    _tutorialInitialLoop = DynAccessor(114000)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(114001)
        up_particles = DynAccessor(114002)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(114003)
            crewCommander = DynAccessor(114004)
            crewDriver = DynAccessor(114005)
            crewGunner = DynAccessor(114006)
            crewLoader = DynAccessor(114007)
            crewRadioOperator = DynAccessor(114008)
            skillAdrenalineRush = DynAccessor(114009)
            skillArmorer = DynAccessor(114010)
            skillArtLamp = DynAccessor(114011)
            skillBrothersInArms = DynAccessor(114012)
            skillCallForVengeance = DynAccessor(114013)
            skillClutchBraking = DynAccessor(114014)
            skillCommanderBonus = DynAccessor(114015)
            skillConcealment = DynAccessor(114016)
            skillControlledImpact = DynAccessor(114017)
            skillDeadEye = DynAccessor(114018)
            skillDesignatedTarget = DynAccessor(114019)
            skillEagleEye = DynAccessor(114020)
            skillExpert = DynAccessor(114021)
            skillFirefighting = DynAccessor(114022)
            skillIntuition = DynAccessor(114023)
            skillJackOfAllTrades = DynAccessor(114024)
            skillMentor = DynAccessor(114025)
            skillOffRoadDriving = DynAccessor(114026)
            skillPreventativeMaintenance = DynAccessor(114027)
            skillRelaying = DynAccessor(114028)
            skillRepairs = DynAccessor(114029)
            skillSafeStowage = DynAccessor(114030)
            skillSignalBoosting = DynAccessor(114031)
            skillSituationalAwareness = DynAccessor(114032)
            skillSixthSense = DynAccessor(114033)
            skillSmoothRide = DynAccessor(114034)
            skillSnapShot = DynAccessor(114035)
            skillSniper = DynAccessor(114036)
            skillSoundIntelligence = DynAccessor(114037)
            statConcealment = DynAccessor(114038)
            statFirepower = DynAccessor(114039)
            statMobility = DynAccessor(114040)
            statSpotting = DynAccessor(114041)
            statSurvivability = DynAccessor(114042)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(114043)
        ay_gun = DynAccessor(114044)
        ay_tracks = DynAccessor(114045)
        ay_turret = DynAccessor(114046)
        video_reward = DynAccessor(114047)
        video_reward_min = DynAccessor(114048)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmoTypeAvailable = DynAccessor(114049)
        AmmunitionCrit = DynAccessor(114050)
        FueltankCrit = DynAccessor(114051)
        InSafetyWhileNotObserved = DynAccessor(114052)
        KilledWhileObserved = DynAccessor(114053)
        ModuleDamage = DynAccessor(114054)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_211_0 = DynAccessor(114055)
        v_212_0 = DynAccessor(114056)
        v_213_0 = DynAccessor(114057)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(114058)
        Intro = DynAccessor(114059)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(114060)
            overcharge = DynAccessor(114061)
            power_shot = DynAccessor(114062)
            teleport = DynAccessor(114063)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(114064)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(114065)
        cosmic_intro_vp8_8_256 = DynAccessor(114066)
        cosmic_intro_vp8_8_96 = DynAccessor(114067)
        cosmic_intro_vp9_8_128 = DynAccessor(114068)
        cosmic_intro_vp9_8_256 = DynAccessor(114069)
        cosmic_intro_vp9_8_96 = DynAccessor(114070)
        example = DynAccessor(114071)
        example_2 = DynAccessor(114072)
        example_3 = DynAccessor(114073)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(114074)
        lootbox_prem = DynAccessor(114075)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(114076)
            gold = DynAccessor(114077)
            silver = DynAccessor(114078)
            standart = DynAccessor(114079)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(114080)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114081)
            small = DynAccessor(114082)

        bd2025 = _bd2025()

        class _bd2026(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114083)
            small = DynAccessor(114084)

        bd2026 = _bd2026()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114085)
            standart = DynAccessor(114086)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114087)
            standart = DynAccessor(114088)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114089)
            standart = DynAccessor(114090)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(114091)
            standart = DynAccessor(114092)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(114093)
            mtl_1_35 = DynAccessor(114094)
            mtl_1_43 = DynAccessor(114095)
            mt_drops = DynAccessor(114096)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(114097)
            medium = DynAccessor(114098)
            small = DynAccessor(114099)
            tanks_6 = DynAccessor(114100)
            tanks_7 = DynAccessor(114101)
            tanks_8 = DynAccessor(114102)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(114103)
            R149_Object_268_4_02 = DynAccessor(114104)
            R177_ISU_152K_BL10_02 = DynAccessor(114105)
            R248_T44_Storm = DynAccessor(114106)
            R45_IS_7_02 = DynAccessor(114107)
            Un24_Vz_68_2_Britva = DynAccessor(114108)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(114109)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(114110)
            intro = DynAccessor(114111)
            R239_ST_Molot_02 = DynAccessor(114112)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(114113)
            GB141_Celestial_2_51 = DynAccessor(114114)
            intro = DynAccessor(114115)
            R239_ST_Molot = DynAccessor(114116)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(114117)
            Ch46_113_140 = DynAccessor(114118)
            G164_Kpz_Pr_68_P = DynAccessor(114119)
            Pl35_CS_57_Sokol = DynAccessor(114120)
            R121_KV4_KTT = DynAccessor(114121)
            S22_Strv_S1 = DynAccessor(114122)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _mt_birthday(DynAccessor):
        __slots__ = ()

        class _tankMail(DynAccessor):
            __slots__ = ()
            sentGift = DynAccessor(114123)

        tankMail = _tankMail()

    mt_birthday = _mt_birthday()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(114124)
        option_2 = DynAccessor(114125)
        option_3 = DynAccessor(114126)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(114127)
        Ch57_BZT_70 = DynAccessor(114128)
        F134_ARL_Projet_F = DynAccessor(114129)
        G184_EisBaer = DynAccessor(114130)
        GB140_Champion = DynAccessor(114131)
        R124_Object_279 = DynAccessor(114132)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(114133)
        operation_10 = DynAccessor(114134)
        operation_8 = DynAccessor(114135)
        operation_9 = DynAccessor(114136)
        operation_99 = DynAccessor(114137)
        video_operations_person = DynAccessor(114138)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(114139)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(114140)

    vehicle = _vehicle()

    class _wt_event(DynAccessor):
        __slots__ = ()
        boss_portal_idle = DynAccessor(114141)
        boss_portal_open = DynAccessor(114142)
        End_1 = DynAccessor(114143)
        End_2 = DynAccessor(114144)
        End_3 = DynAccessor(114145)
        End_4 = DynAccessor(114146)
        End_5 = DynAccessor(114147)
        End_6 = DynAccessor(114148)
        End_7 = DynAccessor(114149)
        hunter_portal_idle = DynAccessor(114150)
        hunter_portal_open = DynAccessor(114151)
        Intro = DynAccessor(114152)
        wt_intro = DynAccessor(114153)
        wt_outro = DynAccessor(114154)

        class _ability(DynAccessor):
            __slots__ = ()
            wt_ability_stunArea = DynAccessor(114155)
            wt_ability_stunAreaModA = DynAccessor(114156)
            wt_ability_unionStrength = DynAccessor(114157)
            wt_barrier = DynAccessor(114158)
            wt_charged_shot = DynAccessor(114159)
            wt_clone = DynAccessor(114160)
            wt_damage_shield = DynAccessor(114161)
            wt_decrease_reload_time = DynAccessor(114162)
            wt_dome = DynAccessor(114163)
            wt_explosive_damage_shield = DynAccessor(114164)
            wt_explosive_shot = DynAccessor(114165)
            wt_extractor_shot = DynAccessor(114166)
            wt_group_repair = DynAccessor(114167)
            wt_hyperion_mod_a = DynAccessor(114168)
            wt_hyperion_mod_b = DynAccessor(114169)
            wt_impulse_mod_a = DynAccessor(114170)
            wt_increase_damage = DynAccessor(114171)
            wt_invisibility_mod_a = DynAccessor(114172)
            wt_invisibility_mod_b = DynAccessor(114173)
            wt_missile = DynAccessor(114174)
            wt_nitro = DynAccessor(114175)
            wt_passive_heal = DynAccessor(114176)
            wt_plasma_retention = DynAccessor(114177)
            wt_smoke_screen = DynAccessor(114178)
            wt_teleport_mod_a = DynAccessor(114179)
            wt_teleport_mod_b = DynAccessor(114180)
            wt_vampirism = DynAccessor(114181)

        ability = _ability()

    wt_event = _wt_event()