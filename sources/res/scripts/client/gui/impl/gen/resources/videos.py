from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(113852)
    _tutorialInitialLoop = DynAccessor(113853)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(113854)
        up_particles = DynAccessor(113855)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(113856)
            crewCommander = DynAccessor(113857)
            crewDriver = DynAccessor(113858)
            crewGunner = DynAccessor(113859)
            crewLoader = DynAccessor(113860)
            crewRadioOperator = DynAccessor(113861)
            skillAdrenalineRush = DynAccessor(113862)
            skillArmorer = DynAccessor(113863)
            skillArtLamp = DynAccessor(113864)
            skillBrothersInArms = DynAccessor(113865)
            skillCallForVengeance = DynAccessor(113866)
            skillClutchBraking = DynAccessor(113867)
            skillCommanderBonus = DynAccessor(113868)
            skillConcealment = DynAccessor(113869)
            skillControlledImpact = DynAccessor(113870)
            skillDeadEye = DynAccessor(113871)
            skillDesignatedTarget = DynAccessor(113872)
            skillEagleEye = DynAccessor(113873)
            skillExpert = DynAccessor(113874)
            skillFirefighting = DynAccessor(113875)
            skillIntuition = DynAccessor(113876)
            skillJackOfAllTrades = DynAccessor(113877)
            skillMentor = DynAccessor(113878)
            skillOffRoadDriving = DynAccessor(113879)
            skillPreventativeMaintenance = DynAccessor(113880)
            skillRelaying = DynAccessor(113881)
            skillRepairs = DynAccessor(113882)
            skillSafeStowage = DynAccessor(113883)
            skillSignalBoosting = DynAccessor(113884)
            skillSituationalAwareness = DynAccessor(113885)
            skillSixthSense = DynAccessor(113886)
            skillSmoothRide = DynAccessor(113887)
            skillSnapShot = DynAccessor(113888)
            skillSniper = DynAccessor(113889)
            skillSoundIntelligence = DynAccessor(113890)
            statConcealment = DynAccessor(113891)
            statFirepower = DynAccessor(113892)
            statMobility = DynAccessor(113893)
            statSpotting = DynAccessor(113894)
            statSurvivability = DynAccessor(113895)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(113896)
        ay_gun = DynAccessor(113897)
        ay_tracks = DynAccessor(113898)
        ay_turret = DynAccessor(113899)
        video_reward = DynAccessor(113900)
        video_reward_min = DynAccessor(113901)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmoTypeAvailable = DynAccessor(113902)
        AmmunitionCrit = DynAccessor(113903)
        FueltankCrit = DynAccessor(113904)
        InSafetyWhileNotObserved = DynAccessor(113905)
        KilledWhileObserved = DynAccessor(113906)
        ModuleDamage = DynAccessor(113907)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_211_0 = DynAccessor(113908)
        v_212_0 = DynAccessor(113909)
        v_213_0 = DynAccessor(113910)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(113911)
        Intro = DynAccessor(113912)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(113913)
            overcharge = DynAccessor(113914)
            power_shot = DynAccessor(113915)
            teleport = DynAccessor(113916)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(113917)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(113918)
        cosmic_intro_vp8_8_256 = DynAccessor(113919)
        cosmic_intro_vp8_8_96 = DynAccessor(113920)
        cosmic_intro_vp9_8_128 = DynAccessor(113921)
        cosmic_intro_vp9_8_256 = DynAccessor(113922)
        cosmic_intro_vp9_8_96 = DynAccessor(113923)
        example = DynAccessor(113924)
        example_2 = DynAccessor(113925)
        example_3 = DynAccessor(113926)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(113927)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(113928)
            gold = DynAccessor(113929)
            silver = DynAccessor(113930)
            standart = DynAccessor(113931)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(113932)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(113933)
            small = DynAccessor(113934)

        bd2025 = _bd2025()

        class _bd2026(DynAccessor):
            __slots__ = ()
            large = DynAccessor(113935)
            small = DynAccessor(113936)

        bd2026 = _bd2026()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(113937)
            standart = DynAccessor(113938)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(113939)
            standart = DynAccessor(113940)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(113941)
            standart = DynAccessor(113942)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(113943)
            standart = DynAccessor(113944)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(113945)
            mtl_1_35 = DynAccessor(113946)
            mtl_1_43 = DynAccessor(113947)
            mt_drops = DynAccessor(113948)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(113949)
            medium = DynAccessor(113950)
            small = DynAccessor(113951)
            tanks_6 = DynAccessor(113952)
            tanks_7 = DynAccessor(113953)
            tanks_8 = DynAccessor(113954)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(113955)
            R149_Object_268_4_02 = DynAccessor(113956)
            R177_ISU_152K_BL10_02 = DynAccessor(113957)
            R248_T44_Storm = DynAccessor(113958)
            R45_IS_7_02 = DynAccessor(113959)
            Un24_Vz_68_2_Britva = DynAccessor(113960)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(113961)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(113962)
            intro = DynAccessor(113963)
            R239_ST_Molot_02 = DynAccessor(113964)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(113965)
            GB141_Celestial_2_51 = DynAccessor(113966)
            intro = DynAccessor(113967)
            R239_ST_Molot = DynAccessor(113968)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(113969)
            Ch46_113_140 = DynAccessor(113970)
            G164_Kpz_Pr_68_P = DynAccessor(113971)
            Pl35_CS_57_Sokol = DynAccessor(113972)
            R121_KV4_KTT = DynAccessor(113973)
            S22_Strv_S1 = DynAccessor(113974)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _mt_birthday(DynAccessor):
        __slots__ = ()

        class _tankMail(DynAccessor):
            __slots__ = ()
            sentGift = DynAccessor(113975)

        tankMail = _tankMail()

    mt_birthday = _mt_birthday()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(113976)
        option_2 = DynAccessor(113977)
        option_3 = DynAccessor(113978)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(113979)
        Ch57_BZT_70 = DynAccessor(113980)
        F134_ARL_Projet_F = DynAccessor(113981)
        G184_EisBaer = DynAccessor(113982)
        GB140_Champion = DynAccessor(113983)
        R124_Object_279 = DynAccessor(113984)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(113985)
        operation_10 = DynAccessor(113986)
        operation_8 = DynAccessor(113987)
        operation_9 = DynAccessor(113988)
        operation_99 = DynAccessor(113989)
        video_operations_person = DynAccessor(113990)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(113991)

    platoon = _platoon()

    class _portal(DynAccessor):
        __slots__ = ()
        portal_intro = DynAccessor(113992)
        portal_outro = DynAccessor(113993)
        portal_transition = DynAccessor(113994)

        class _abilities(DynAccessor):
            __slots__ = ()
            berserk_portal = DynAccessor(113995)
            curse_shot_portal = DynAccessor(113996)
            fire_shot_portal = DynAccessor(113997)
            frozen_shot_portal = DynAccessor(113998)
            guided_missile_portal = DynAccessor(113999)
            laugh_shot_portal = DynAccessor(114000)
            minefield_portal = DynAccessor(114001)
            reload_aura_portal = DynAccessor(114002)
            sentry_gun_portal = DynAccessor(114003)
            shield_portal = DynAccessor(114004)
            trap_portal = DynAccessor(114005)
            vehicle_change_shot_portal = DynAccessor(114006)

        abilities = _abilities()

    portal = _portal()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(114007)

    vehicle = _vehicle()