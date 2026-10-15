from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(113721)
    _tutorialInitialLoop = DynAccessor(113722)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(113723)
        up_particles = DynAccessor(113724)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(113725)
            crewCommander = DynAccessor(113726)
            crewDriver = DynAccessor(113727)
            crewGunner = DynAccessor(113728)
            crewLoader = DynAccessor(113729)
            crewRadioOperator = DynAccessor(113730)
            skillAdrenalineRush = DynAccessor(113731)
            skillArmorer = DynAccessor(113732)
            skillArtLamp = DynAccessor(113733)
            skillBrothersInArms = DynAccessor(113734)
            skillCallForVengeance = DynAccessor(113735)
            skillClutchBraking = DynAccessor(113736)
            skillCommanderBonus = DynAccessor(113737)
            skillConcealment = DynAccessor(113738)
            skillControlledImpact = DynAccessor(113739)
            skillDeadEye = DynAccessor(113740)
            skillDesignatedTarget = DynAccessor(113741)
            skillEagleEye = DynAccessor(113742)
            skillExpert = DynAccessor(113743)
            skillFirefighting = DynAccessor(113744)
            skillIntuition = DynAccessor(113745)
            skillJackOfAllTrades = DynAccessor(113746)
            skillMentor = DynAccessor(113747)
            skillOffRoadDriving = DynAccessor(113748)
            skillPreventativeMaintenance = DynAccessor(113749)
            skillRelaying = DynAccessor(113750)
            skillRepairs = DynAccessor(113751)
            skillSafeStowage = DynAccessor(113752)
            skillSignalBoosting = DynAccessor(113753)
            skillSituationalAwareness = DynAccessor(113754)
            skillSixthSense = DynAccessor(113755)
            skillSmoothRide = DynAccessor(113756)
            skillSnapShot = DynAccessor(113757)
            skillSniper = DynAccessor(113758)
            skillSoundIntelligence = DynAccessor(113759)
            statConcealment = DynAccessor(113760)
            statFirepower = DynAccessor(113761)
            statMobility = DynAccessor(113762)
            statSpotting = DynAccessor(113763)
            statSurvivability = DynAccessor(113764)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(113765)
        ay_gun = DynAccessor(113766)
        ay_tracks = DynAccessor(113767)
        ay_turret = DynAccessor(113768)
        video_reward = DynAccessor(113769)
        video_reward_min = DynAccessor(113770)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmoTypeAvailable = DynAccessor(113771)
        AmmunitionCrit = DynAccessor(113772)
        FueltankCrit = DynAccessor(113773)
        InSafetyWhileNotObserved = DynAccessor(113774)
        KilledWhileObserved = DynAccessor(113775)
        ModuleDamage = DynAccessor(113776)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_211_0 = DynAccessor(113777)
        v_212_0 = DynAccessor(113778)
        v_213_0 = DynAccessor(113779)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(113780)
        Intro = DynAccessor(113781)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(113782)
            overcharge = DynAccessor(113783)
            power_shot = DynAccessor(113784)
            teleport = DynAccessor(113785)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(113786)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(113787)
        cosmic_intro_vp8_8_256 = DynAccessor(113788)
        cosmic_intro_vp8_8_96 = DynAccessor(113789)
        cosmic_intro_vp9_8_128 = DynAccessor(113790)
        cosmic_intro_vp9_8_256 = DynAccessor(113791)
        cosmic_intro_vp9_8_96 = DynAccessor(113792)
        example = DynAccessor(113793)
        example_2 = DynAccessor(113794)
        example_3 = DynAccessor(113795)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(113796)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(113797)
            gold = DynAccessor(113798)
            silver = DynAccessor(113799)
            standart = DynAccessor(113800)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(113801)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(113802)
            small = DynAccessor(113803)

        bd2025 = _bd2025()

        class _bd2026(DynAccessor):
            __slots__ = ()
            large = DynAccessor(113804)
            small = DynAccessor(113805)

        bd2026 = _bd2026()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(113806)
            standart = DynAccessor(113807)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(113808)
            standart = DynAccessor(113809)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(113810)
            standart = DynAccessor(113811)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(113812)
            standart = DynAccessor(113813)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(113814)
            mtl_1_35 = DynAccessor(113815)
            mtl_1_43 = DynAccessor(113816)
            mt_drops = DynAccessor(113817)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(113818)
            medium = DynAccessor(113819)
            small = DynAccessor(113820)
            tanks_6 = DynAccessor(113821)
            tanks_7 = DynAccessor(113822)
            tanks_8 = DynAccessor(113823)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(113824)
            R149_Object_268_4_02 = DynAccessor(113825)
            R177_ISU_152K_BL10_02 = DynAccessor(113826)
            R248_T44_Storm = DynAccessor(113827)
            R45_IS_7_02 = DynAccessor(113828)
            Un24_Vz_68_2_Britva = DynAccessor(113829)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(113830)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(113831)
            intro = DynAccessor(113832)
            R239_ST_Molot_02 = DynAccessor(113833)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(113834)
            GB141_Celestial_2_51 = DynAccessor(113835)
            intro = DynAccessor(113836)
            R239_ST_Molot = DynAccessor(113837)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(113838)
            Ch46_113_140 = DynAccessor(113839)
            G164_Kpz_Pr_68_P = DynAccessor(113840)
            Pl35_CS_57_Sokol = DynAccessor(113841)
            R121_KV4_KTT = DynAccessor(113842)
            S22_Strv_S1 = DynAccessor(113843)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _mt_birthday(DynAccessor):
        __slots__ = ()

        class _tankMail(DynAccessor):
            __slots__ = ()
            sentGift = DynAccessor(113844)

        tankMail = _tankMail()

    mt_birthday = _mt_birthday()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(113845)
        option_2 = DynAccessor(113846)
        option_3 = DynAccessor(113847)

    newbie_start_page = _newbie_start_page()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(113848)
        Ch57_BZT_70 = DynAccessor(113849)
        F134_ARL_Projet_F = DynAccessor(113850)
        G184_EisBaer = DynAccessor(113851)
        GB140_Champion = DynAccessor(113852)
        R124_Object_279 = DynAccessor(113853)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(113854)
        operation_10 = DynAccessor(113855)
        operation_8 = DynAccessor(113856)
        operation_9 = DynAccessor(113857)
        operation_99 = DynAccessor(113858)
        video_operations_person = DynAccessor(113859)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(113860)

    platoon = _platoon()

    class _portal(DynAccessor):
        __slots__ = ()
        portal_intro = DynAccessor(113861)
        portal_outro = DynAccessor(113862)
        portal_transition = DynAccessor(113863)

        class _abilities(DynAccessor):
            __slots__ = ()
            berserk_portal = DynAccessor(113864)
            curse_shot_portal = DynAccessor(113865)
            fire_shot_portal = DynAccessor(113866)
            frozen_shot_portal = DynAccessor(113867)
            guided_missile_portal = DynAccessor(113868)
            laugh_shot_portal = DynAccessor(113869)
            minefield_portal = DynAccessor(113870)
            reload_aura_portal = DynAccessor(113871)
            sentry_gun_portal = DynAccessor(113872)
            shield_portal = DynAccessor(113873)
            trap_portal = DynAccessor(113874)
            vehicle_change_shot_portal = DynAccessor(113875)

        abilities = _abilities()

    portal = _portal()

    class _startup(DynAccessor):
        __slots__ = ()
        c_1_46_showreel = DynAccessor(113876)

    startup = _startup()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(113877)

    vehicle = _vehicle()