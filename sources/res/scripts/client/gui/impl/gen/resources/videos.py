from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _bootcampLesson1 = DynAccessor(104633)
    _bootcampLesson2 = DynAccessor(104634)
    _bootcampLesson3_1 = DynAccessor(104635)
    _bootcampLesson3_2 = DynAccessor(104636)
    _bootcampLesson4 = DynAccessor(104637)
    _bootcampOutro = DynAccessor(104638)
    _tutorialInitial = DynAccessor(104639)
    _tutorialInitialLoop = DynAccessor(104640)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(104641)
        up_particles = DynAccessor(104642)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(104643)
            crewCommander = DynAccessor(104644)
            crewDriver = DynAccessor(104645)
            crewGunner = DynAccessor(104646)
            crewLoader = DynAccessor(104647)
            crewRadioOperator = DynAccessor(104648)
            skillAdrenalineRush = DynAccessor(104649)
            skillArmorer = DynAccessor(104650)
            skillArtLamp = DynAccessor(104651)
            skillBrothersInArms = DynAccessor(104652)
            skillCallForVengeance = DynAccessor(104653)
            skillClutchBraking = DynAccessor(104654)
            skillCommanderBonus = DynAccessor(104655)
            skillConcealment = DynAccessor(104656)
            skillControlledImpact = DynAccessor(104657)
            skillDeadEye = DynAccessor(104658)
            skillDesignatedTarget = DynAccessor(104659)
            skillEagleEye = DynAccessor(104660)
            skillExpert = DynAccessor(104661)
            skillFirefighting = DynAccessor(104662)
            skillIntuition = DynAccessor(104663)
            skillJackOfAllTrades = DynAccessor(104664)
            skillMentor = DynAccessor(104665)
            skillOffRoadDriving = DynAccessor(104666)
            skillPreventativeMaintenance = DynAccessor(104667)
            skillRelaying = DynAccessor(104668)
            skillRepairs = DynAccessor(104669)
            skillSafeStowage = DynAccessor(104670)
            skillSignalBoosting = DynAccessor(104671)
            skillSituationalAwareness = DynAccessor(104672)
            skillSixthSense = DynAccessor(104673)
            skillSmoothRide = DynAccessor(104674)
            skillSnapShot = DynAccessor(104675)
            skillSniper = DynAccessor(104676)
            skillSoundIntelligence = DynAccessor(104677)
            statConcealment = DynAccessor(104678)
            statFirepower = DynAccessor(104679)
            statMobility = DynAccessor(104680)
            statSpotting = DynAccessor(104681)
            statSurvivability = DynAccessor(104682)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(104683)
        ay_gun = DynAccessor(104684)
        ay_tracks = DynAccessor(104685)
        ay_turret = DynAccessor(104686)
        video_reward = DynAccessor(104687)
        video_reward_min = DynAccessor(104688)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_181_0 = DynAccessor(104689)
        v_182_0 = DynAccessor(104690)
        v_183_0 = DynAccessor(104691)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(104692)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(104693)
            overcharge = DynAccessor(104694)
            power_shot = DynAccessor(104695)
            rapid_shelling = DynAccessor(104696)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(104697)
            Loop_1 = DynAccessor(104698)
            Loop_10 = DynAccessor(104699)
            Loop_2 = DynAccessor(104700)
            Loop_3 = DynAccessor(104701)
            Loop_4 = DynAccessor(104702)
            Loop_5 = DynAccessor(104703)
            Loop_6 = DynAccessor(104704)
            Loop_7 = DynAccessor(104705)
            Loop_8 = DynAccessor(104706)
            Loop_9 = DynAccessor(104707)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(104708)
        example_2 = DynAccessor(104709)
        example_3 = DynAccessor(104710)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        lootbox_prem = DynAccessor(104711)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(104712)
            gold = DynAccessor(104713)
            silver = DynAccessor(104714)
            standart = DynAccessor(104715)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(104716)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(104717)
            small = DynAccessor(104718)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104719)
            standart = DynAccessor(104720)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104721)
            standart = DynAccessor(104722)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104723)
            standart = DynAccessor(104724)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(104725)
            mtl_1_35 = DynAccessor(104726)
            mt_drops = DynAccessor(104727)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(104728)
            medium = DynAccessor(104729)
            small = DynAccessor(104730)
            tanks_6 = DynAccessor(104731)
            tanks_7 = DynAccessor(104732)
            tanks_8 = DynAccessor(104733)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(104734)
            G171_E77 = DynAccessor(104735)
            G171_E77_02 = DynAccessor(104736)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(104737)
            intro = DynAccessor(104738)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(104739)
            Pl35_CS_57_Sokol = DynAccessor(104740)

        mtl_universal = _mtl_universal()

        class _tanks_birthday_2025(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(104741)
            A124_T54E2 = DynAccessor(104742)
            A149_AMBT = DynAccessor(104743)
            Ch43_WZ_122_2 = DynAccessor(104744)
            F130_AMX_Tracteur_D = DynAccessor(104745)
            G168_KJpz_T_III = DynAccessor(104746)
            GB110_FV4201_Chieftain_Prototype = DynAccessor(104747)
            GB112_Caliban = DynAccessor(104748)
            intro = DynAccessor(104749)
            It18_Progetto_C45_mod_71 = DynAccessor(104750)
            Pl19_CS_52_LIS = DynAccessor(104751)
            R188_Object_259A = DynAccessor(104752)
            R227_Object_407_MZ = DynAccessor(104753)

        tanks_birthday_2025 = _tanks_birthday_2025()

    lootbox_reward_video = _lootbox_reward_video()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(104754)
        operation_10 = DynAccessor(104755)
        operation_8 = DynAccessor(104756)
        operation_9 = DynAccessor(104757)
        operation_99 = DynAccessor(104758)
        video_operations_person = DynAccessor(104759)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(104760)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(104761)

    vehicle = _vehicle()

    class _wt_event(DynAccessor):
        __slots__ = ()
        c_2_Projet_57_Ampere_v001 = DynAccessor(104762)
        boss_portal_idle = DynAccessor(104763)
        boss_portal_open = DynAccessor(104764)
        CVT_Spider_v001 = DynAccessor(104765)
        Czolg_P_Wz_46_3dst_Verbesserter_v001 = DynAccessor(104766)
        hunter_portal_idle = DynAccessor(104767)
        hunter_portal_open = DynAccessor(104768)
        MAIN_2_Projet_57_Ampere_v001 = DynAccessor(104769)
        MAIN_CVT_Spider_v001 = DynAccessor(104770)
        MAIN_Czolg_P_Wz_46_3dst_Verbesserter_v001 = DynAccessor(104771)
        MAIN_Projekt_SAT_v003 = DynAccessor(104772)
        MAIN_Projet_57_v001 = DynAccessor(104773)
        Projekt_SAT_v003 = DynAccessor(104774)
        Projet_57_v001 = DynAccessor(104775)
        vehicle1_v001 = DynAccessor(104776)
        vehicle2_v001 = DynAccessor(104777)
        vehicle3_v001 = DynAccessor(104778)
        vehicle4_v001 = DynAccessor(104779)
        vehicle5_v001 = DynAccessor(104780)
        vehicle_common = DynAccessor(104781)
        wt_intro = DynAccessor(104782)
        wt_outro = DynAccessor(104783)

    wt_event = _wt_event()