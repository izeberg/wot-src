from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(108744)
    _tutorialInitialLoop = DynAccessor(108745)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(108746)
        up_particles = DynAccessor(108747)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(108748)
            crewCommander = DynAccessor(108749)
            crewDriver = DynAccessor(108750)
            crewGunner = DynAccessor(108751)
            crewLoader = DynAccessor(108752)
            crewRadioOperator = DynAccessor(108753)
            skillAdrenalineRush = DynAccessor(108754)
            skillArmorer = DynAccessor(108755)
            skillArtLamp = DynAccessor(108756)
            skillBrothersInArms = DynAccessor(108757)
            skillCallForVengeance = DynAccessor(108758)
            skillClutchBraking = DynAccessor(108759)
            skillCommanderBonus = DynAccessor(108760)
            skillConcealment = DynAccessor(108761)
            skillControlledImpact = DynAccessor(108762)
            skillDeadEye = DynAccessor(108763)
            skillDesignatedTarget = DynAccessor(108764)
            skillEagleEye = DynAccessor(108765)
            skillExpert = DynAccessor(108766)
            skillFirefighting = DynAccessor(108767)
            skillIntuition = DynAccessor(108768)
            skillJackOfAllTrades = DynAccessor(108769)
            skillMentor = DynAccessor(108770)
            skillOffRoadDriving = DynAccessor(108771)
            skillPreventativeMaintenance = DynAccessor(108772)
            skillRelaying = DynAccessor(108773)
            skillRepairs = DynAccessor(108774)
            skillSafeStowage = DynAccessor(108775)
            skillSignalBoosting = DynAccessor(108776)
            skillSituationalAwareness = DynAccessor(108777)
            skillSixthSense = DynAccessor(108778)
            skillSmoothRide = DynAccessor(108779)
            skillSnapShot = DynAccessor(108780)
            skillSniper = DynAccessor(108781)
            skillSoundIntelligence = DynAccessor(108782)
            statConcealment = DynAccessor(108783)
            statFirepower = DynAccessor(108784)
            statMobility = DynAccessor(108785)
            statSpotting = DynAccessor(108786)
            statSurvivability = DynAccessor(108787)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(108788)
        ay_gun = DynAccessor(108789)
        ay_tracks = DynAccessor(108790)
        ay_turret = DynAccessor(108791)
        video_reward = DynAccessor(108792)
        video_reward_min = DynAccessor(108793)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_181_0 = DynAccessor(108794)
        v_182_0 = DynAccessor(108795)
        v_183_0 = DynAccessor(108796)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(108797)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(108798)
            overcharge = DynAccessor(108799)
            power_shot = DynAccessor(108800)
            rapid_shelling = DynAccessor(108801)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(108802)
            Loop_1 = DynAccessor(108803)
            Loop_10 = DynAccessor(108804)
            Loop_2 = DynAccessor(108805)
            Loop_3 = DynAccessor(108806)
            Loop_4 = DynAccessor(108807)
            Loop_5 = DynAccessor(108808)
            Loop_6 = DynAccessor(108809)
            Loop_7 = DynAccessor(108810)
            Loop_8 = DynAccessor(108811)
            Loop_9 = DynAccessor(108812)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(108813)
        example_2 = DynAccessor(108814)
        example_3 = DynAccessor(108815)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(108816)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(108817)
            gold = DynAccessor(108818)
            silver = DynAccessor(108819)
            standart = DynAccessor(108820)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(108821)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108822)
            small = DynAccessor(108823)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108824)
            standart = DynAccessor(108825)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108826)
            standart = DynAccessor(108827)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108828)
            standart = DynAccessor(108829)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(108830)
            mtl_1_35 = DynAccessor(108831)
            mt_drops = DynAccessor(108832)

        mt_lootbox = _mt_lootbox()

        class _ny2024(DynAccessor):
            __slots__ = ()
            china = DynAccessor(108833)
            magic = DynAccessor(108834)
            standart = DynAccessor(108835)
            ussr = DynAccessor(108836)
            xmas = DynAccessor(108837)

        ny2024 = _ny2024()

        class _ny2025(DynAccessor):
            __slots__ = ()
            ny_2025_big = DynAccessor(108838)
            ny_2025_small = DynAccessor(108839)
            ny_2025_tanks = DynAccessor(108840)

        ny2025 = _ny2025()

        class _ny2026(DynAccessor):
            __slots__ = ()
            ny_2026_big = DynAccessor(108841)
            ny_2026_small = DynAccessor(108842)
            ny_2026_tanks = DynAccessor(108843)

        ny2026 = _ny2026()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108844)
            medium = DynAccessor(108845)
            small = DynAccessor(108846)
            tanks_6 = DynAccessor(108847)
            tanks_7 = DynAccessor(108848)
            tanks_8 = DynAccessor(108849)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(108850)
            G171_E77 = DynAccessor(108851)
            G171_E77_02 = DynAccessor(108852)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(108853)
            intro = DynAccessor(108854)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(108855)
            Pl35_CS_57_Sokol = DynAccessor(108856)

        mtl_universal = _mtl_universal()

        class _ny_2026_big(DynAccessor):
            __slots__ = ()
            A156_T54_2022 = DynAccessor(108857)
            A163_H_3 = DynAccessor(108858)
            Ch56_BZ_74_1 = DynAccessor(108859)
            customizations_113740 = DynAccessor(108860)
            customizations_22348 = DynAccessor(108861)
            customizations_31308 = DynAccessor(108862)
            customizations_75084 = DynAccessor(108863)
            customizations_93772 = DynAccessor(108864)
            Cz32_Vz_58_Koncept = DynAccessor(108865)
            F129_Schneider_120_AC_Gendarme = DynAccessor(108866)
            G98_Waffentrager_E100 = DynAccessor(108867)
            GB118_Taurus_CA = DynAccessor(108868)
            GB128_Nemesis = DynAccessor(108869)
            intro = DynAccessor(108870)
            It32_Prototipo_6 = DynAccessor(108871)
            ny_2026_tanks = DynAccessor(108872)
            R199_SU_122V = DynAccessor(108873)
            R203_Object_168N = DynAccessor(108874)
            R219_Waffentrager_E100_Gold = DynAccessor(108875)
            S31_Strv_K = DynAccessor(108876)

        ny_2026_big = _ny_2026_big()

        class _ny_2026_tanks(DynAccessor):
            __slots__ = ()
            F69_AMX13_57_100 = DynAccessor(108877)
            G36_PzII_J = DynAccessor(108878)
            G48_E_25 = DynAccessor(108879)
            R50_SU76I = DynAccessor(108880)

        ny_2026_tanks = _ny_2026_tanks()

    lootbox_reward_video = _lootbox_reward_video()

    class _new_year(DynAccessor):
        __slots__ = ()

        class _greetings(DynAccessor):
            __slots__ = ()
            ng_greetings = DynAccessor(108881)

        greetings = _greetings()

        class _lootbox(DynAccessor):
            __slots__ = ()
            box_delivery = DynAccessor(108882)

        lootbox = _lootbox()

        class _onboarding(DynAccessor):
            __slots__ = ()
            onboarding_day = DynAccessor(108883)
            onboarding_night = DynAccessor(108884)

        onboarding = _onboarding()

        class _pet(DynAccessor):
            __slots__ = ()
            letter = DynAccessor(108885)
            pet_story = DynAccessor(108886)

        pet = _pet()

        class _robotTvScreen(DynAccessor):
            __slots__ = ()
            tv_screen_active = DynAccessor(108887)
            tv_screen_idle = DynAccessor(108888)

        robotTvScreen = _robotTvScreen()

    new_year = _new_year()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(108889)
        operation_10 = DynAccessor(108890)
        operation_8 = DynAccessor(108891)
        operation_9 = DynAccessor(108892)
        operation_99 = DynAccessor(108893)
        video_operations_person = DynAccessor(108894)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(108895)

    platoon = _platoon()