from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(108883)
    _tutorialInitialLoop = DynAccessor(108884)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(108885)
        up_particles = DynAccessor(108886)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(108887)
            crewCommander = DynAccessor(108888)
            crewDriver = DynAccessor(108889)
            crewGunner = DynAccessor(108890)
            crewLoader = DynAccessor(108891)
            crewRadioOperator = DynAccessor(108892)
            skillAdrenalineRush = DynAccessor(108893)
            skillArmorer = DynAccessor(108894)
            skillArtLamp = DynAccessor(108895)
            skillBrothersInArms = DynAccessor(108896)
            skillCallForVengeance = DynAccessor(108897)
            skillClutchBraking = DynAccessor(108898)
            skillCommanderBonus = DynAccessor(108899)
            skillConcealment = DynAccessor(108900)
            skillControlledImpact = DynAccessor(108901)
            skillDeadEye = DynAccessor(108902)
            skillDesignatedTarget = DynAccessor(108903)
            skillEagleEye = DynAccessor(108904)
            skillExpert = DynAccessor(108905)
            skillFirefighting = DynAccessor(108906)
            skillIntuition = DynAccessor(108907)
            skillJackOfAllTrades = DynAccessor(108908)
            skillMentor = DynAccessor(108909)
            skillOffRoadDriving = DynAccessor(108910)
            skillPreventativeMaintenance = DynAccessor(108911)
            skillRelaying = DynAccessor(108912)
            skillRepairs = DynAccessor(108913)
            skillSafeStowage = DynAccessor(108914)
            skillSignalBoosting = DynAccessor(108915)
            skillSituationalAwareness = DynAccessor(108916)
            skillSixthSense = DynAccessor(108917)
            skillSmoothRide = DynAccessor(108918)
            skillSnapShot = DynAccessor(108919)
            skillSniper = DynAccessor(108920)
            skillSoundIntelligence = DynAccessor(108921)
            statConcealment = DynAccessor(108922)
            statFirepower = DynAccessor(108923)
            statMobility = DynAccessor(108924)
            statSpotting = DynAccessor(108925)
            statSurvivability = DynAccessor(108926)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(108927)
        ay_gun = DynAccessor(108928)
        ay_tracks = DynAccessor(108929)
        ay_turret = DynAccessor(108930)
        video_reward = DynAccessor(108931)
        video_reward_min = DynAccessor(108932)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_181_0 = DynAccessor(108933)
        v_182_0 = DynAccessor(108934)
        v_183_0 = DynAccessor(108935)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(108936)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(108937)
            overcharge = DynAccessor(108938)
            power_shot = DynAccessor(108939)
            rapid_shelling = DynAccessor(108940)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(108941)
            Loop_1 = DynAccessor(108942)
            Loop_10 = DynAccessor(108943)
            Loop_2 = DynAccessor(108944)
            Loop_3 = DynAccessor(108945)
            Loop_4 = DynAccessor(108946)
            Loop_5 = DynAccessor(108947)
            Loop_6 = DynAccessor(108948)
            Loop_7 = DynAccessor(108949)
            Loop_8 = DynAccessor(108950)
            Loop_9 = DynAccessor(108951)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(108952)
        example_2 = DynAccessor(108953)
        example_3 = DynAccessor(108954)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(108955)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(108956)
            gold = DynAccessor(108957)
            silver = DynAccessor(108958)
            standart = DynAccessor(108959)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(108960)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108961)
            small = DynAccessor(108962)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108963)
            standart = DynAccessor(108964)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108965)
            standart = DynAccessor(108966)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(108967)
            standart = DynAccessor(108968)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(108969)
            mtl_1_35 = DynAccessor(108970)
            mt_drops = DynAccessor(108971)

        mt_lootbox = _mt_lootbox()

        class _ny2024(DynAccessor):
            __slots__ = ()
            china = DynAccessor(108972)
            magic = DynAccessor(108973)
            standart = DynAccessor(108974)
            ussr = DynAccessor(108975)
            xmas = DynAccessor(108976)

        ny2024 = _ny2024()

        class _ny2025(DynAccessor):
            __slots__ = ()
            ny_2025_big = DynAccessor(108977)
            ny_2025_small = DynAccessor(108978)
            ny_2025_tanks = DynAccessor(108979)

        ny2025 = _ny2025()

        class _ny2026(DynAccessor):
            __slots__ = ()
            ny_2026_big = DynAccessor(108980)
            ny_2026_small = DynAccessor(108981)
            ny_2026_tanks = DynAccessor(108982)

        ny2026 = _ny2026()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(108983)
            medium = DynAccessor(108984)
            small = DynAccessor(108985)
            tanks_6 = DynAccessor(108986)
            tanks_7 = DynAccessor(108987)
            tanks_8 = DynAccessor(108988)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(108989)
            G171_E77 = DynAccessor(108990)
            G171_E77_02 = DynAccessor(108991)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(108992)
            intro = DynAccessor(108993)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(108994)
            Pl35_CS_57_Sokol = DynAccessor(108995)

        mtl_universal = _mtl_universal()

        class _ny_2026_big(DynAccessor):
            __slots__ = ()
            A165_XM57 = DynAccessor(108996)
            A175_OTAC_MT_58 = DynAccessor(108997)
            A175_OTAC_MT_58_02 = DynAccessor(108998)
            customizations_28748 = DynAccessor(108999)
            customizations_77132 = DynAccessor(109000)
            customizations_8046924 = DynAccessor(109001)
            customizations_8047180 = DynAccessor(109002)
            customizations_8054092 = DynAccessor(109003)
            Cz39_SD_122_49_Sekera = DynAccessor(109004)
            F118_Char_Mle_75 = DynAccessor(109005)
            G181_StuG_Maus_17cm = DynAccessor(109006)
            G196_E_75_Ausf_B_Doppel = DynAccessor(109007)
            GB139_Vulcan = DynAccessor(109008)
            intro = DynAccessor(109009)
            It33_Orso = DynAccessor(109010)
            ny_2026_tanks = DynAccessor(109011)
            R165_Object_703_II_100 = DynAccessor(109012)
            R222_Object_120_Taran = DynAccessor(109013)
            R223_T_54B_1958 = DynAccessor(109014)
            R228_Duplet = DynAccessor(109015)

        ny_2026_big = _ny_2026_big()

        class _ny_2026_tanks(DynAccessor):
            __slots__ = ()
            Cz14_Skoda_T_56 = DynAccessor(109016)
            F106_Panhard_EBR_75_Mle1954 = DynAccessor(109017)
            F116_Bat_Chatillon_Bourrasque = DynAccessor(109018)
            F97_ELC_EVEN_90 = DynAccessor(109019)
            GB99_Turtle_Mk1 = DynAccessor(109020)
            It13_Progetto_M35_mod_46 = DynAccessor(109021)

        ny_2026_tanks = _ny_2026_tanks()

    lootbox_reward_video = _lootbox_reward_video()

    class _new_year(DynAccessor):
        __slots__ = ()

        class _greetings(DynAccessor):
            __slots__ = ()
            ng_greetings = DynAccessor(109022)

        greetings = _greetings()

        class _lootbox(DynAccessor):
            __slots__ = ()
            box_delivery = DynAccessor(109023)

        lootbox = _lootbox()

        class _onboarding(DynAccessor):
            __slots__ = ()
            onboarding_day = DynAccessor(109024)
            onboarding_night = DynAccessor(109025)

        onboarding = _onboarding()

        class _pet(DynAccessor):
            __slots__ = ()
            letter = DynAccessor(109026)
            pet_story = DynAccessor(109027)

        pet = _pet()

        class _robotTvScreen(DynAccessor):
            __slots__ = ()
            tv_screen_active = DynAccessor(109028)
            tv_screen_idle = DynAccessor(109029)

        robotTvScreen = _robotTvScreen()

    new_year = _new_year()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(109030)
        operation_10 = DynAccessor(109031)
        operation_8 = DynAccessor(109032)
        operation_9 = DynAccessor(109033)
        operation_99 = DynAccessor(109034)
        video_operations_person = DynAccessor(109035)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(109036)

    platoon = _platoon()