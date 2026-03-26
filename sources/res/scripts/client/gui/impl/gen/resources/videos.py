from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    space_day_congrats = DynAccessor(108044)
    _tutorialInitial = DynAccessor(108045)
    _tutorialInitialLoop = DynAccessor(108046)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(108047)
        up_particles = DynAccessor(108048)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(108049)
            crewCommander = DynAccessor(108050)
            crewDriver = DynAccessor(108051)
            crewGunner = DynAccessor(108052)
            crewLoader = DynAccessor(108053)
            crewRadioOperator = DynAccessor(108054)
            skillAdrenalineRush = DynAccessor(108055)
            skillArmorer = DynAccessor(108056)
            skillArtLamp = DynAccessor(108057)
            skillBrothersInArms = DynAccessor(108058)
            skillCallForVengeance = DynAccessor(108059)
            skillClutchBraking = DynAccessor(108060)
            skillCommanderBonus = DynAccessor(108061)
            skillConcealment = DynAccessor(108062)
            skillControlledImpact = DynAccessor(108063)
            skillDeadEye = DynAccessor(108064)
            skillDesignatedTarget = DynAccessor(108065)
            skillEagleEye = DynAccessor(108066)
            skillExpert = DynAccessor(108067)
            skillFirefighting = DynAccessor(108068)
            skillIntuition = DynAccessor(108069)
            skillJackOfAllTrades = DynAccessor(108070)
            skillMentor = DynAccessor(108071)
            skillOffRoadDriving = DynAccessor(108072)
            skillPreventativeMaintenance = DynAccessor(108073)
            skillRelaying = DynAccessor(108074)
            skillRepairs = DynAccessor(108075)
            skillSafeStowage = DynAccessor(108076)
            skillSignalBoosting = DynAccessor(108077)
            skillSituationalAwareness = DynAccessor(108078)
            skillSixthSense = DynAccessor(108079)
            skillSmoothRide = DynAccessor(108080)
            skillSnapShot = DynAccessor(108081)
            skillSniper = DynAccessor(108082)
            skillSoundIntelligence = DynAccessor(108083)
            statConcealment = DynAccessor(108084)
            statFirepower = DynAccessor(108085)
            statMobility = DynAccessor(108086)
            statSpotting = DynAccessor(108087)
            statSurvivability = DynAccessor(108088)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(108089)
        ay_gun = DynAccessor(108090)
        ay_tracks = DynAccessor(108091)
        ay_turret = DynAccessor(108092)
        video_reward = DynAccessor(108093)
        video_reward_min = DynAccessor(108094)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmunitionCrit = DynAccessor(108095)
        FueltankCrit = DynAccessor(108096)
        InSafetyWhileNotObserved = DynAccessor(108097)
        KilledWhileObserved = DynAccessor(108098)
        ModuleDamage = DynAccessor(108099)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_191_0 = DynAccessor(108100)
        v_192_0 = DynAccessor(108101)
        v_193_0 = DynAccessor(108102)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(108103)
        Intro = DynAccessor(108104)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(108105)
            overcharge = DynAccessor(108106)
            power_shot = DynAccessor(108107)
            teleport = DynAccessor(108108)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(108109)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(108110)
        example_2 = DynAccessor(108111)
        example_3 = DynAccessor(108112)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(108113)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(108114)
            gold = DynAccessor(108115)
            silver = DynAccessor(108116)
            standart = DynAccessor(108117)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(108118)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108119)
            small = DynAccessor(108120)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108121)
            standart = DynAccessor(108122)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108123)
            standart = DynAccessor(108124)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108125)
            standart = DynAccessor(108126)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108127)
            standart = DynAccessor(108128)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(108129)
            mtl_1_35 = DynAccessor(108130)
            mt_drops = DynAccessor(108131)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108132)
            medium = DynAccessor(108133)
            small = DynAccessor(108134)
            tanks_6 = DynAccessor(108135)
            tanks_7 = DynAccessor(108136)
            tanks_8 = DynAccessor(108137)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(108138)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(108139)
            intro = DynAccessor(108140)
            R239_ST_Molot_02 = DynAccessor(108141)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(108142)
            GB141_Celestial_2_51 = DynAccessor(108143)
            intro = DynAccessor(108144)
            R239_ST_Molot = DynAccessor(108145)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(108146)
            Pl35_CS_57_Sokol = DynAccessor(108147)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(108148)
        option_2 = DynAccessor(108149)
        option_3 = DynAccessor(108150)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(108151)
        Ch57_BZT_70 = DynAccessor(108152)
        F134_ARL_Projet_F = DynAccessor(108153)
        G184_EisBaer = DynAccessor(108154)
        GB140_Champion = DynAccessor(108155)
        R124_Object_279 = DynAccessor(108156)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(108157)
        operation_10 = DynAccessor(108158)
        operation_8 = DynAccessor(108159)
        operation_9 = DynAccessor(108160)
        operation_99 = DynAccessor(108161)
        video_operations_person = DynAccessor(108162)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(108163)

    platoon = _platoon()

    class _startup(DynAccessor):
        __slots__ = ()
        c_1_41_showreel = DynAccessor(108164)

    startup = _startup()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(108165)

    vehicle = _vehicle()