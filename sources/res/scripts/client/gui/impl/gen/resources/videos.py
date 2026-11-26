from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(117530)
    _tutorialInitialLoop = DynAccessor(117531)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(117532)
        up_particles = DynAccessor(117533)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(117534)
            crewCommander = DynAccessor(117535)
            crewDriver = DynAccessor(117536)
            crewGunner = DynAccessor(117537)
            crewLoader = DynAccessor(117538)
            crewRadioOperator = DynAccessor(117539)
            skillAdrenalineRush = DynAccessor(117540)
            skillArmorer = DynAccessor(117541)
            skillArtLamp = DynAccessor(117542)
            skillBrothersInArms = DynAccessor(117543)
            skillCallForVengeance = DynAccessor(117544)
            skillClutchBraking = DynAccessor(117545)
            skillCommanderBonus = DynAccessor(117546)
            skillConcealment = DynAccessor(117547)
            skillControlledImpact = DynAccessor(117548)
            skillDeadEye = DynAccessor(117549)
            skillDesignatedTarget = DynAccessor(117550)
            skillEagleEye = DynAccessor(117551)
            skillExpert = DynAccessor(117552)
            skillFirefighting = DynAccessor(117553)
            skillIntuition = DynAccessor(117554)
            skillJackOfAllTrades = DynAccessor(117555)
            skillMentor = DynAccessor(117556)
            skillOffRoadDriving = DynAccessor(117557)
            skillPreventativeMaintenance = DynAccessor(117558)
            skillRelaying = DynAccessor(117559)
            skillRepairs = DynAccessor(117560)
            skillSafeStowage = DynAccessor(117561)
            skillSignalBoosting = DynAccessor(117562)
            skillSituationalAwareness = DynAccessor(117563)
            skillSixthSense = DynAccessor(117564)
            skillSmoothRide = DynAccessor(117565)
            skillSnapShot = DynAccessor(117566)
            skillSniper = DynAccessor(117567)
            skillSoundIntelligence = DynAccessor(117568)
            statConcealment = DynAccessor(117569)
            statFirepower = DynAccessor(117570)
            statMobility = DynAccessor(117571)
            statSpotting = DynAccessor(117572)
            statSurvivability = DynAccessor(117573)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(117574)
        ay_gun = DynAccessor(117575)
        ay_tracks = DynAccessor(117576)
        ay_turret = DynAccessor(117577)
        video_reward = DynAccessor(117578)
        video_reward_min = DynAccessor(117579)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmoTypeAvailable = DynAccessor(117580)
        AmmunitionCrit = DynAccessor(117581)
        FueltankCrit = DynAccessor(117582)
        InSafetyWhileNotObserved = DynAccessor(117583)
        KilledWhileObserved = DynAccessor(117584)
        ModuleDamage = DynAccessor(117585)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_211_0 = DynAccessor(117586)
        v_212_0 = DynAccessor(117587)
        v_213_0 = DynAccessor(117588)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(117589)
        Intro = DynAccessor(117590)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(117591)
            overcharge = DynAccessor(117592)
            power_shot = DynAccessor(117593)
            teleport = DynAccessor(117594)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(117595)

        progression = _progression()

    cosmic = _cosmic()

    class _customizationResource(DynAccessor):
        __slots__ = ()
        cr_paint_reward = DynAccessor(117596)

    customizationResource = _customizationResource()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(117597)
        cosmic_intro_vp8_8_256 = DynAccessor(117598)
        cosmic_intro_vp8_8_96 = DynAccessor(117599)
        cosmic_intro_vp9_8_128 = DynAccessor(117600)
        cosmic_intro_vp9_8_256 = DynAccessor(117601)
        cosmic_intro_vp9_8_96 = DynAccessor(117602)
        example = DynAccessor(117603)
        example_2 = DynAccessor(117604)
        example_3 = DynAccessor(117605)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(117606)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(117607)
            gold = DynAccessor(117608)
            silver = DynAccessor(117609)
            standart = DynAccessor(117610)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(117611)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(117612)
            small = DynAccessor(117613)

        bd2025 = _bd2025()

        class _bd2026(DynAccessor):
            __slots__ = ()
            large = DynAccessor(117614)
            small = DynAccessor(117615)

        bd2026 = _bd2026()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117616)
            standart = DynAccessor(117617)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117618)
            standart = DynAccessor(117619)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117620)
            standart = DynAccessor(117621)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117622)
            standart = DynAccessor(117623)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(117624)
            mtl_1_35 = DynAccessor(117625)
            mtl_1_43 = DynAccessor(117626)
            mt_drops = DynAccessor(117627)

        mt_lootbox = _mt_lootbox()

        class _ny2027(DynAccessor):
            __slots__ = ()
            ny_2027_big = DynAccessor(117628)
            ny_2027_small = DynAccessor(117629)
            ny_2027_tanks = DynAccessor(117630)

        ny2027 = _ny2027()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(117631)
            medium = DynAccessor(117632)
            small = DynAccessor(117633)
            tanks_6 = DynAccessor(117634)
            tanks_7 = DynAccessor(117635)
            tanks_8 = DynAccessor(117636)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(117637)
            R149_Object_268_4_02 = DynAccessor(117638)
            R177_ISU_152K_BL10_02 = DynAccessor(117639)
            R248_T44_Storm = DynAccessor(117640)
            R45_IS_7_02 = DynAccessor(117641)
            Un24_Vz_68_2_Britva = DynAccessor(117642)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(117643)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(117644)
            intro = DynAccessor(117645)
            R239_ST_Molot_02 = DynAccessor(117646)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(117647)
            GB141_Celestial_2_51 = DynAccessor(117648)
            intro = DynAccessor(117649)
            R239_ST_Molot = DynAccessor(117650)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(117651)
            Ch46_113_140 = DynAccessor(117652)
            G164_Kpz_Pr_68_P = DynAccessor(117653)
            Pl35_CS_57_Sokol = DynAccessor(117654)
            R121_KV4_KTT = DynAccessor(117655)
            S22_Strv_S1 = DynAccessor(117656)

        mtl_universal = _mtl_universal()

        class _ny_2027_big(DynAccessor):
            __slots__ = ()
            A151_TS_60 = DynAccessor(117657)
            A162_ATAC_II = DynAccessor(117658)
            A180_ACIT_40t_Concept = DynAccessor(117659)
            Ch41_WZ_111_QL = DynAccessor(117660)
            Ch75_ZTQ_56 = DynAccessor(117661)
            customizations_24908 = DynAccessor(117662)
            customizations_25676 = DynAccessor(117663)
            customizations_25932 = DynAccessor(117664)
            customizations_8095308 = DynAccessor(117665)
            customizations_8098892 = DynAccessor(117666)
            customizations_8101452 = DynAccessor(117667)
            G180_Hauptpanzer_Gruppe_A = DynAccessor(117668)
            intro = DynAccessor(117669)
            It37_CAS_149 = DynAccessor(117670)
            J51_Naginata = DynAccessor(117671)
            ny_2027_tanks = DynAccessor(117672)
            R147_Object_701 = DynAccessor(117673)
            R247_Object_440 = DynAccessor(117674)
            R250_NST_130 = DynAccessor(117675)
            R250_NST_130_03 = DynAccessor(117676)
            S43_Armborst = DynAccessor(117677)

        ny_2027_big = _ny_2027_big()

        class _ny_2027_tanks(DynAccessor):
            __slots__ = ()
            A163_H_3 = DynAccessor(117678)
            Ch25_121_mod_1971B_MK = DynAccessor(117679)
            Ch40_WZ120G_FT = DynAccessor(117680)
            Ch56_BZ_74_1 = DynAccessor(117681)
            Cz39_SD_122_49_Sekera = DynAccessor(117682)
            F129_Schneider_120_AC_Gendarme = DynAccessor(117683)
            F133_Projet_57 = DynAccessor(117684)
            G181_StuG_Maus_17cm = DynAccessor(117685)
            G196_E_75_Ausf_B_Doppel = DynAccessor(117686)
            G98_Waffentrager_E100 = DynAccessor(117687)
            GB139_Vulcan = DynAccessor(117688)
            GB99_Turtle_Mk1 = DynAccessor(117689)
            It32_Prototipo_6 = DynAccessor(117690)
            Pl26_Czolg_P_Wz_46 = DynAccessor(117691)
            R165_Object_703_II = DynAccessor(117692)
            R173_K_91_2_122 = DynAccessor(117693)
            R222_Object_120_Taran = DynAccessor(117694)
            R228_Duplet = DynAccessor(117695)

        ny_2027_tanks = _ny_2027_tanks()

        class _ny_2027_tanks_test(DynAccessor):
            __slots__ = ()
            A115_Chrysler_K = DynAccessor(117696)
            A117_T26E5 = DynAccessor(117697)
            A124_T54E2 = DynAccessor(117698)
            A136_T42 = DynAccessor(117699)
            A140_ASTRON_REX_105mm = DynAccessor(117700)
            G120_M41_90 = DynAccessor(117701)
            G138_VK168_02 = DynAccessor(117702)
            G44_JagdTigerH = DynAccessor(117703)
            GB115_Gonsalo = DynAccessor(117704)
            GB121_GSOR_1010_FB = DynAccessor(117705)
            GB87_Chieftain_T95_turret = DynAccessor(117706)
            It18_Progetto_C45_mod_71 = DynAccessor(117707)
            Pl08_50TP_prototyp = DynAccessor(117708)
            R134_Object_252U = DynAccessor(117709)
            R146_STG = DynAccessor(117710)
            R188_Object_259A = DynAccessor(117711)
            S25_EMIL_51 = DynAccessor(117712)
            S26_Lansen_C = DynAccessor(117713)

        ny_2027_tanks_test = _ny_2027_tanks_test()

    lootbox_reward_video = _lootbox_reward_video()

    class _mt_birthday(DynAccessor):
        __slots__ = ()

        class _tankMail(DynAccessor):
            __slots__ = ()
            sentGift = DynAccessor(117714)

        tankMail = _tankMail()

    mt_birthday = _mt_birthday()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(117715)
        option_2 = DynAccessor(117716)
        option_3 = DynAccessor(117717)

    newbie_start_page = _newbie_start_page()

    class _new_year(DynAccessor):
        __slots__ = ()

        class _clips(DynAccessor):
            __slots__ = ()
            clip_1 = DynAccessor(117718)
            clip_2 = DynAccessor(117719)
            ldt_reward = DynAccessor(117720)

        clips = _clips()

        class _greetings(DynAccessor):
            __slots__ = ()
            lvl_greetings = DynAccessor(117721)
            ng_greetings = DynAccessor(117722)
            report_1 = DynAccessor(117723)
            report_2 = DynAccessor(117724)
            report_3 = DynAccessor(117725)
            report_4 = DynAccessor(117726)
            report_5 = DynAccessor(117727)
            report_6 = DynAccessor(117728)
            report_7 = DynAccessor(117729)

        greetings = _greetings()

        class _lootbox(DynAccessor):
            __slots__ = ()
            box_delivery = DynAccessor(117730)
            pre_delivery = DynAccessor(117731)

        lootbox = _lootbox()

        class _onboarding(DynAccessor):
            __slots__ = ()
            onboarding_day = DynAccessor(117732)
            onboarding_night = DynAccessor(117733)

        onboarding = _onboarding()

        class _petTvScreen(DynAccessor):
            __slots__ = ()
            animations = DynAccessor(117734)

        petTvScreen = _petTvScreen()

        class _robotTvScreen(DynAccessor):
            __slots__ = ()
            tv_screen_active = DynAccessor(117735)
            tv_screen_idle = DynAccessor(117736)

        robotTvScreen = _robotTvScreen()

    new_year = _new_year()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(117737)
        Ch57_BZT_70 = DynAccessor(117738)
        F134_ARL_Projet_F = DynAccessor(117739)
        G184_EisBaer = DynAccessor(117740)
        GB140_Champion = DynAccessor(117741)
        R124_Object_279 = DynAccessor(117742)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(117743)
        operation_10 = DynAccessor(117744)
        operation_8 = DynAccessor(117745)
        operation_9 = DynAccessor(117746)
        operation_99 = DynAccessor(117747)
        video_operations_person = DynAccessor(117748)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(117749)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(117750)

    vehicle = _vehicle()