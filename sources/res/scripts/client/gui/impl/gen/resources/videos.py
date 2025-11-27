from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(108745)
    _tutorialInitialLoop = DynAccessor(108746)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(108747)
        up_particles = DynAccessor(108748)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(108749)
            crewCommander = DynAccessor(108750)
            crewDriver = DynAccessor(108751)
            crewGunner = DynAccessor(108752)
            crewLoader = DynAccessor(108753)
            crewRadioOperator = DynAccessor(108754)
            skillAdrenalineRush = DynAccessor(108755)
            skillArmorer = DynAccessor(108756)
            skillArtLamp = DynAccessor(108757)
            skillBrothersInArms = DynAccessor(108758)
            skillCallForVengeance = DynAccessor(108759)
            skillClutchBraking = DynAccessor(108760)
            skillCommanderBonus = DynAccessor(108761)
            skillConcealment = DynAccessor(108762)
            skillControlledImpact = DynAccessor(108763)
            skillDeadEye = DynAccessor(108764)
            skillDesignatedTarget = DynAccessor(108765)
            skillEagleEye = DynAccessor(108766)
            skillExpert = DynAccessor(108767)
            skillFirefighting = DynAccessor(108768)
            skillIntuition = DynAccessor(108769)
            skillJackOfAllTrades = DynAccessor(108770)
            skillMentor = DynAccessor(108771)
            skillOffRoadDriving = DynAccessor(108772)
            skillPreventativeMaintenance = DynAccessor(108773)
            skillRelaying = DynAccessor(108774)
            skillRepairs = DynAccessor(108775)
            skillSafeStowage = DynAccessor(108776)
            skillSignalBoosting = DynAccessor(108777)
            skillSituationalAwareness = DynAccessor(108778)
            skillSixthSense = DynAccessor(108779)
            skillSmoothRide = DynAccessor(108780)
            skillSnapShot = DynAccessor(108781)
            skillSniper = DynAccessor(108782)
            skillSoundIntelligence = DynAccessor(108783)
            statConcealment = DynAccessor(108784)
            statFirepower = DynAccessor(108785)
            statMobility = DynAccessor(108786)
            statSpotting = DynAccessor(108787)
            statSurvivability = DynAccessor(108788)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(108789)
        ay_gun = DynAccessor(108790)
        ay_tracks = DynAccessor(108791)
        ay_turret = DynAccessor(108792)
        video_reward = DynAccessor(108793)
        video_reward_min = DynAccessor(108794)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_181_0 = DynAccessor(108795)
        v_182_0 = DynAccessor(108796)
        v_183_0 = DynAccessor(108797)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(108798)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(108799)
            overcharge = DynAccessor(108800)
            power_shot = DynAccessor(108801)
            rapid_shelling = DynAccessor(108802)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(108803)
            Loop_1 = DynAccessor(108804)
            Loop_10 = DynAccessor(108805)
            Loop_2 = DynAccessor(108806)
            Loop_3 = DynAccessor(108807)
            Loop_4 = DynAccessor(108808)
            Loop_5 = DynAccessor(108809)
            Loop_6 = DynAccessor(108810)
            Loop_7 = DynAccessor(108811)
            Loop_8 = DynAccessor(108812)
            Loop_9 = DynAccessor(108813)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(108814)
        example_2 = DynAccessor(108815)
        example_3 = DynAccessor(108816)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(108817)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(108818)
            gold = DynAccessor(108819)
            silver = DynAccessor(108820)
            standart = DynAccessor(108821)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(108822)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108823)
            small = DynAccessor(108824)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108825)
            standart = DynAccessor(108826)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108827)
            standart = DynAccessor(108828)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108829)
            standart = DynAccessor(108830)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(108831)
            mtl_1_35 = DynAccessor(108832)
            mt_drops = DynAccessor(108833)

        mt_lootbox = _mt_lootbox()

        class _ny2024(DynAccessor):
            __slots__ = ()
            china = DynAccessor(108834)
            magic = DynAccessor(108835)
            standart = DynAccessor(108836)
            ussr = DynAccessor(108837)
            xmas = DynAccessor(108838)

        ny2024 = _ny2024()

        class _ny2025(DynAccessor):
            __slots__ = ()
            ny_2025_big = DynAccessor(108839)
            ny_2025_small = DynAccessor(108840)
            ny_2025_tanks = DynAccessor(108841)

        ny2025 = _ny2025()

        class _ny2026(DynAccessor):
            __slots__ = ()
            ny_2026_big = DynAccessor(108842)
            ny_2026_small = DynAccessor(108843)
            ny_2026_tanks = DynAccessor(108844)

        ny2026 = _ny2026()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108845)
            medium = DynAccessor(108846)
            small = DynAccessor(108847)
            tanks_6 = DynAccessor(108848)
            tanks_7 = DynAccessor(108849)
            tanks_8 = DynAccessor(108850)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(108851)
            G171_E77 = DynAccessor(108852)
            G171_E77_02 = DynAccessor(108853)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(108854)
            intro = DynAccessor(108855)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(108856)
            Pl35_CS_57_Sokol = DynAccessor(108857)

        mtl_universal = _mtl_universal()

        class _ny_2026_big(DynAccessor):
            __slots__ = ()
            A165_XM57 = DynAccessor(108858)
            A175_OTAC_MT_58 = DynAccessor(108859)
            A175_OTAC_MT_58_02 = DynAccessor(108860)
            customizations_28748 = DynAccessor(108861)
            customizations_77132 = DynAccessor(108862)
            customizations_8046924 = DynAccessor(108863)
            customizations_8047180 = DynAccessor(108864)
            customizations_8054092 = DynAccessor(108865)
            Cz39_SD_122_49_Sekera = DynAccessor(108866)
            F118_Char_Mle_75 = DynAccessor(108867)
            G181_StuG_Maus_17cm = DynAccessor(108868)
            G196_E_75_Ausf_B_Doppel = DynAccessor(108869)
            GB139_Vulcan = DynAccessor(108870)
            intro = DynAccessor(108871)
            It33_Orso = DynAccessor(108872)
            ny_2026_tanks = DynAccessor(108873)
            R165_Object_703_II_100 = DynAccessor(108874)
            R222_Object_120_Taran = DynAccessor(108875)
            R223_T_54B_1958 = DynAccessor(108876)
            R228_Duplet = DynAccessor(108877)

        ny_2026_big = _ny_2026_big()

        class _ny_2026_tanks(DynAccessor):
            __slots__ = ()
            Cz14_Skoda_T_56 = DynAccessor(108878)
            F106_Panhard_EBR_75_Mle1954 = DynAccessor(108879)
            F116_Bat_Chatillon_Bourrasque = DynAccessor(108880)
            F97_ELC_EVEN_90 = DynAccessor(108881)
            GB99_Turtle_Mk1 = DynAccessor(108882)
            It13_Progetto_M35_mod_46 = DynAccessor(108883)

        ny_2026_tanks = _ny_2026_tanks()

    lootbox_reward_video = _lootbox_reward_video()

    class _new_year(DynAccessor):
        __slots__ = ()

        class _greetings(DynAccessor):
            __slots__ = ()
            ng_greetings = DynAccessor(108884)

        greetings = _greetings()

        class _lootbox(DynAccessor):
            __slots__ = ()
            box_delivery = DynAccessor(108885)

        lootbox = _lootbox()

        class _onboarding(DynAccessor):
            __slots__ = ()
            onboarding_day = DynAccessor(108886)
            onboarding_night = DynAccessor(108887)

        onboarding = _onboarding()

        class _pet(DynAccessor):
            __slots__ = ()
            letter = DynAccessor(108888)
            pet_story = DynAccessor(108889)

        pet = _pet()

        class _robotTvScreen(DynAccessor):
            __slots__ = ()
            tv_screen_active = DynAccessor(108890)
            tv_screen_idle = DynAccessor(108891)

        robotTvScreen = _robotTvScreen()

    new_year = _new_year()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(108892)
        operation_10 = DynAccessor(108893)
        operation_8 = DynAccessor(108894)
        operation_9 = DynAccessor(108895)
        operation_99 = DynAccessor(108896)
        video_operations_person = DynAccessor(108897)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(108898)

    platoon = _platoon()