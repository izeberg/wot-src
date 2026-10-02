from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(113851)
    _tutorialInitialLoop = DynAccessor(113852)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(113853)
        up_particles = DynAccessor(113854)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(113855)
            crewCommander = DynAccessor(113856)
            crewDriver = DynAccessor(113857)
            crewGunner = DynAccessor(113858)
            crewLoader = DynAccessor(113859)
            crewRadioOperator = DynAccessor(113860)
            skillAdrenalineRush = DynAccessor(113861)
            skillArmorer = DynAccessor(113862)
            skillArtLamp = DynAccessor(113863)
            skillBrothersInArms = DynAccessor(113864)
            skillCallForVengeance = DynAccessor(113865)
            skillClutchBraking = DynAccessor(113866)
            skillCommanderBonus = DynAccessor(113867)
            skillConcealment = DynAccessor(113868)
            skillControlledImpact = DynAccessor(113869)
            skillDeadEye = DynAccessor(113870)
            skillDesignatedTarget = DynAccessor(113871)
            skillEagleEye = DynAccessor(113872)
            skillExpert = DynAccessor(113873)
            skillFirefighting = DynAccessor(113874)
            skillIntuition = DynAccessor(113875)
            skillJackOfAllTrades = DynAccessor(113876)
            skillMentor = DynAccessor(113877)
            skillOffRoadDriving = DynAccessor(113878)
            skillPreventativeMaintenance = DynAccessor(113879)
            skillRelaying = DynAccessor(113880)
            skillRepairs = DynAccessor(113881)
            skillSafeStowage = DynAccessor(113882)
            skillSignalBoosting = DynAccessor(113883)
            skillSituationalAwareness = DynAccessor(113884)
            skillSixthSense = DynAccessor(113885)
            skillSmoothRide = DynAccessor(113886)
            skillSnapShot = DynAccessor(113887)
            skillSniper = DynAccessor(113888)
            skillSoundIntelligence = DynAccessor(113889)
            statConcealment = DynAccessor(113890)
            statFirepower = DynAccessor(113891)
            statMobility = DynAccessor(113892)
            statSpotting = DynAccessor(113893)
            statSurvivability = DynAccessor(113894)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(113895)
        ay_gun = DynAccessor(113896)
        ay_tracks = DynAccessor(113897)
        ay_turret = DynAccessor(113898)
        video_reward = DynAccessor(113899)
        video_reward_min = DynAccessor(113900)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmoTypeAvailable = DynAccessor(113901)
        AmmunitionCrit = DynAccessor(113902)
        FueltankCrit = DynAccessor(113903)
        InSafetyWhileNotObserved = DynAccessor(113904)
        KilledWhileObserved = DynAccessor(113905)
        ModuleDamage = DynAccessor(113906)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_211_0 = DynAccessor(113907)
        v_212_0 = DynAccessor(113908)
        v_213_0 = DynAccessor(113909)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(113910)
        Intro = DynAccessor(113911)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(113912)
            overcharge = DynAccessor(113913)
            power_shot = DynAccessor(113914)
            teleport = DynAccessor(113915)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(113916)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(113917)
        cosmic_intro_vp8_8_256 = DynAccessor(113918)
        cosmic_intro_vp8_8_96 = DynAccessor(113919)
        cosmic_intro_vp9_8_128 = DynAccessor(113920)
        cosmic_intro_vp9_8_256 = DynAccessor(113921)
        cosmic_intro_vp9_8_96 = DynAccessor(113922)
        example = DynAccessor(113923)
        example_2 = DynAccessor(113924)
        example_3 = DynAccessor(113925)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(113926)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(113927)
            gold = DynAccessor(113928)
            silver = DynAccessor(113929)
            standart = DynAccessor(113930)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(113931)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(113932)
            small = DynAccessor(113933)

        bd2025 = _bd2025()

        class _bd2026(DynAccessor):
            __slots__ = ()
            large = DynAccessor(113934)
            small = DynAccessor(113935)

        bd2026 = _bd2026()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(113936)
            standart = DynAccessor(113937)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(113938)
            standart = DynAccessor(113939)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(113940)
            standart = DynAccessor(113941)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(113942)
            standart = DynAccessor(113943)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(113944)
            mtl_1_35 = DynAccessor(113945)
            mtl_1_43 = DynAccessor(113946)
            mt_drops = DynAccessor(113947)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(113948)
            medium = DynAccessor(113949)
            small = DynAccessor(113950)
            tanks_6 = DynAccessor(113951)
            tanks_7 = DynAccessor(113952)
            tanks_8 = DynAccessor(113953)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(113954)
            R149_Object_268_4_02 = DynAccessor(113955)
            R177_ISU_152K_BL10_02 = DynAccessor(113956)
            R248_T44_Storm = DynAccessor(113957)
            R45_IS_7_02 = DynAccessor(113958)
            Un24_Vz_68_2_Britva = DynAccessor(113959)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(113960)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(113961)
            intro = DynAccessor(113962)
            R239_ST_Molot_02 = DynAccessor(113963)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(113964)
            GB141_Celestial_2_51 = DynAccessor(113965)
            intro = DynAccessor(113966)
            R239_ST_Molot = DynAccessor(113967)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(113968)
            Ch46_113_140 = DynAccessor(113969)
            G164_Kpz_Pr_68_P = DynAccessor(113970)
            Pl35_CS_57_Sokol = DynAccessor(113971)
            R121_KV4_KTT = DynAccessor(113972)
            S22_Strv_S1 = DynAccessor(113973)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _mt_birthday(DynAccessor):
        __slots__ = ()

        class _tankMail(DynAccessor):
            __slots__ = ()
            sentGift = DynAccessor(113974)

        tankMail = _tankMail()

    mt_birthday = _mt_birthday()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(113975)
        option_2 = DynAccessor(113976)
        option_3 = DynAccessor(113977)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(113978)
        Ch57_BZT_70 = DynAccessor(113979)
        F134_ARL_Projet_F = DynAccessor(113980)
        G184_EisBaer = DynAccessor(113981)
        GB140_Champion = DynAccessor(113982)
        R124_Object_279 = DynAccessor(113983)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(113984)
        operation_10 = DynAccessor(113985)
        operation_8 = DynAccessor(113986)
        operation_9 = DynAccessor(113987)
        operation_99 = DynAccessor(113988)
        video_operations_person = DynAccessor(113989)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(113990)

    platoon = _platoon()

    class _portal(DynAccessor):
        __slots__ = ()
        portal_intro = DynAccessor(113991)
        portal_outro = DynAccessor(113992)
        portal_transition = DynAccessor(113993)

        class _abilities(DynAccessor):
            __slots__ = ()
            berserk_portal = DynAccessor(113994)
            curse_shot_portal = DynAccessor(113995)
            fire_shot_portal = DynAccessor(113996)
            frozen_shot_portal = DynAccessor(113997)
            guided_missile_portal = DynAccessor(113998)
            laugh_shot_portal = DynAccessor(113999)
            minefield_portal = DynAccessor(114000)
            reload_aura_portal = DynAccessor(114001)
            sentry_gun_portal = DynAccessor(114002)
            shield_portal = DynAccessor(114003)
            trap_portal = DynAccessor(114004)
            vehicle_change_shot_portal = DynAccessor(114005)

        abilities = _abilities()

    portal = _portal()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(114006)

    vehicle = _vehicle()