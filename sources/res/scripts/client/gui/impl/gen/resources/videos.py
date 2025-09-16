from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _bootcampLesson1 = DynAccessor(104628)
    _bootcampLesson2 = DynAccessor(104629)
    _bootcampLesson3_1 = DynAccessor(104630)
    _bootcampLesson3_2 = DynAccessor(104631)
    _bootcampLesson4 = DynAccessor(104632)
    _bootcampOutro = DynAccessor(104633)
    _tutorialInitial = DynAccessor(104634)
    _tutorialInitialLoop = DynAccessor(104635)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(104636)
        up_particles = DynAccessor(104637)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(104638)
            crewCommander = DynAccessor(104639)
            crewDriver = DynAccessor(104640)
            crewGunner = DynAccessor(104641)
            crewLoader = DynAccessor(104642)
            crewRadioOperator = DynAccessor(104643)
            skillAdrenalineRush = DynAccessor(104644)
            skillArmorer = DynAccessor(104645)
            skillArtLamp = DynAccessor(104646)
            skillBrothersInArms = DynAccessor(104647)
            skillCallForVengeance = DynAccessor(104648)
            skillClutchBraking = DynAccessor(104649)
            skillCommanderBonus = DynAccessor(104650)
            skillConcealment = DynAccessor(104651)
            skillControlledImpact = DynAccessor(104652)
            skillDeadEye = DynAccessor(104653)
            skillDesignatedTarget = DynAccessor(104654)
            skillEagleEye = DynAccessor(104655)
            skillExpert = DynAccessor(104656)
            skillFirefighting = DynAccessor(104657)
            skillIntuition = DynAccessor(104658)
            skillJackOfAllTrades = DynAccessor(104659)
            skillMentor = DynAccessor(104660)
            skillOffRoadDriving = DynAccessor(104661)
            skillPreventativeMaintenance = DynAccessor(104662)
            skillRelaying = DynAccessor(104663)
            skillRepairs = DynAccessor(104664)
            skillSafeStowage = DynAccessor(104665)
            skillSignalBoosting = DynAccessor(104666)
            skillSituationalAwareness = DynAccessor(104667)
            skillSixthSense = DynAccessor(104668)
            skillSmoothRide = DynAccessor(104669)
            skillSnapShot = DynAccessor(104670)
            skillSniper = DynAccessor(104671)
            skillSoundIntelligence = DynAccessor(104672)
            statConcealment = DynAccessor(104673)
            statFirepower = DynAccessor(104674)
            statMobility = DynAccessor(104675)
            statSpotting = DynAccessor(104676)
            statSurvivability = DynAccessor(104677)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(104678)
        ay_gun = DynAccessor(104679)
        ay_tracks = DynAccessor(104680)
        ay_turret = DynAccessor(104681)
        video_reward = DynAccessor(104682)
        video_reward_min = DynAccessor(104683)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_181_0 = DynAccessor(104684)
        v_182_0 = DynAccessor(104685)
        v_183_0 = DynAccessor(104686)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(104687)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(104688)
            overcharge = DynAccessor(104689)
            power_shot = DynAccessor(104690)
            rapid_shelling = DynAccessor(104691)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(104692)
            Loop_1 = DynAccessor(104693)
            Loop_10 = DynAccessor(104694)
            Loop_2 = DynAccessor(104695)
            Loop_3 = DynAccessor(104696)
            Loop_4 = DynAccessor(104697)
            Loop_5 = DynAccessor(104698)
            Loop_6 = DynAccessor(104699)
            Loop_7 = DynAccessor(104700)
            Loop_8 = DynAccessor(104701)
            Loop_9 = DynAccessor(104702)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(104703)
        example_2 = DynAccessor(104704)
        example_3 = DynAccessor(104705)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        lootbox_prem = DynAccessor(104706)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(104707)
            gold = DynAccessor(104708)
            silver = DynAccessor(104709)
            standart = DynAccessor(104710)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(104711)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(104712)
            small = DynAccessor(104713)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104714)
            standart = DynAccessor(104715)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104716)
            standart = DynAccessor(104717)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104718)
            standart = DynAccessor(104719)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(104720)
            mtl_1_35 = DynAccessor(104721)
            mt_drops = DynAccessor(104722)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(104723)
            medium = DynAccessor(104724)
            small = DynAccessor(104725)
            tanks_6 = DynAccessor(104726)
            tanks_7 = DynAccessor(104727)
            tanks_8 = DynAccessor(104728)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(104729)
            G171_E77 = DynAccessor(104730)
            G171_E77_02 = DynAccessor(104731)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(104732)
            intro = DynAccessor(104733)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(104734)
            Pl35_CS_57_Sokol = DynAccessor(104735)

        mtl_universal = _mtl_universal()

        class _tanks_birthday_2025(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(104736)
            A124_T54E2 = DynAccessor(104737)
            A149_AMBT = DynAccessor(104738)
            Ch43_WZ_122_2 = DynAccessor(104739)
            F130_AMX_Tracteur_D = DynAccessor(104740)
            G168_KJpz_T_III = DynAccessor(104741)
            GB110_FV4201_Chieftain_Prototype = DynAccessor(104742)
            GB112_Caliban = DynAccessor(104743)
            intro = DynAccessor(104744)
            It18_Progetto_C45_mod_71 = DynAccessor(104745)
            Pl19_CS_52_LIS = DynAccessor(104746)
            R188_Object_259A = DynAccessor(104747)
            R227_Object_407_MZ = DynAccessor(104748)

        tanks_birthday_2025 = _tanks_birthday_2025()

    lootbox_reward_video = _lootbox_reward_video()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(104749)
        operation_10 = DynAccessor(104750)
        operation_8 = DynAccessor(104751)
        operation_9 = DynAccessor(104752)
        operation_99 = DynAccessor(104753)
        video_operations_person = DynAccessor(104754)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(104755)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(104756)

    vehicle = _vehicle()

    class _wt_event(DynAccessor):
        __slots__ = ()
        c_2_Projet_57_Ampere_v001 = DynAccessor(104757)
        boss_portal_idle = DynAccessor(104758)
        boss_portal_open = DynAccessor(104759)
        CVT_Spider_v001 = DynAccessor(104760)
        Czolg_P_Wz_46_3dst_Verbesserter_v001 = DynAccessor(104761)
        hunter_portal_idle = DynAccessor(104762)
        hunter_portal_open = DynAccessor(104763)
        MAIN_2_Projet_57_Ampere_v001 = DynAccessor(104764)
        MAIN_CVT_Spider_v001 = DynAccessor(104765)
        MAIN_Czolg_P_Wz_46_3dst_Verbesserter_v001 = DynAccessor(104766)
        MAIN_Projekt_SAT_v003 = DynAccessor(104767)
        MAIN_Projet_57_v001 = DynAccessor(104768)
        Projekt_SAT_v003 = DynAccessor(104769)
        Projet_57_v001 = DynAccessor(104770)
        vehicle1_v001 = DynAccessor(104771)
        vehicle2_v001 = DynAccessor(104772)
        vehicle3_v001 = DynAccessor(104773)
        vehicle4_v001 = DynAccessor(104774)
        vehicle5_v001 = DynAccessor(104775)
        vehicle_common = DynAccessor(104776)
        wt_intro = DynAccessor(104777)
        wt_outro = DynAccessor(104778)

    wt_event = _wt_event()