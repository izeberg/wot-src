from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(108692)
    _tutorialInitialLoop = DynAccessor(108693)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(108694)
        up_particles = DynAccessor(108695)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(108696)
            crewCommander = DynAccessor(108697)
            crewDriver = DynAccessor(108698)
            crewGunner = DynAccessor(108699)
            crewLoader = DynAccessor(108700)
            crewRadioOperator = DynAccessor(108701)
            skillAdrenalineRush = DynAccessor(108702)
            skillArmorer = DynAccessor(108703)
            skillArtLamp = DynAccessor(108704)
            skillBrothersInArms = DynAccessor(108705)
            skillCallForVengeance = DynAccessor(108706)
            skillClutchBraking = DynAccessor(108707)
            skillCommanderBonus = DynAccessor(108708)
            skillConcealment = DynAccessor(108709)
            skillControlledImpact = DynAccessor(108710)
            skillDeadEye = DynAccessor(108711)
            skillDesignatedTarget = DynAccessor(108712)
            skillEagleEye = DynAccessor(108713)
            skillExpert = DynAccessor(108714)
            skillFirefighting = DynAccessor(108715)
            skillIntuition = DynAccessor(108716)
            skillJackOfAllTrades = DynAccessor(108717)
            skillMentor = DynAccessor(108718)
            skillOffRoadDriving = DynAccessor(108719)
            skillPreventativeMaintenance = DynAccessor(108720)
            skillRelaying = DynAccessor(108721)
            skillRepairs = DynAccessor(108722)
            skillSafeStowage = DynAccessor(108723)
            skillSignalBoosting = DynAccessor(108724)
            skillSituationalAwareness = DynAccessor(108725)
            skillSixthSense = DynAccessor(108726)
            skillSmoothRide = DynAccessor(108727)
            skillSnapShot = DynAccessor(108728)
            skillSniper = DynAccessor(108729)
            skillSoundIntelligence = DynAccessor(108730)
            statConcealment = DynAccessor(108731)
            statFirepower = DynAccessor(108732)
            statMobility = DynAccessor(108733)
            statSpotting = DynAccessor(108734)
            statSurvivability = DynAccessor(108735)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(108736)
        ay_gun = DynAccessor(108737)
        ay_tracks = DynAccessor(108738)
        ay_turret = DynAccessor(108739)
        video_reward = DynAccessor(108740)
        video_reward_min = DynAccessor(108741)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_181_0 = DynAccessor(108742)
        v_182_0 = DynAccessor(108743)
        v_183_0 = DynAccessor(108744)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(108745)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(108746)
            overcharge = DynAccessor(108747)
            power_shot = DynAccessor(108748)
            rapid_shelling = DynAccessor(108749)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(108750)
            Loop_1 = DynAccessor(108751)
            Loop_10 = DynAccessor(108752)
            Loop_2 = DynAccessor(108753)
            Loop_3 = DynAccessor(108754)
            Loop_4 = DynAccessor(108755)
            Loop_5 = DynAccessor(108756)
            Loop_6 = DynAccessor(108757)
            Loop_7 = DynAccessor(108758)
            Loop_8 = DynAccessor(108759)
            Loop_9 = DynAccessor(108760)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(108761)
        example_2 = DynAccessor(108762)
        example_3 = DynAccessor(108763)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(108764)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(108765)
            gold = DynAccessor(108766)
            silver = DynAccessor(108767)
            standart = DynAccessor(108768)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(108769)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108770)
            small = DynAccessor(108771)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108772)
            standart = DynAccessor(108773)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108774)
            standart = DynAccessor(108775)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108776)
            standart = DynAccessor(108777)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(108778)
            mtl_1_35 = DynAccessor(108779)
            mt_drops = DynAccessor(108780)

        mt_lootbox = _mt_lootbox()

        class _ny2024(DynAccessor):
            __slots__ = ()
            china = DynAccessor(108781)
            magic = DynAccessor(108782)
            standart = DynAccessor(108783)
            ussr = DynAccessor(108784)
            xmas = DynAccessor(108785)

        ny2024 = _ny2024()

        class _ny2025(DynAccessor):
            __slots__ = ()
            ny_2025_big = DynAccessor(108786)
            ny_2025_small = DynAccessor(108787)
            ny_2025_tanks = DynAccessor(108788)

        ny2025 = _ny2025()

        class _ny2026(DynAccessor):
            __slots__ = ()
            ny_2026_big = DynAccessor(108789)
            ny_2026_small = DynAccessor(108790)
            ny_2026_tanks = DynAccessor(108791)

        ny2026 = _ny2026()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108792)
            medium = DynAccessor(108793)
            small = DynAccessor(108794)
            tanks_6 = DynAccessor(108795)
            tanks_7 = DynAccessor(108796)
            tanks_8 = DynAccessor(108797)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(108798)
            G171_E77 = DynAccessor(108799)
            G171_E77_02 = DynAccessor(108800)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(108801)
            intro = DynAccessor(108802)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(108803)
            Pl35_CS_57_Sokol = DynAccessor(108804)

        mtl_universal = _mtl_universal()

        class _ny_2026_big(DynAccessor):
            __slots__ = ()
            A156_T54_2022 = DynAccessor(108805)
            A163_H_3 = DynAccessor(108806)
            Ch56_BZ_74_1 = DynAccessor(108807)
            customizations_113740 = DynAccessor(108808)
            customizations_22348 = DynAccessor(108809)
            customizations_31308 = DynAccessor(108810)
            customizations_75084 = DynAccessor(108811)
            customizations_93772 = DynAccessor(108812)
            Cz32_Vz_58_Koncept = DynAccessor(108813)
            F129_Schneider_120_AC_Gendarme = DynAccessor(108814)
            G98_Waffentrager_E100 = DynAccessor(108815)
            GB118_Taurus_CA = DynAccessor(108816)
            GB128_Nemesis = DynAccessor(108817)
            intro = DynAccessor(108818)
            It32_Prototipo_6 = DynAccessor(108819)
            ny_2026_tanks = DynAccessor(108820)
            R199_SU_122V = DynAccessor(108821)
            R203_Object_168N = DynAccessor(108822)
            R219_Waffentrager_E100_Gold = DynAccessor(108823)
            S31_Strv_K = DynAccessor(108824)

        ny_2026_big = _ny_2026_big()

        class _ny_2026_tanks(DynAccessor):
            __slots__ = ()
            F69_AMX13_57_100 = DynAccessor(108825)
            G36_PzII_J = DynAccessor(108826)
            G48_E_25 = DynAccessor(108827)
            R50_SU76I = DynAccessor(108828)

        ny_2026_tanks = _ny_2026_tanks()

    lootbox_reward_video = _lootbox_reward_video()

    class _new_year(DynAccessor):
        __slots__ = ()

        class _greetings(DynAccessor):
            __slots__ = ()
            ng_greetings = DynAccessor(108829)

        greetings = _greetings()

        class _lootbox(DynAccessor):
            __slots__ = ()
            box_delivery = DynAccessor(108830)

        lootbox = _lootbox()

        class _onboarding(DynAccessor):
            __slots__ = ()
            onboarding_day = DynAccessor(108831)
            onboarding_night = DynAccessor(108832)

        onboarding = _onboarding()

        class _pet(DynAccessor):
            __slots__ = ()
            letter = DynAccessor(108833)
            pet_story = DynAccessor(108834)

        pet = _pet()

        class _robotTvScreen(DynAccessor):
            __slots__ = ()
            tv_screen_active = DynAccessor(108835)
            tv_screen_idle = DynAccessor(108836)

        robotTvScreen = _robotTvScreen()

    new_year = _new_year()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(108837)
        operation_10 = DynAccessor(108838)
        operation_8 = DynAccessor(108839)
        operation_9 = DynAccessor(108840)
        operation_99 = DynAccessor(108841)
        video_operations_person = DynAccessor(108842)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(108843)

    platoon = _platoon()