from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    space_day_congrats = DynAccessor(108023)
    _tutorialInitial = DynAccessor(108024)
    _tutorialInitialLoop = DynAccessor(108025)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(108026)
        up_particles = DynAccessor(108027)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(108028)
            crewCommander = DynAccessor(108029)
            crewDriver = DynAccessor(108030)
            crewGunner = DynAccessor(108031)
            crewLoader = DynAccessor(108032)
            crewRadioOperator = DynAccessor(108033)
            skillAdrenalineRush = DynAccessor(108034)
            skillArmorer = DynAccessor(108035)
            skillArtLamp = DynAccessor(108036)
            skillBrothersInArms = DynAccessor(108037)
            skillCallForVengeance = DynAccessor(108038)
            skillClutchBraking = DynAccessor(108039)
            skillCommanderBonus = DynAccessor(108040)
            skillConcealment = DynAccessor(108041)
            skillControlledImpact = DynAccessor(108042)
            skillDeadEye = DynAccessor(108043)
            skillDesignatedTarget = DynAccessor(108044)
            skillEagleEye = DynAccessor(108045)
            skillExpert = DynAccessor(108046)
            skillFirefighting = DynAccessor(108047)
            skillIntuition = DynAccessor(108048)
            skillJackOfAllTrades = DynAccessor(108049)
            skillMentor = DynAccessor(108050)
            skillOffRoadDriving = DynAccessor(108051)
            skillPreventativeMaintenance = DynAccessor(108052)
            skillRelaying = DynAccessor(108053)
            skillRepairs = DynAccessor(108054)
            skillSafeStowage = DynAccessor(108055)
            skillSignalBoosting = DynAccessor(108056)
            skillSituationalAwareness = DynAccessor(108057)
            skillSixthSense = DynAccessor(108058)
            skillSmoothRide = DynAccessor(108059)
            skillSnapShot = DynAccessor(108060)
            skillSniper = DynAccessor(108061)
            skillSoundIntelligence = DynAccessor(108062)
            statConcealment = DynAccessor(108063)
            statFirepower = DynAccessor(108064)
            statMobility = DynAccessor(108065)
            statSpotting = DynAccessor(108066)
            statSurvivability = DynAccessor(108067)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(108068)
        ay_gun = DynAccessor(108069)
        ay_tracks = DynAccessor(108070)
        ay_turret = DynAccessor(108071)
        video_reward = DynAccessor(108072)
        video_reward_min = DynAccessor(108073)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmunitionCrit = DynAccessor(108074)
        FueltankCrit = DynAccessor(108075)
        InSafetyWhileNotObserved = DynAccessor(108076)
        KilledWhileObserved = DynAccessor(108077)
        ModuleDamage = DynAccessor(108078)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_191_0 = DynAccessor(108079)
        v_192_0 = DynAccessor(108080)
        v_193_0 = DynAccessor(108081)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(108082)
        Intro = DynAccessor(108083)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(108084)
            overcharge = DynAccessor(108085)
            power_shot = DynAccessor(108086)
            teleport = DynAccessor(108087)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(108088)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(108089)
        example_2 = DynAccessor(108090)
        example_3 = DynAccessor(108091)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(108092)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(108093)
            gold = DynAccessor(108094)
            silver = DynAccessor(108095)
            standart = DynAccessor(108096)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(108097)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108098)
            small = DynAccessor(108099)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108100)
            standart = DynAccessor(108101)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108102)
            standart = DynAccessor(108103)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108104)
            standart = DynAccessor(108105)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108106)
            standart = DynAccessor(108107)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(108108)
            mtl_1_35 = DynAccessor(108109)
            mt_drops = DynAccessor(108110)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108111)
            medium = DynAccessor(108112)
            small = DynAccessor(108113)
            tanks_6 = DynAccessor(108114)
            tanks_7 = DynAccessor(108115)
            tanks_8 = DynAccessor(108116)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(108117)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(108118)
            intro = DynAccessor(108119)
            R239_ST_Molot_02 = DynAccessor(108120)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(108121)
            GB141_Celestial_2_51 = DynAccessor(108122)
            intro = DynAccessor(108123)
            R239_ST_Molot = DynAccessor(108124)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(108125)
            Pl35_CS_57_Sokol = DynAccessor(108126)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(108127)
        option_2 = DynAccessor(108128)
        option_3 = DynAccessor(108129)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(108130)
        Ch57_BZT_70 = DynAccessor(108131)
        F134_ARL_Projet_F = DynAccessor(108132)
        G184_EisBaer = DynAccessor(108133)
        GB140_Champion = DynAccessor(108134)
        R124_Object_279 = DynAccessor(108135)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(108136)
        operation_10 = DynAccessor(108137)
        operation_8 = DynAccessor(108138)
        operation_9 = DynAccessor(108139)
        operation_99 = DynAccessor(108140)
        video_operations_person = DynAccessor(108141)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(108142)

    platoon = _platoon()

    class _startup(DynAccessor):
        __slots__ = ()
        c_1_41_showreel = DynAccessor(108143)

    startup = _startup()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(108144)

    vehicle = _vehicle()