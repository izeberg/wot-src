from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(117466)
    _tutorialInitialLoop = DynAccessor(117467)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(117468)
        up_particles = DynAccessor(117469)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(117470)
            crewCommander = DynAccessor(117471)
            crewDriver = DynAccessor(117472)
            crewGunner = DynAccessor(117473)
            crewLoader = DynAccessor(117474)
            crewRadioOperator = DynAccessor(117475)
            skillAdrenalineRush = DynAccessor(117476)
            skillArmorer = DynAccessor(117477)
            skillArtLamp = DynAccessor(117478)
            skillBrothersInArms = DynAccessor(117479)
            skillCallForVengeance = DynAccessor(117480)
            skillClutchBraking = DynAccessor(117481)
            skillCommanderBonus = DynAccessor(117482)
            skillConcealment = DynAccessor(117483)
            skillControlledImpact = DynAccessor(117484)
            skillDeadEye = DynAccessor(117485)
            skillDesignatedTarget = DynAccessor(117486)
            skillEagleEye = DynAccessor(117487)
            skillExpert = DynAccessor(117488)
            skillFirefighting = DynAccessor(117489)
            skillIntuition = DynAccessor(117490)
            skillJackOfAllTrades = DynAccessor(117491)
            skillMentor = DynAccessor(117492)
            skillOffRoadDriving = DynAccessor(117493)
            skillPreventativeMaintenance = DynAccessor(117494)
            skillRelaying = DynAccessor(117495)
            skillRepairs = DynAccessor(117496)
            skillSafeStowage = DynAccessor(117497)
            skillSignalBoosting = DynAccessor(117498)
            skillSituationalAwareness = DynAccessor(117499)
            skillSixthSense = DynAccessor(117500)
            skillSmoothRide = DynAccessor(117501)
            skillSnapShot = DynAccessor(117502)
            skillSniper = DynAccessor(117503)
            skillSoundIntelligence = DynAccessor(117504)
            statConcealment = DynAccessor(117505)
            statFirepower = DynAccessor(117506)
            statMobility = DynAccessor(117507)
            statSpotting = DynAccessor(117508)
            statSurvivability = DynAccessor(117509)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(117510)
        ay_gun = DynAccessor(117511)
        ay_tracks = DynAccessor(117512)
        ay_turret = DynAccessor(117513)
        video_reward = DynAccessor(117514)
        video_reward_min = DynAccessor(117515)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmoTypeAvailable = DynAccessor(117516)
        AmmunitionCrit = DynAccessor(117517)
        FueltankCrit = DynAccessor(117518)
        InSafetyWhileNotObserved = DynAccessor(117519)
        KilledWhileObserved = DynAccessor(117520)
        ModuleDamage = DynAccessor(117521)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_211_0 = DynAccessor(117522)
        v_212_0 = DynAccessor(117523)
        v_213_0 = DynAccessor(117524)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(117525)
        Intro = DynAccessor(117526)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(117527)
            overcharge = DynAccessor(117528)
            power_shot = DynAccessor(117529)
            teleport = DynAccessor(117530)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(117531)

        progression = _progression()

    cosmic = _cosmic()

    class _customizationResource(DynAccessor):
        __slots__ = ()
        cr_paint_reward = DynAccessor(117532)

    customizationResource = _customizationResource()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(117533)
        cosmic_intro_vp8_8_256 = DynAccessor(117534)
        cosmic_intro_vp8_8_96 = DynAccessor(117535)
        cosmic_intro_vp9_8_128 = DynAccessor(117536)
        cosmic_intro_vp9_8_256 = DynAccessor(117537)
        cosmic_intro_vp9_8_96 = DynAccessor(117538)
        example = DynAccessor(117539)
        example_2 = DynAccessor(117540)
        example_3 = DynAccessor(117541)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(117542)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(117543)
            gold = DynAccessor(117544)
            silver = DynAccessor(117545)
            standart = DynAccessor(117546)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(117547)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(117548)
            small = DynAccessor(117549)

        bd2025 = _bd2025()

        class _bd2026(DynAccessor):
            __slots__ = ()
            large = DynAccessor(117550)
            small = DynAccessor(117551)

        bd2026 = _bd2026()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117552)
            standart = DynAccessor(117553)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117554)
            standart = DynAccessor(117555)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117556)
            standart = DynAccessor(117557)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117558)
            standart = DynAccessor(117559)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(117560)
            mtl_1_35 = DynAccessor(117561)
            mtl_1_43 = DynAccessor(117562)
            mt_drops = DynAccessor(117563)

        mt_lootbox = _mt_lootbox()

        class _ny2027(DynAccessor):
            __slots__ = ()
            ny_2027_big = DynAccessor(117564)
            ny_2027_small = DynAccessor(117565)
            ny_2027_tanks = DynAccessor(117566)

        ny2027 = _ny2027()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(117567)
            medium = DynAccessor(117568)
            small = DynAccessor(117569)
            tanks_6 = DynAccessor(117570)
            tanks_7 = DynAccessor(117571)
            tanks_8 = DynAccessor(117572)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(117573)
            R149_Object_268_4_02 = DynAccessor(117574)
            R177_ISU_152K_BL10_02 = DynAccessor(117575)
            R248_T44_Storm = DynAccessor(117576)
            R45_IS_7_02 = DynAccessor(117577)
            Un24_Vz_68_2_Britva = DynAccessor(117578)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(117579)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(117580)
            intro = DynAccessor(117581)
            R239_ST_Molot_02 = DynAccessor(117582)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(117583)
            GB141_Celestial_2_51 = DynAccessor(117584)
            intro = DynAccessor(117585)
            R239_ST_Molot = DynAccessor(117586)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(117587)
            Ch46_113_140 = DynAccessor(117588)
            G164_Kpz_Pr_68_P = DynAccessor(117589)
            Pl35_CS_57_Sokol = DynAccessor(117590)
            R121_KV4_KTT = DynAccessor(117591)
            S22_Strv_S1 = DynAccessor(117592)

        mtl_universal = _mtl_universal()

        class _ny_2027_big(DynAccessor):
            __slots__ = ()
            A165_XM57 = DynAccessor(117593)
            A175_OTAC_MT_58 = DynAccessor(117594)
            A175_OTAC_MT_58_02 = DynAccessor(117595)
            customizations_177484 = DynAccessor(117596)
            customizations_7990860 = DynAccessor(117597)
            customizations_7999308 = DynAccessor(117598)
            customizations_7999564 = DynAccessor(117599)
            customizations_8001356 = DynAccessor(117600)
            customizations_8001612 = DynAccessor(117601)
            Cz39_SD_122_49_Sekera = DynAccessor(117602)
            F118_Char_Mle_75 = DynAccessor(117603)
            G181_StuG_Maus_17cm = DynAccessor(117604)
            G196_E_75_Ausf_B_Doppel = DynAccessor(117605)
            GB139_Vulcan = DynAccessor(117606)
            intro = DynAccessor(117607)
            It33_Orso = DynAccessor(117608)
            ny_2027_tanks = DynAccessor(117609)
            R165_Object_703_II_100 = DynAccessor(117610)
            R222_Object_120_Taran = DynAccessor(117611)
            R223_T_54B_1958 = DynAccessor(117612)
            R228_Duplet = DynAccessor(117613)

        ny_2027_big = _ny_2027_big()

        class _ny_2027_tanks(DynAccessor):
            __slots__ = ()
            A115_Chrysler_K = DynAccessor(117614)
            A117_T26E5 = DynAccessor(117615)
            A124_T54E2 = DynAccessor(117616)
            A136_T42 = DynAccessor(117617)
            A140_ASTRON_REX_105mm = DynAccessor(117618)
            G120_M41_90 = DynAccessor(117619)
            G138_VK168_02 = DynAccessor(117620)
            G44_JagdTigerH = DynAccessor(117621)
            GB115_Gonsalo = DynAccessor(117622)
            GB121_GSOR_1010_FB = DynAccessor(117623)
            GB87_Chieftain_T95_turret = DynAccessor(117624)
            It18_Progetto_C45_mod_71 = DynAccessor(117625)
            Pl08_50TP_prototyp = DynAccessor(117626)
            R134_Object_252U = DynAccessor(117627)
            R146_STG = DynAccessor(117628)
            R188_Object_259A = DynAccessor(117629)
            S25_EMIL_51 = DynAccessor(117630)
            S26_Lansen_C = DynAccessor(117631)

        ny_2027_tanks = _ny_2027_tanks()

    lootbox_reward_video = _lootbox_reward_video()

    class _mt_birthday(DynAccessor):
        __slots__ = ()

        class _tankMail(DynAccessor):
            __slots__ = ()
            sentGift = DynAccessor(117632)

        tankMail = _tankMail()

    mt_birthday = _mt_birthday()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(117633)
        option_2 = DynAccessor(117634)
        option_3 = DynAccessor(117635)

    newbie_start_page = _newbie_start_page()

    class _new_year(DynAccessor):
        __slots__ = ()

        class _clips(DynAccessor):
            __slots__ = ()
            clip_1 = DynAccessor(117636)
            clip_2 = DynAccessor(117637)
            ldt_reward = DynAccessor(117638)

        clips = _clips()

        class _greetings(DynAccessor):
            __slots__ = ()
            lvl_greetings = DynAccessor(117639)
            ng_greetings = DynAccessor(117640)
            report_1 = DynAccessor(117641)
            report_2 = DynAccessor(117642)
            report_3 = DynAccessor(117643)
            report_4 = DynAccessor(117644)
            report_5 = DynAccessor(117645)
            report_6 = DynAccessor(117646)
            report_7 = DynAccessor(117647)

        greetings = _greetings()

        class _lootbox(DynAccessor):
            __slots__ = ()
            box_delivery = DynAccessor(117648)
            pre_delivery = DynAccessor(117649)

        lootbox = _lootbox()

        class _onboarding(DynAccessor):
            __slots__ = ()
            onboarding_day = DynAccessor(117650)
            onboarding_night = DynAccessor(117651)

        onboarding = _onboarding()

        class _petTvScreen(DynAccessor):
            __slots__ = ()
            animations = DynAccessor(117652)

        petTvScreen = _petTvScreen()

        class _robotTvScreen(DynAccessor):
            __slots__ = ()
            tv_screen_active = DynAccessor(117653)
            tv_screen_idle = DynAccessor(117654)

        robotTvScreen = _robotTvScreen()

    new_year = _new_year()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(117655)
        Ch57_BZT_70 = DynAccessor(117656)
        F134_ARL_Projet_F = DynAccessor(117657)
        G184_EisBaer = DynAccessor(117658)
        GB140_Champion = DynAccessor(117659)
        R124_Object_279 = DynAccessor(117660)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(117661)
        operation_10 = DynAccessor(117662)
        operation_8 = DynAccessor(117663)
        operation_9 = DynAccessor(117664)
        operation_99 = DynAccessor(117665)
        video_operations_person = DynAccessor(117666)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(117667)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(117668)

    vehicle = _vehicle()