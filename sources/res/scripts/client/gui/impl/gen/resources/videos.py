from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(108885)
    _tutorialInitialLoop = DynAccessor(108886)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(108887)
        up_particles = DynAccessor(108888)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(108889)
            crewCommander = DynAccessor(108890)
            crewDriver = DynAccessor(108891)
            crewGunner = DynAccessor(108892)
            crewLoader = DynAccessor(108893)
            crewRadioOperator = DynAccessor(108894)
            skillAdrenalineRush = DynAccessor(108895)
            skillArmorer = DynAccessor(108896)
            skillArtLamp = DynAccessor(108897)
            skillBrothersInArms = DynAccessor(108898)
            skillCallForVengeance = DynAccessor(108899)
            skillClutchBraking = DynAccessor(108900)
            skillCommanderBonus = DynAccessor(108901)
            skillConcealment = DynAccessor(108902)
            skillControlledImpact = DynAccessor(108903)
            skillDeadEye = DynAccessor(108904)
            skillDesignatedTarget = DynAccessor(108905)
            skillEagleEye = DynAccessor(108906)
            skillExpert = DynAccessor(108907)
            skillFirefighting = DynAccessor(108908)
            skillIntuition = DynAccessor(108909)
            skillJackOfAllTrades = DynAccessor(108910)
            skillMentor = DynAccessor(108911)
            skillOffRoadDriving = DynAccessor(108912)
            skillPreventativeMaintenance = DynAccessor(108913)
            skillRelaying = DynAccessor(108914)
            skillRepairs = DynAccessor(108915)
            skillSafeStowage = DynAccessor(108916)
            skillSignalBoosting = DynAccessor(108917)
            skillSituationalAwareness = DynAccessor(108918)
            skillSixthSense = DynAccessor(108919)
            skillSmoothRide = DynAccessor(108920)
            skillSnapShot = DynAccessor(108921)
            skillSniper = DynAccessor(108922)
            skillSoundIntelligence = DynAccessor(108923)
            statConcealment = DynAccessor(108924)
            statFirepower = DynAccessor(108925)
            statMobility = DynAccessor(108926)
            statSpotting = DynAccessor(108927)
            statSurvivability = DynAccessor(108928)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(108929)
        ay_gun = DynAccessor(108930)
        ay_tracks = DynAccessor(108931)
        ay_turret = DynAccessor(108932)
        video_reward = DynAccessor(108933)
        video_reward_min = DynAccessor(108934)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_181_0 = DynAccessor(108935)
        v_182_0 = DynAccessor(108936)
        v_183_0 = DynAccessor(108937)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(108938)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(108939)
            overcharge = DynAccessor(108940)
            power_shot = DynAccessor(108941)
            rapid_shelling = DynAccessor(108942)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(108943)
            Loop_1 = DynAccessor(108944)
            Loop_10 = DynAccessor(108945)
            Loop_2 = DynAccessor(108946)
            Loop_3 = DynAccessor(108947)
            Loop_4 = DynAccessor(108948)
            Loop_5 = DynAccessor(108949)
            Loop_6 = DynAccessor(108950)
            Loop_7 = DynAccessor(108951)
            Loop_8 = DynAccessor(108952)
            Loop_9 = DynAccessor(108953)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(108954)
        example_2 = DynAccessor(108955)
        example_3 = DynAccessor(108956)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(108957)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(108958)
            gold = DynAccessor(108959)
            silver = DynAccessor(108960)
            standart = DynAccessor(108961)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(108962)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108963)
            small = DynAccessor(108964)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108965)
            standart = DynAccessor(108966)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108967)
            standart = DynAccessor(108968)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108969)
            standart = DynAccessor(108970)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(108971)
            mtl_1_35 = DynAccessor(108972)
            mt_drops = DynAccessor(108973)

        mt_lootbox = _mt_lootbox()

        class _ny2024(DynAccessor):
            __slots__ = ()
            china = DynAccessor(108974)
            magic = DynAccessor(108975)
            standart = DynAccessor(108976)
            ussr = DynAccessor(108977)
            xmas = DynAccessor(108978)

        ny2024 = _ny2024()

        class _ny2025(DynAccessor):
            __slots__ = ()
            ny_2025_big = DynAccessor(108979)
            ny_2025_small = DynAccessor(108980)
            ny_2025_tanks = DynAccessor(108981)

        ny2025 = _ny2025()

        class _ny2026(DynAccessor):
            __slots__ = ()
            ny_2026_big = DynAccessor(108982)
            ny_2026_small = DynAccessor(108983)
            ny_2026_tanks = DynAccessor(108984)

        ny2026 = _ny2026()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108985)
            medium = DynAccessor(108986)
            small = DynAccessor(108987)
            tanks_6 = DynAccessor(108988)
            tanks_7 = DynAccessor(108989)
            tanks_8 = DynAccessor(108990)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(108991)
            G171_E77 = DynAccessor(108992)
            G171_E77_02 = DynAccessor(108993)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(108994)
            intro = DynAccessor(108995)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(108996)
            Pl35_CS_57_Sokol = DynAccessor(108997)

        mtl_universal = _mtl_universal()

        class _ny_2026_big(DynAccessor):
            __slots__ = ()
            A165_XM57 = DynAccessor(108998)
            A175_OTAC_MT_58 = DynAccessor(108999)
            A175_OTAC_MT_58_02 = DynAccessor(109000)
            customizations_28748 = DynAccessor(109001)
            customizations_77132 = DynAccessor(109002)
            customizations_8046924 = DynAccessor(109003)
            customizations_8047180 = DynAccessor(109004)
            customizations_8054092 = DynAccessor(109005)
            Cz39_SD_122_49_Sekera = DynAccessor(109006)
            F118_Char_Mle_75 = DynAccessor(109007)
            G181_StuG_Maus_17cm = DynAccessor(109008)
            G196_E_75_Ausf_B_Doppel = DynAccessor(109009)
            GB139_Vulcan = DynAccessor(109010)
            intro = DynAccessor(109011)
            It33_Orso = DynAccessor(109012)
            ny_2026_tanks = DynAccessor(109013)
            R165_Object_703_II_100 = DynAccessor(109014)
            R222_Object_120_Taran = DynAccessor(109015)
            R223_T_54B_1958 = DynAccessor(109016)
            R228_Duplet = DynAccessor(109017)

        ny_2026_big = _ny_2026_big()

        class _ny_2026_tanks(DynAccessor):
            __slots__ = ()
            Cz14_Skoda_T_56 = DynAccessor(109018)
            F106_Panhard_EBR_75_Mle1954 = DynAccessor(109019)
            F116_Bat_Chatillon_Bourrasque = DynAccessor(109020)
            F97_ELC_EVEN_90 = DynAccessor(109021)
            GB99_Turtle_Mk1 = DynAccessor(109022)
            It13_Progetto_M35_mod_46 = DynAccessor(109023)

        ny_2026_tanks = _ny_2026_tanks()

    lootbox_reward_video = _lootbox_reward_video()

    class _new_year(DynAccessor):
        __slots__ = ()

        class _greetings(DynAccessor):
            __slots__ = ()
            ng_greetings = DynAccessor(109024)

        greetings = _greetings()

        class _lootbox(DynAccessor):
            __slots__ = ()
            box_delivery = DynAccessor(109025)

        lootbox = _lootbox()

        class _onboarding(DynAccessor):
            __slots__ = ()
            onboarding_day = DynAccessor(109026)
            onboarding_night = DynAccessor(109027)

        onboarding = _onboarding()

        class _pet(DynAccessor):
            __slots__ = ()
            letter = DynAccessor(109028)
            pet_story = DynAccessor(109029)

        pet = _pet()

        class _robotTvScreen(DynAccessor):
            __slots__ = ()
            tv_screen_active = DynAccessor(109030)
            tv_screen_idle = DynAccessor(109031)

        robotTvScreen = _robotTvScreen()

    new_year = _new_year()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(109032)
        operation_10 = DynAccessor(109033)
        operation_8 = DynAccessor(109034)
        operation_9 = DynAccessor(109035)
        operation_99 = DynAccessor(109036)
        video_operations_person = DynAccessor(109037)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(109038)

    platoon = _platoon()