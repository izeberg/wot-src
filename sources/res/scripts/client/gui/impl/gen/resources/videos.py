from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(117470)
    _tutorialInitialLoop = DynAccessor(117471)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(117472)
        up_particles = DynAccessor(117473)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(117474)
            crewCommander = DynAccessor(117475)
            crewDriver = DynAccessor(117476)
            crewGunner = DynAccessor(117477)
            crewLoader = DynAccessor(117478)
            crewRadioOperator = DynAccessor(117479)
            skillAdrenalineRush = DynAccessor(117480)
            skillArmorer = DynAccessor(117481)
            skillArtLamp = DynAccessor(117482)
            skillBrothersInArms = DynAccessor(117483)
            skillCallForVengeance = DynAccessor(117484)
            skillClutchBraking = DynAccessor(117485)
            skillCommanderBonus = DynAccessor(117486)
            skillConcealment = DynAccessor(117487)
            skillControlledImpact = DynAccessor(117488)
            skillDeadEye = DynAccessor(117489)
            skillDesignatedTarget = DynAccessor(117490)
            skillEagleEye = DynAccessor(117491)
            skillExpert = DynAccessor(117492)
            skillFirefighting = DynAccessor(117493)
            skillIntuition = DynAccessor(117494)
            skillJackOfAllTrades = DynAccessor(117495)
            skillMentor = DynAccessor(117496)
            skillOffRoadDriving = DynAccessor(117497)
            skillPreventativeMaintenance = DynAccessor(117498)
            skillRelaying = DynAccessor(117499)
            skillRepairs = DynAccessor(117500)
            skillSafeStowage = DynAccessor(117501)
            skillSignalBoosting = DynAccessor(117502)
            skillSituationalAwareness = DynAccessor(117503)
            skillSixthSense = DynAccessor(117504)
            skillSmoothRide = DynAccessor(117505)
            skillSnapShot = DynAccessor(117506)
            skillSniper = DynAccessor(117507)
            skillSoundIntelligence = DynAccessor(117508)
            statConcealment = DynAccessor(117509)
            statFirepower = DynAccessor(117510)
            statMobility = DynAccessor(117511)
            statSpotting = DynAccessor(117512)
            statSurvivability = DynAccessor(117513)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(117514)
        ay_gun = DynAccessor(117515)
        ay_tracks = DynAccessor(117516)
        ay_turret = DynAccessor(117517)
        video_reward = DynAccessor(117518)
        video_reward_min = DynAccessor(117519)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmoTypeAvailable = DynAccessor(117520)
        AmmunitionCrit = DynAccessor(117521)
        FueltankCrit = DynAccessor(117522)
        InSafetyWhileNotObserved = DynAccessor(117523)
        KilledWhileObserved = DynAccessor(117524)
        ModuleDamage = DynAccessor(117525)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_211_0 = DynAccessor(117526)
        v_212_0 = DynAccessor(117527)
        v_213_0 = DynAccessor(117528)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(117529)
        Intro = DynAccessor(117530)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(117531)
            overcharge = DynAccessor(117532)
            power_shot = DynAccessor(117533)
            teleport = DynAccessor(117534)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(117535)

        progression = _progression()

    cosmic = _cosmic()

    class _customizationResource(DynAccessor):
        __slots__ = ()
        cr_paint_reward = DynAccessor(117536)

    customizationResource = _customizationResource()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(117537)
        cosmic_intro_vp8_8_256 = DynAccessor(117538)
        cosmic_intro_vp8_8_96 = DynAccessor(117539)
        cosmic_intro_vp9_8_128 = DynAccessor(117540)
        cosmic_intro_vp9_8_256 = DynAccessor(117541)
        cosmic_intro_vp9_8_96 = DynAccessor(117542)
        example = DynAccessor(117543)
        example_2 = DynAccessor(117544)
        example_3 = DynAccessor(117545)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(117546)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(117547)
            gold = DynAccessor(117548)
            silver = DynAccessor(117549)
            standart = DynAccessor(117550)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(117551)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(117552)
            small = DynAccessor(117553)

        bd2025 = _bd2025()

        class _bd2026(DynAccessor):
            __slots__ = ()
            large = DynAccessor(117554)
            small = DynAccessor(117555)

        bd2026 = _bd2026()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117556)
            standart = DynAccessor(117557)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117558)
            standart = DynAccessor(117559)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117560)
            standart = DynAccessor(117561)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117562)
            standart = DynAccessor(117563)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(117564)
            mtl_1_35 = DynAccessor(117565)
            mtl_1_43 = DynAccessor(117566)
            mt_drops = DynAccessor(117567)

        mt_lootbox = _mt_lootbox()

        class _ny2027(DynAccessor):
            __slots__ = ()
            ny_2027_big = DynAccessor(117568)
            ny_2027_small = DynAccessor(117569)
            ny_2027_tanks = DynAccessor(117570)

        ny2027 = _ny2027()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(117571)
            medium = DynAccessor(117572)
            small = DynAccessor(117573)
            tanks_6 = DynAccessor(117574)
            tanks_7 = DynAccessor(117575)
            tanks_8 = DynAccessor(117576)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(117577)
            R149_Object_268_4_02 = DynAccessor(117578)
            R177_ISU_152K_BL10_02 = DynAccessor(117579)
            R248_T44_Storm = DynAccessor(117580)
            R45_IS_7_02 = DynAccessor(117581)
            Un24_Vz_68_2_Britva = DynAccessor(117582)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(117583)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(117584)
            intro = DynAccessor(117585)
            R239_ST_Molot_02 = DynAccessor(117586)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(117587)
            GB141_Celestial_2_51 = DynAccessor(117588)
            intro = DynAccessor(117589)
            R239_ST_Molot = DynAccessor(117590)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(117591)
            Ch46_113_140 = DynAccessor(117592)
            G164_Kpz_Pr_68_P = DynAccessor(117593)
            Pl35_CS_57_Sokol = DynAccessor(117594)
            R121_KV4_KTT = DynAccessor(117595)
            S22_Strv_S1 = DynAccessor(117596)

        mtl_universal = _mtl_universal()

        class _ny_2027_big(DynAccessor):
            __slots__ = ()
            A165_XM57 = DynAccessor(117597)
            A175_OTAC_MT_58 = DynAccessor(117598)
            A175_OTAC_MT_58_02 = DynAccessor(117599)
            customizations_177484 = DynAccessor(117600)
            customizations_7990860 = DynAccessor(117601)
            customizations_7999308 = DynAccessor(117602)
            customizations_7999564 = DynAccessor(117603)
            customizations_8001356 = DynAccessor(117604)
            customizations_8001612 = DynAccessor(117605)
            Cz39_SD_122_49_Sekera = DynAccessor(117606)
            F118_Char_Mle_75 = DynAccessor(117607)
            G181_StuG_Maus_17cm = DynAccessor(117608)
            G196_E_75_Ausf_B_Doppel = DynAccessor(117609)
            GB139_Vulcan = DynAccessor(117610)
            intro = DynAccessor(117611)
            It33_Orso = DynAccessor(117612)
            ny_2027_tanks = DynAccessor(117613)
            R165_Object_703_II_100 = DynAccessor(117614)
            R222_Object_120_Taran = DynAccessor(117615)
            R223_T_54B_1958 = DynAccessor(117616)
            R228_Duplet = DynAccessor(117617)

        ny_2027_big = _ny_2027_big()

        class _ny_2027_tanks(DynAccessor):
            __slots__ = ()
            A115_Chrysler_K = DynAccessor(117618)
            A117_T26E5 = DynAccessor(117619)
            A124_T54E2 = DynAccessor(117620)
            A136_T42 = DynAccessor(117621)
            A140_ASTRON_REX_105mm = DynAccessor(117622)
            G120_M41_90 = DynAccessor(117623)
            G138_VK168_02 = DynAccessor(117624)
            G44_JagdTigerH = DynAccessor(117625)
            GB115_Gonsalo = DynAccessor(117626)
            GB121_GSOR_1010_FB = DynAccessor(117627)
            GB87_Chieftain_T95_turret = DynAccessor(117628)
            It18_Progetto_C45_mod_71 = DynAccessor(117629)
            Pl08_50TP_prototyp = DynAccessor(117630)
            R134_Object_252U = DynAccessor(117631)
            R146_STG = DynAccessor(117632)
            R188_Object_259A = DynAccessor(117633)
            S25_EMIL_51 = DynAccessor(117634)
            S26_Lansen_C = DynAccessor(117635)

        ny_2027_tanks = _ny_2027_tanks()

    lootbox_reward_video = _lootbox_reward_video()

    class _mt_birthday(DynAccessor):
        __slots__ = ()

        class _tankMail(DynAccessor):
            __slots__ = ()
            sentGift = DynAccessor(117636)

        tankMail = _tankMail()

    mt_birthday = _mt_birthday()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(117637)
        option_2 = DynAccessor(117638)
        option_3 = DynAccessor(117639)

    newbie_start_page = _newbie_start_page()

    class _new_year(DynAccessor):
        __slots__ = ()

        class _clips(DynAccessor):
            __slots__ = ()
            clip_1 = DynAccessor(117640)
            clip_2 = DynAccessor(117641)
            ldt_reward = DynAccessor(117642)

        clips = _clips()

        class _greetings(DynAccessor):
            __slots__ = ()
            lvl_greetings = DynAccessor(117643)
            ng_greetings = DynAccessor(117644)
            report_1 = DynAccessor(117645)
            report_2 = DynAccessor(117646)
            report_3 = DynAccessor(117647)
            report_4 = DynAccessor(117648)
            report_5 = DynAccessor(117649)
            report_6 = DynAccessor(117650)
            report_7 = DynAccessor(117651)

        greetings = _greetings()

        class _lootbox(DynAccessor):
            __slots__ = ()
            box_delivery = DynAccessor(117652)
            pre_delivery = DynAccessor(117653)

        lootbox = _lootbox()

        class _onboarding(DynAccessor):
            __slots__ = ()
            onboarding_day = DynAccessor(117654)
            onboarding_night = DynAccessor(117655)

        onboarding = _onboarding()

        class _petTvScreen(DynAccessor):
            __slots__ = ()
            animations = DynAccessor(117656)

        petTvScreen = _petTvScreen()

        class _robotTvScreen(DynAccessor):
            __slots__ = ()
            tv_screen_active = DynAccessor(117657)
            tv_screen_idle = DynAccessor(117658)

        robotTvScreen = _robotTvScreen()

    new_year = _new_year()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(117659)
        Ch57_BZT_70 = DynAccessor(117660)
        F134_ARL_Projet_F = DynAccessor(117661)
        G184_EisBaer = DynAccessor(117662)
        GB140_Champion = DynAccessor(117663)
        R124_Object_279 = DynAccessor(117664)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(117665)
        operation_10 = DynAccessor(117666)
        operation_8 = DynAccessor(117667)
        operation_9 = DynAccessor(117668)
        operation_99 = DynAccessor(117669)
        video_operations_person = DynAccessor(117670)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(117671)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(117672)

    vehicle = _vehicle()